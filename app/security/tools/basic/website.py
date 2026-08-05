"""
CloudShield Enterprise
Website Scanner
"""

import time
import requests

<<<<<<< HEAD
from app.security.constants import HTTP_TIMEOUT, USER_AGENT
=======
from app.security.constants import (
    HTTP_TIMEOUT,
    USER_AGENT
)
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5


class WebsiteScanner:
    """
    Website Scanner
    """

    def __init__(self):
        self.name = "Website Scanner"

    def scan(self, target):
        """
        Scan a website.
        """
        return website_scan(target)


def website_scan(url):
    """
    Perform website scan.
    """

    start_time = time.perf_counter()

    try:

        response = requests.get(
            url,
            timeout=HTTP_TIMEOUT,
            allow_redirects=True,
<<<<<<< HEAD
            headers={"User-Agent": USER_AGENT},
=======
            headers={
                "User-Agent": USER_AGENT
            }
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
        )

        end_time = time.perf_counter()

        return {
<<<<<<< HEAD
            "success": True,
            "url": response.url,
            "status_code": response.status_code,
            "reason": response.reason,
            "https": response.url.startswith("https"),
            "response_time": round(end_time - start_time, 3),
            "redirects": len(response.history),
            "server": response.headers.get("Server", "Unknown"),
            "content_type": response.headers.get("Content-Type", "Unknown"),
            "content_length": response.headers.get("Content-Length", "Unknown"),
            "encoding": response.encoding,
            "cookies": list(response.cookies.keys()),
            "headers": dict(response.headers),
            "html": response.text,
=======

            "success": True,

            "url": response.url,

            "status_code": response.status_code,

            "reason": response.reason,

            "https": response.url.startswith("https"),

            "response_time": round(
                end_time - start_time,
                3
            ),

            "redirects": len(response.history),

            "server": response.headers.get(
                "Server",
                "Unknown"
            ),

            "content_type": response.headers.get(
                "Content-Type",
                "Unknown"
            ),

            "content_length": response.headers.get(
                "Content-Length",
                "Unknown"
            ),

            "encoding": response.encoding,

            "cookies": list(
                response.cookies.keys()
            ),

            "headers": dict(
                response.headers
            ),

            "html": response.text

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
        }

    except requests.exceptions.Timeout:

<<<<<<< HEAD
        return {"success": False, "error": "Connection timed out."}

    except requests.exceptions.ConnectionError:

        return {"success": False, "error": "Unable to connect."}

    except requests.exceptions.RequestException as e:

        return {"success": False, "error": str(e)}
=======
        return {

            "success": False,

            "error": "Connection timed out."

        }

    except requests.exceptions.ConnectionError:

        return {

            "success": False,

            "error": "Unable to connect."

        }

    except requests.exceptions.RequestException as e:

        return {

            "success": False,

            "error": str(e)

        }
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
