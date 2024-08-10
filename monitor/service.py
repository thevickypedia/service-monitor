import psutil
import subprocess
import platform

from http import HTTPStatus
from monitor.squire import ServiceStatus
from monitor.exceptions import ServiceNotFound, UnSupportedOS

current_os = platform.system()

if current_os not in ("Darwin", "Linux", "Windows"):
    raise UnSupportedOS(
        f"{current_os} is unsupported.\n\t"
        "Host machine should either be macOS, Windows or any of Linux distros"
    )


def get_pid(service_name: str) -> int:
    """Get process ID for a particular service.

    Args:
        service_name (str): Name of the service.

    Returns:
        int:
        Process ID running the service.
    """
    for proc in psutil.process_iter(['pid', 'name']):
        if proc.info['name'] == service_name:
            return proc.info['pid']


def get_service_status(service_name: str) -> ServiceStatus:
    """Get service status.

    Args:
        service_name (str): Name of the service.

    Raises:
        ServiceNotFound: When the service could not be found.

    Returns:
        ServiceStatus:
        Returns an instance of the ServiceStatus.
    """
    # A service (eg: docker) may have multiple process IDs with different suffix names
    if not (pid := get_pid(service_name)):
        pid = 0000

    service_not_found = ServiceNotFound(
        f"Service {service_name!r} not found."
    )

    running = ServiceStatus(
        pid=pid,
        status_code=HTTPStatus.OK.real,
        description=f"{service_name} is running"
    )

    stopped = ServiceStatus(
        pid=pid,
        status_code=HTTPStatus.NOT_IMPLEMENTED.real,
        description=f"{service_name} has been stopped"
    )

    unknown = ServiceStatus(
        pid=pid,
        status_code=HTTPStatus.SERVICE_UNAVAILABLE.real,
        description=f"{service_name} - status unknwon"
    )

    if current_os == "Windows":
        # Windows: Use sc command
        cmd = f"sc query {service_name}"
        try:
            output = subprocess.check_output(cmd, shell=True, text=True)
            if "RUNNING" in output:
                return running
            elif "STOPPED" in output:
                return stopped
            else:
                return unknown
        except subprocess.CalledProcessError:
            raise service_not_found
    
    if current_os == "Linux":
        # Linux: Use systemctl
        cmd = f"systemctl is-active {service_name}"
        try:
            output = subprocess.check_output(cmd, shell=True, text=True).strip()
            if output == "active":
                return running
            elif output == "inactive":
                return stopped
            else:
                return ServiceStatus(
                    status_code=HTTPStatus.NOT_IMPLEMENTED.real,
                    description=f"{service_name} - {output}"
                )
        except subprocess.CalledProcessError:
            raise service_not_found
    
    if current_os == "Darwin":
        # macOS: Use launchctl
        cmd = f"launchctl list | grep {service_name}"
        try:
            output = subprocess.check_output(cmd, shell=True, text=True)
            if service_name in output:
                return running
            else:
                return stopped
        except subprocess.CalledProcessError:
            raise service_not_found
