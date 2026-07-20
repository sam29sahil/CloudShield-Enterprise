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

    return render_template(

        "threat/dashboard.html",

        data=data

    )

@threat.route("/cve")
@login_required
def cve():

    keyword = request.args.get("search", "").strip()

    if keyword:

        cves = service.search_cves(keyword)

    else:

        cves = service.all_cves()

    return render_template(

        "threat/cve.html",

        cves=cves,

        keyword=keyword

    )

@threat.route("/mitre")
@login_required
def mitre():

    techniques = service.mitre()

    return render_template(

        "threat/mitre.html",

        techniques=techniques

    )

@threat.route("/ioc")
@login_required
def ioc():

    iocs = service.iocs()

    return render_template(

        "threat/ioc.html",

        iocs=iocs

    )

@threat.route("/feeds")
@login_required
def feeds():

    feeds = service.feeds()

    return render_template(

        "threat/feeds.html",

        feeds=feeds

    )