import time

from fastapi.responses import HTMLResponse
from pydantic import BaseModel


async def clear_session(response: HTMLResponse) -> HTMLResponse:
    """Clear the session token from the response.

    Args:
        response: Takes the ``Response`` object as an argument.

    Returns:
        Response:
        Returns the response object with the session token cleared.
    """
    response.delete_cookie("session_token")
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Authorization"] = ""
    return response


async def get_expiry(lease_start: int, lease_duration: int) -> str:
    """Get expiry datetime as string using max age.

    Args:
        lease_start: Time when the authentication was made.
        lease_duration: Number of seconds until expiry.

    Returns:
        str:
        Returns the date and time of expiry in GMT.
    """
    end = time.gmtime(lease_start + lease_duration)
    return time.strftime("%a, %d-%b-%Y %T GMT", end)


class Static(BaseModel):
    """Object to store static values.

    >>> Static

    """

    login_endpoint: str = "/login"
    logout_endpoint: str = "/logout"
    monitor_endpoint: str = "/monitor"


static = Static()
