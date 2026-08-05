"""
CloudShield Enterprise
Finding Deduplicator
"""

from collections import defaultdict


class Deduplicator:
    """
    Enterprise Finding Deduplicator

    Removes duplicate findings generated
    by multiple scanners.
    """

    # =====================================================
    # SIGNATURE
    # =====================================================

    @staticmethod
    def signature(finding):

        return (
<<<<<<< HEAD
            finding.title.strip().lower(),
            finding.severity,
            finding.category,
            finding.project_id,
            finding.asset_id,
            finding.scan_id,
=======

            finding.title.strip().lower(),

            finding.severity,

            finding.category,

            finding.project_id,

            finding.asset_id,

            finding.scan_id

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
        )

    # =====================================================
    # REMOVE DUPLICATES
    # =====================================================

    @classmethod
    def remove(cls, findings):

        unique = {}

        duplicates = []

        for finding in findings:

            key = cls.signature(finding)

            if key in unique:

                duplicates.append(finding)

                continue

            unique[key] = finding

        return list(unique.values())

    # =====================================================
    # FIND DUPLICATES
    # =====================================================

    @classmethod
    def duplicates(cls, findings):

        seen = set()

        duplicate_list = []

        for finding in findings:

            key = cls.signature(finding)

            if key in seen:

                duplicate_list.append(finding)

            else:

                seen.add(key)

        return duplicate_list

    # =====================================================
    # COUNT DUPLICATES
    # =====================================================

    @classmethod
    def duplicate_count(cls, findings):

<<<<<<< HEAD
        return len(cls.duplicates(findings))

        # =====================================================

=======
        return len(

            cls.duplicates(findings)

        )
    
        # =====================================================
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
    # GROUP DUPLICATES
    # =====================================================

    @classmethod
    def group(cls, findings):

        groups = defaultdict(list)

        for finding in findings:

<<<<<<< HEAD
            groups[cls.signature(finding)].append(finding)
=======
            groups[

                cls.signature(finding)

            ].append(finding)
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

        return groups

    # =====================================================
    # MERGE DUPLICATES
    # =====================================================

    @classmethod
    def merge(cls, findings):

        merged = []

        groups = cls.group(findings)

        for duplicates in groups.values():

            primary = duplicates[0]

            # -------------------------
            # Highest CVSS
            # -------------------------

<<<<<<< HEAD
            primary.cvss = max(float(f.cvss or 0) for f in duplicates)
=======
            primary.cvss = max(

                float(

                    f.cvss or 0

                )

                for f in duplicates

            )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

            # -------------------------
            # Highest Severity
            # -------------------------

            severity_order = {
<<<<<<< HEAD
                "Critical": 5,
                "High": 4,
                "Medium": 3,
                "Low": 2,
                "Info": 1,
            }

            highest = max(duplicates, key=lambda x: severity_order.get(x.severity, 0))
=======

                "Critical": 5,

                "High": 4,

                "Medium": 3,

                "Low": 2,

                "Info": 1

            }

            highest = max(

                duplicates,

                key=lambda x: severity_order.get(

                    x.severity,

                    0

                )

            )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

            primary.severity = highest.severity

            merged.append(primary)

        return merged

    # =====================================================
    # KEEP HIGHEST CVSS
    # =====================================================

    @classmethod
    def highest_cvss(cls, findings):

        if not findings:

            return None

<<<<<<< HEAD
        return max(findings, key=lambda x: float(x.cvss or 0))
=======
        return max(

            findings,

            key=lambda x: float(

                x.cvss or 0

            )

        )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

    # =====================================================
    # KEEP HIGHEST SEVERITY
    # =====================================================

    @classmethod
    def highest_severity(cls, findings):

<<<<<<< HEAD
        order = {"Critical": 5, "High": 4, "Medium": 3, "Low": 2, "Info": 1}
=======
        order = {

            "Critical": 5,

            "High": 4,

            "Medium": 3,

            "Low": 2,

            "Info": 1

        }
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

        if not findings:

            return None

<<<<<<< HEAD
        return max(findings, key=lambda x: order.get(x.severity, 0))

        # =====================================================

=======
        return max(

            findings,

            key=lambda x: order.get(

                x.severity,

                0

            )

        )
    
        # =====================================================
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
    # MERGE RECOMMENDATIONS
    # =====================================================

    @classmethod
    def merge_recommendations(cls, findings):

        recommendations = []

        for finding in findings:

            recommendation = (finding.recommendation or "").strip()

            if recommendation and recommendation not in recommendations:

                recommendations.append(recommendation)

        return "\n\n".join(recommendations)

    # =====================================================
    # MERGE EVIDENCE
    # =====================================================

    @classmethod
    def merge_evidence(cls, findings):

        evidence = []

        for finding in findings:

            item = (finding.evidence or "").strip()

            if item and item not in evidence:

                evidence.append(item)

        return "\n\n".join(evidence)

    # =====================================================
    # MERGE CATEGORIES
    # =====================================================

    @classmethod
    def merge_categories(cls, findings):

        categories = []

        for finding in findings:

<<<<<<< HEAD
            if finding.category and finding.category not in categories:

                categories.append(finding.category)
=======
            if (

                finding.category

                and

                finding.category not in categories

            ):

                categories.append(

                    finding.category

                )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

        return categories

    # =====================================================
    # STATISTICS
    # =====================================================

    @classmethod
    def statistics(cls, findings):

        return {
<<<<<<< HEAD
            "original": len(findings),
            "duplicates": cls.duplicate_count(findings),
            "unique": len(cls.remove(findings)),
=======

            "original": len(findings),

            "duplicates": cls.duplicate_count(findings),

            "unique": len(cls.remove(findings))

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
        }

    # =====================================================
    # COMPLETE PACKAGE
    # =====================================================

    @classmethod
    def package(cls, findings):

        merged = cls.merge(findings)

        return {
<<<<<<< HEAD
            "statistics": cls.statistics(findings),
            "unique": merged,
            "duplicates": cls.duplicates(findings),
        }
=======

            "statistics": cls.statistics(findings),

            "unique": merged,

            "duplicates": cls.duplicates(findings)

        }
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
