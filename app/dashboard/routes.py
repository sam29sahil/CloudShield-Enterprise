"""
CloudShield Enterprise
Dashboard Routes
"""

from flask import render_template
from flask_login import login_required, current_user

from app.dashboard import dashboard
from app.models import SecurityScan


@dashboard.route("/")
@login_required
def home():

    scans = SecurityScan.query.filter_by(
        user_id=current_user.id
    ).all()

    total_scans = len(scans)

    successful = sum(    
        1 for s in scans
        if s.status == "Completed"
    )

    failed = sum(    
        1 for s in scans
        if s.status == "Failed"
    )

    critical = sum(    
        1 for s in scans
        if s.risk == "Critical"
    )

    high = sum(    
        1 for s in scans
        if s.risk == "High"
    )

    medium = sum(    
        1 for s in scans
        if s.risk == "Medium"
    )

    low = sum(    
        1 for s in scans
        if s.risk == "Low"
   )

    average_score = 0

    if scans:    

        average_score = round(

            sum(s.score for s in scans) / len(scans),

            2

        )

    recent_scans = (

        SecurityScan.query

        .filter_by(user_id=current_user.id)

        .order_by(SecurityScan.started_at.desc())

        .limit(10)

        .all()

    )

    return render_template(

        "dashboard/index.html",

    total_scans=total_scans,

    successful=successful,

    failed=failed,

    critical=critical,

    high=high,

    medium=medium,

    low=low,

    average_score=average_score,

    recent_scans=recent_scans

)