"""
CloudShield Enterprise
Duplicate Finding Remover
"""


class Deduplicator:

    def remove(self, findings):

        unique = {}

        for finding in findings:

            key = (

                finding.title,

                finding.target,

                finding.source

            )

            unique[key] = finding

        return list(unique.values())