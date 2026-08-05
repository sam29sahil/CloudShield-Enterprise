"""
CloudShield Enterprise
Threat Intelligence Routes
"""

from flask import render_template, request
from flask_login import login_required

from app.threat import threat
from app.threat.services import ThreatService

service = ThreatService()


@threat.route("/")
@login_required
def dashboard():

    data = service.dashboard()

<<<<<<< HEAD
    return render_template("threat/dashboard.html", data=data)

=======
    return render_template(

        "threat/dashboard.html",

        data=data

    )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

@threat.route("/cve")
@login_required
def cve():

    keyword = request.args.get("search", "").strip()

    if keyword:

        cves = service.search_cves(keyword)

    else:

        cves = service.all_cves()

<<<<<<< HEAD
    return render_template("threat/cve.html", cves=cves, keyword=keyword)

=======
    return render_template(

        "threat/cve.html",

        cves=cves,

        keyword=keyword

    )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

@threat.route("/mitre")
@login_required
def mitre():

    techniques = service.mitre()

<<<<<<< HEAD
    return render_template("threat/mitre.html", techniques=techniques)

=======
    return render_template(

        "threat/mitre.html",

        techniques=techniques

    )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

@threat.route("/ioc")
@login_required
def ioc():

    iocs = service.iocs()

<<<<<<< HEAD
    return render_template("threat/ioc.html", iocs=iocs)

=======
    return render_template(

        "threat/ioc.html",

        iocs=iocs

    )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

@threat.route("/feeds")
@login_required
def feeds():

    feeds = service.feeds()

<<<<<<< HEAD
    return render_template("threat/feeds.html", feeds=feeds)
=======
    return render_template(

        "threat/feeds.html",

        feeds=feeds

    )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
