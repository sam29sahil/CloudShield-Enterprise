"""
CloudShield Enterprise
Asset Service
"""

from app.extensions import db
from app.models.asset import Asset


class AssetManager:

<<<<<<< HEAD
    def create_asset(self, name, target, asset_type, project_id):

        asset = Asset(
            project_id=project_id, name=name, target=target, asset_type=asset_type
=======
    def create_asset(
        self,
        name,
        target,
        asset_type,
        project_id
    ):

        asset = Asset(

            project_id=project_id,

            name=name,

            target=target,

            asset_type=asset_type

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
        )

        db.session.add(asset)

        db.session.commit()

        return asset

    def all_assets(self):

<<<<<<< HEAD
        return Asset.query.order_by(Asset.created_at.desc()).all()
=======
        return (

            Asset.query

            .order_by(Asset.created_at.desc())

            .all()

        )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

    def get(self, asset_id):

        return Asset.query.get_or_404(asset_id)

<<<<<<< HEAD
    def update_asset(self, asset_id, name, target, asset_type, project_id):
=======
    def update_asset(

        self,

        asset_id,

        name,

        target,

        asset_type,

        project_id

    ):
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

        asset = Asset.query.get_or_404(asset_id)

        asset.name = name

        asset.target = target

        asset.asset_type = asset_type

        asset.project_id = project_id

        db.session.commit()

        return asset

    def delete_asset(self, asset_id):

        asset = Asset.query.get_or_404(asset_id)

        db.session.delete(asset)

        db.session.commit()

<<<<<<< HEAD
    def update_scan(self, asset_id, score, risk, findings):
=======
    def update_scan(

        self,

        asset_id,

        score,

        risk,

        findings

    ):
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

        asset = Asset.query.get_or_404(asset_id)

        asset.score = score

        asset.risk = risk

        db.session.commit()

        return asset

    def total_assets(self):

        return Asset.query.count()

    def critical_assets(self):

<<<<<<< HEAD
        return Asset.query.filter_by(risk="Critical").count()

=======
        return (

            Asset.query

            .filter_by(risk="Critical")

            .count()

        )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
    def search(self, keyword=""):

        query = Asset.query

        if keyword:

            keyword = f"%{keyword}%"

            query = query.filter(
<<<<<<< HEAD
                db.or_(
                    Asset.name.ilike(keyword),
                    Asset.target.ilike(keyword),
                    Asset.asset_type.ilike(keyword),
                )
            )

    def filter_assets(self, search="", risk="", asset_type="", project=""):
=======

                db.or_(

                    Asset.name.ilike(keyword),

                    Asset.target.ilike(keyword),

                    Asset.asset_type.ilike(keyword)

                )

            )

    def filter_assets(

        self,

        search="",

        risk="",

        asset_type="",

        project=""

    ):
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

        query = Asset.query

        if search:

            keyword = f"%{search}%"

            query = query.filter(
<<<<<<< HEAD
                db.or_(Asset.name.ilike(keyword), Asset.target.ilike(keyword))
=======

                db.or_(

                    Asset.name.ilike(keyword),

                    Asset.target.ilike(keyword)

                )

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
            )

        if risk:

            query = query.filter_by(risk=risk)

        if asset_type:

            query = query.filter_by(asset_type=asset_type)

        if project:

            query = query.filter_by(project_id=project)

<<<<<<< HEAD
        return query.order_by(Asset.created_at.desc()).all()
=======
        return (

            query

            .order_by(Asset.created_at.desc())

            .all()

        )

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

    def projects(self):

        from app.models.project import Project

<<<<<<< HEAD
        return Project.query.order_by(Project.name).all()
=======
        return Project.query.order_by(Project.name).all()        

        
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
