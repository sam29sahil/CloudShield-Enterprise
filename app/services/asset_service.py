"""
CloudShield Enterprise
Asset Service
"""

from app.extensions import db
from app.models.asset import Asset


class AssetService:

    def all(self):

        return Asset.query.all()

    def get(self, asset_id):

        return Asset.query.get(asset_id)

<<<<<<< HEAD
    def create(self, project_id, name, target, asset_type):

        asset = Asset(
            project_id=project_id, name=name, target=target, asset_type=asset_type
=======
    def create(

        self,

        project_id,

        name,

        target,

        asset_type

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

<<<<<<< HEAD
    def update_score(self, asset, score, risk):
=======
    def update_score(

        self,

        asset,

        score,

        risk

    ):
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

        asset.score = score

        asset.risk = risk

        db.session.commit()
<<<<<<< HEAD
=======
        
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
