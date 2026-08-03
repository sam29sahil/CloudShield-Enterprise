"""
CloudShield Enterprise
Kubernetes Report Generator
"""

from app.kubernetes.scanner import KubernetesScanner
from app.kubernetes.analyzer import KubernetesAnalyzer
from app.kubernetes.benchmark import KubernetesBenchmark


class KubernetesReport:

    def generate(self):

        scanner = KubernetesScanner()

        analyzer = KubernetesAnalyzer()

        benchmark = KubernetesBenchmark()

        data = scanner.scan()

        findings = analyzer.analyze(data)

        security = benchmark.evaluate(findings)

        recommendations = [

            "Keep Kubernetes version updated.",

            "Restrict public LoadBalancer services.",

            "Monitor pod security policies.",

            "Review RBAC permissions regularly.",

            "Enable audit logging."

        ]

        return {

            "dashboard": data,

            "security": security,

            "recommendations": recommendations

        }