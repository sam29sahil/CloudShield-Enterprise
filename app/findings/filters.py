"""
CloudShield Enterprise
Finding Filters
"""

from app.models.finding import Finding


class FindingFilters:
    """
    Enterprise Finding Query Builder
    """

    def __init__(self):

        self.query = Finding.query

    # =====================================================
    # RESET
    # =====================================================

    def reset(self):

        self.query = Finding.query

        return self

    # =====================================================
    # SEARCH
    # =====================================================

    def search(self, keyword):

        if keyword:

            self.query = self.query.filter(
<<<<<<< HEAD
                Finding.title.ilike(f"%{keyword}%")
                | Finding.description.ilike(f"%{keyword}%")
                | Finding.category.ilike(f"%{keyword}%")
=======

                Finding.title.ilike(f"%{keyword}%")

                |

                Finding.description.ilike(f"%{keyword}%")

                |

                Finding.category.ilike(f"%{keyword}%")

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
            )

        return self

    # =====================================================
    # SEVERITY
    # =====================================================

    def severity(self, severity):

        if severity:

<<<<<<< HEAD
            self.query = self.query.filter(Finding.severity == severity)
=======
            self.query = self.query.filter(

                Finding.severity == severity

            )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

        return self

    # =====================================================
    # STATUS
    # =====================================================

    def status(self, status):

        if status:

<<<<<<< HEAD
            self.query = self.query.filter(Finding.status == status)
=======
            self.query = self.query.filter(

                Finding.status == status

            )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

        return self

    # =====================================================
    # CATEGORY
    # =====================================================

    def category(self, category):

        if category:

<<<<<<< HEAD
            self.query = self.query.filter(Finding.category == category)

        return self

        # =====================================================

=======
            self.query = self.query.filter(

                Finding.category == category

            )

        return self
    
        # =====================================================
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
    # PROJECT
    # =====================================================

    def project(self, project_id):

        if project_id:

<<<<<<< HEAD
            self.query = self.query.filter(Finding.project_id == project_id)
=======
            self.query = self.query.filter(

                Finding.project_id == project_id

            )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

        return self

    # =====================================================
    # ASSET
    # =====================================================

    def asset(self, asset_id):

        if asset_id:

<<<<<<< HEAD
            self.query = self.query.filter(Finding.asset_id == asset_id)
=======
            self.query = self.query.filter(

                Finding.asset_id == asset_id

            )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

        return self

    # =====================================================
    # SCAN
    # =====================================================

    def scan(self, scan_id):

        if scan_id:

<<<<<<< HEAD
            self.query = self.query.filter(Finding.scan_id == scan_id)
=======
            self.query = self.query.filter(

                Finding.scan_id == scan_id

            )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

        return self

    # =====================================================
    # FALSE POSITIVE
    # =====================================================

    def false_positive(self, enabled=None):

        if enabled is not None:

<<<<<<< HEAD
            self.query = self.query.filter(Finding.false_positive == enabled)
=======
            self.query = self.query.filter(

                Finding.false_positive == enabled

            )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

        return self

    # =====================================================
    # MIN CVSS
    # =====================================================

    def min_cvss(self, value):

        if value is not None:

<<<<<<< HEAD
            self.query = self.query.filter(Finding.cvss >= value)
=======
            self.query = self.query.filter(

                Finding.cvss >= value

            )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

        return self

    # =====================================================
    # MAX CVSS
    # =====================================================

    def max_cvss(self, value):

        if value is not None:

<<<<<<< HEAD
            self.query = self.query.filter(Finding.cvss <= value)
=======
            self.query = self.query.filter(

                Finding.cvss <= value

            )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

        return self

    # =====================================================
    # DATE FROM
    # =====================================================

    def date_from(self, date):

        if date:

<<<<<<< HEAD
            self.query = self.query.filter(Finding.created_at >= date)
=======
            self.query = self.query.filter(

                Finding.created_at >= date

            )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

        return self

    # =====================================================
    # DATE TO
    # =====================================================

    def date_to(self, date):

        if date:

<<<<<<< HEAD
            self.query = self.query.filter(Finding.created_at <= date)

        return self

        # =====================================================

=======
            self.query = self.query.filter(

                Finding.created_at <= date

            )

        return self
    
        # =====================================================
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
    # ORDER BY
    # =====================================================

    def order_by(self, field="created_at", direction="desc"):

        column = getattr(Finding, field, Finding.created_at)

        if direction.lower() == "asc":

            self.query = self.query.order_by(column.asc())

        else:

            self.query = self.query.order_by(column.desc())

        return self

    # =====================================================
    # PAGINATION
    # =====================================================

    def paginate(self, page=1, per_page=20):

<<<<<<< HEAD
        return self.query.paginate(page=page, per_page=per_page, error_out=False)
=======
        return self.query.paginate(

            page=page,

            per_page=per_page,

            error_out=False

        )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

    # =====================================================
    # LIMIT
    # =====================================================

    def limit(self, value):

        self.query = self.query.limit(value)

        return self

    # =====================================================
    # ALL
    # =====================================================

    def all(self):

        return self.query.all()

    # =====================================================
    # FIRST
    # =====================================================

    def first(self):

        return self.query.first()

    # =====================================================
    # COUNT
    # =====================================================

    def count(self):

        return self.query.count()

    # =====================================================
    # APPLY FILTERS
    # =====================================================

    def apply(self, filters):

        self.reset()

        self.search(filters.get("search"))

        self.severity(filters.get("severity"))

        self.status(filters.get("status"))

        self.category(filters.get("category"))

        self.project(filters.get("project"))

        self.asset(filters.get("asset"))

        self.scan(filters.get("scan"))

        self.false_positive(filters.get("false_positive"))

        self.min_cvss(filters.get("min_cvss"))

        self.max_cvss(filters.get("max_cvss"))

        self.date_from(filters.get("date_from"))

        self.date_to(filters.get("date_to"))

        self.order_by(
<<<<<<< HEAD
            filters.get("sort", "created_at"), filters.get("direction", "desc")
        )

        return self
=======

            filters.get("sort", "created_at"),

            filters.get("direction", "desc")

        )

        return self
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
