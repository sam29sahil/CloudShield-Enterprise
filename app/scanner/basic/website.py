"""
CloudShield Enterprise
Website Scanner
"""

import time
import requests

from app.scanner.constants import (
    HTTP_TIMEOUT,
    USER_AGENT
)


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

            headers={
                "User-Agent": USER_AGENT
            }

        )

        end_time = time.perf_counter()

        return {

            "success": True,

            "url": response.url,

            "status_code": response.status_code,

            "reason": response.reason,

            "https": response.url.startswith("https"),

            "response_time": round(
                end_time - start_time,
                3
            ),

            "redirects": len(
                response.history
            ),

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

        }

    except requests.exceptions.Timeout:

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