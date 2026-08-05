"""
CloudShield Enterprise
Tool Registry
"""


class ToolRegistry:

    def __init__(self):

        self._tools = {}

    def register(self, tool):

        self._tools[tool.name] = tool

    def unregister(self, name):

<<<<<<< HEAD
        self._tools.pop(name, None)

    def get(self, name):

        return self._tools.get(name)
=======
        self._tools.pop(

            name,

            None

        )

    def get(self, name):

        return self._tools.get(

            name

        )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

    def all(self):

        return self._tools

    def names(self):

<<<<<<< HEAD
        return list(self._tools.keys())

    def exists(self, name):

        return name in self._tools
=======
        return list(

            self._tools.keys()

        )

    def exists(self, name):

        return name in self._tools
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
