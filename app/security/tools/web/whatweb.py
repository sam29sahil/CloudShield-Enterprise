"""
CloudShield Enterprise
WhatWeb Tool
"""

import subprocess

from app.security.core.command import Command
from app.security.core.parser import Parser
from app.security.core.result import Result
from app.security.core.target import Target
from app.security.tools.common.base import BaseTool


class WhatWebTool(BaseTool):

    name = "whatweb"

    display_name = "WhatWeb"

    category = "web"

    description = "Website Technology Detection"

    default_arguments = [

        "--color=never",

        "--log-json=-"

    ]

    timeout = 300

    def scan(
        self,
        target,
        arguments=None
    ):
        """Run WhatWeb through the shared scanner framework."""
        target_value = str(Target.parse(target))
        if arguments is None:
            arguments = []
        elif isinstance(arguments, str):
            arguments = [arguments]

        command = Command.build(
            "whatweb", self.default_arguments, arguments, target_value
        )
        try:
            process = command.run(timeout=self.timeout)
        except FileNotFoundError:
            return Result(
                success=False, tool=self.name, target=target_value,
                command=command.display, error="WhatWeb is not installed."
            ).to_dict()
        except subprocess.TimeoutExpired:
            return Result(
                success=False, tool=self.name, target=target_value,
                command=command.display, error="WhatWeb scan timed out."
            ).to_dict()

        output = process.stdout.strip()
        data = Parser.json(output, default=[])
        record = data[0] if isinstance(data, list) and data else {}
        technology = record.get("plugins", {}) if isinstance(record, dict) else {}
        return Result(
            success=process.returncode == 0,
            tool=self.name,
            target=target_value,
            command=command.display,
            return_code=process.returncode,
            stdout=output,
            stderr=process.stderr.strip(),
            data={"technology": technology, "raw_output": output},
        ).to_dict()

    # Legacy callers used execute(); retain that public method during migration.
    def execute(self, target, arguments=None):
        return self.scan(target, arguments)


def get_tool():

    return WhatWebTool()
