"""
CloudShield Enterprise
WhatWeb Parser
"""


class WhatWebParser:

    def parse(self, output):

        technologies = []

        parts = output.split(",")

        for item in parts:

            item = item.strip()

            if item:

                technologies.append(item)

        return {"count": len(technologies), "technologies": technologies}
