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

        )

        db.session.add(asset)

        db.session.commit()

        return asset

    def update_score(

        self,

        asset,

        score,

        risk

    ):

        asset.score = score

        asset.risk = risk

        db.session.commit()
        