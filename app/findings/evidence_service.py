import os

from werkzeug.utils import secure_filename

from flask import current_app

from app.extensions import db
from app.models.evidence import Evidence


class EvidenceService:

    @staticmethod
    def allowed(filename):

        if "." not in filename:
            return False

        extension = filename.rsplit(".", 1)[1].lower()

<<<<<<< HEAD
        return extension in current_app.config["ALLOWED_EVIDENCE_EXTENSIONS"]
=======
        return extension in current_app.config[
            "ALLOWED_EVIDENCE_EXTENSIONS"
        ]
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

    @staticmethod
    def upload(file, finding_id):

        if not file:
            return None

        if file.filename == "":
            return None

        if not EvidenceService.allowed(file.filename):
            return None

        filename = secure_filename(file.filename)

        # ==========================================
        # Create folder for this finding
        # ==========================================

        finding_folder = os.path.join(
<<<<<<< HEAD
            current_app.config["UPLOAD_FOLDER"], f"finding_{finding_id}"
        )

        os.makedirs(finding_folder, exist_ok=True)

        filepath = os.path.join(finding_folder, filename)
=======
            current_app.config["UPLOAD_FOLDER"],
            f"finding_{finding_id}"
        )

        os.makedirs(
            finding_folder,
            exist_ok=True
        )

        filepath = os.path.join(
            finding_folder,
            filename
        )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

        file.save(filepath)

        evidence = Evidence(
<<<<<<< HEAD
            finding_id=finding_id,
            filename=filename,
            filepath=filepath,
            filetype=file.content_type,
=======

            finding_id=finding_id,

            filename=filename,

            filepath=filepath,

            filetype=file.content_type

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
        )

        db.session.add(evidence)

        db.session.commit()

<<<<<<< HEAD
        return evidence
=======
        return evidence
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
