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

<<<<<<< HEAD
        return {"count": len(technologies), "technologies": technologies}
=======
        return {

            "count": len(technologies),

            "technologies": technologies

        }
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
