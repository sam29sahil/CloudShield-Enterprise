"""
CloudShield Enterprise
Nmap Result Parser
"""


class NmapParser:
    """
    Parse Nmap Results
    """

<<<<<<< HEAD
    def summary(self, result):
=======
    def summary(

        self,

        result

    ):
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

        if not result.get("success"):

            return {}

<<<<<<< HEAD
        ports = result.get("ports", [])

        open_ports = [p for p in ports if p["state"] == "open"]

        return {
            "target": result["target"],
            "hostname": result["hostname"],
            "state": result["state"],
            "total_ports": len(ports),
            "open_ports": len(open_ports),
            "os": result["os"],
        }

    def services(self, result):

        services = []

        for port in result.get("ports", []):

            services.append(
                {
                    "port": port["port"],
                    "service": port["service"],
                    "version": port["version"],
                }
            )

        return services
=======
        ports = result.get(

            "ports",

            []

        )

        open_ports = [

            p for p in ports

            if p["state"] == "open"

        ]

        return {

            "target": result["target"],

            "hostname": result["hostname"],

            "state": result["state"],

            "total_ports": len(ports),

            "open_ports": len(open_ports),

            "os": result["os"]

        }

    def services(

        self,

        result

    ):

        services = []

        for port in result.get(

            "ports",

            []

        ):

            services.append({

                "port": port["port"],

                "service": port["service"],

                "version": port["version"]

            })

        return services
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
