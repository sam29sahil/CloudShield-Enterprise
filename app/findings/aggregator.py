"""
CloudShield Enterprise
Finding Aggregator
"""

from collections import Counter, defaultdict


class FindingAggregator:
    """
    Enterprise Finding Aggregator

    Aggregates findings for dashboards,
    reports and analytics.
    """

    # =====================================================
    # SEVERITY
    # =====================================================

    @staticmethod
    def by_severity(findings):

        result = Counter()

        for finding in findings:

            result[finding.severity] += 1

        return dict(result)

    # =====================================================
    # CATEGORY
    # =====================================================

    @staticmethod
    def by_category(findings):

        result = Counter()

        for finding in findings:

            result[finding.category] += 1

        return dict(result)

    # =====================================================
    # STATUS
    # =====================================================

    @staticmethod
    def by_status(findings):

        result = Counter()

        for finding in findings:

            result[finding.status] += 1

        return dict(result)

    # =====================================================
    # PROJECT
    # =====================================================

    @staticmethod
    def by_project(findings):

        result = Counter()

        for finding in findings:

            result[finding.project_id] += 1

        return dict(result)

    # =====================================================
    # ASSET
    # =====================================================

    @staticmethod
    def by_asset(findings):

        result = Counter()

        for finding in findings:

            result[finding.asset_id] += 1

        return dict(result)
    
        # =====================================================
    # SCAN
    # =====================================================

    @staticmethod
    def by_scan(findings):

        result = Counter()

        for finding in findings:

            result[finding.scan_id] += 1

        return dict(result)

    # =====================================================
    # CVSS
    # =====================================================

    @staticmethod
    def cvss(findings):

        if not findings:

            return {

                "average": 0,

                "maximum": 0,

                "minimum": 0

            }

        scores = [

            float(f.cvss or 0)

            for f in findings

        ]

        return {

            "average": round(

                sum(scores) / len(scores),

                2

            ),

            "maximum": max(scores),

            "minimum": min(scores)

        }

    # =====================================================
    # RISK SCORE
    # =====================================================

    @staticmethod
    def risk_score(findings):

        weights = {

            "Critical": 10,

            "High": 7,

            "Medium": 5,

            "Low": 2,

            "Info": 0

        }

        score = 0

        for finding in findings:

            if finding.status != "Resolved":

                score += weights.get(

                    finding.severity,

                    0

                )

        return score

    # =====================================================
    # OPEN / RESOLVED
    # =====================================================

    @staticmethod
    def resolution(findings):

        return {

            "open": len([

                f for f in findings

                if f.status == "Open"

            ]),

            "resolved": len([

                f for f in findings

                if f.status == "Resolved"

            ])

        }

    # =====================================================
    # FALSE POSITIVES
    # =====================================================

    @staticmethod
    def false_positives(findings):

        return len([

            f

            for f in findings

            if f.false_positive

        ])

    # =====================================================
    # TOP ASSETS
    # =====================================================

    @staticmethod
    def top_assets(findings, limit=10):

        assets = Counter()

        for finding in findings:

            assets[finding.asset_id] += 1

        return assets.most_common(limit)

    # =====================================================
    # TOP PROJECTS
    # =====================================================

    @staticmethod
    def top_projects(findings, limit=10):

        projects = Counter()

        for finding in findings:

            projects[finding.project_id] += 1

        return projects.most_common(limit)
    
        # =====================================================
    # EXECUTIVE SUMMARY
    # =====================================================

    @staticmethod
    def executive_summary(findings):

        return {

            "total": len(findings),

            "severity": FindingAggregator.by_severity(findings),

            "status": FindingAggregator.by_status(findings),

            "categories": FindingAggregator.by_category(findings),

            "risk_score": FindingAggregator.risk_score(findings),

            "cvss": FindingAggregator.cvss(findings)

        }

    # =====================================================
    # DASHBOARD DATA
    # =====================================================

    @staticmethod
    def dashboard(findings):

        return {

            "summary": FindingAggregator.executive_summary(

                findings

            ),

            "top_assets": FindingAggregator.top_assets(

                findings

            ),

            "top_projects": FindingAggregator.top_projects(

                findings

            ),

            "false_positives": FindingAggregator.false_positives(

                findings

            ),

            "resolution": FindingAggregator.resolution(

                findings

            )

        }

    # =====================================================
    # TIMELINE
    # =====================================================

    @staticmethod
    def timeline(findings):

        timeline = defaultdict(int)

        for finding in findings:

            if finding.created_at:

                key = finding.created_at.strftime(

                    "%Y-%m-%d"

                )

                timeline[key] += 1

        return dict(

            sorted(

                timeline.items()

            )

        )

    # =====================================================
    # MONTHLY TREND
    # =====================================================

    @staticmethod
    def monthly(findings):

        trend = defaultdict(int)

        for finding in findings:

            if finding.created_at:

                key = finding.created_at.strftime(

                    "%Y-%m"

                )

                trend[key] += 1

        return dict(

            sorted(

                trend.items()

            )

        )

    # =====================================================
    # COMPLETE PACKAGE
    # =====================================================

    @staticmethod
    def package(findings):

        return {

            "dashboard": FindingAggregator.dashboard(

                findings

            ),

            "timeline": FindingAggregator.timeline(

                findings

            ),

            "monthly": FindingAggregator.monthly(

                findings

            )

        }