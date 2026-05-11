import os
import subprocess

from dotenv import load_dotenv
from langchain_core.tools import tool

load_dotenv()


@tool
def get_sharepoint_sites_count() -> str:
    """
    Get total SharePoint Online sites count using PnP PowerShell.
    """

    tenant = os.getenv("TENANT_NAME")
    client_id = os.getenv("CLIENT_ID")

    script_path = r"scripts/get_sites_count.ps1"

    command = [
        "pwsh",
        "-ExecutionPolicy",
        "Bypass",
        "-File",
        script_path,
        "-Tenant",
        tenant,
        "-ClientId",
        client_id
    ]

    result = subprocess.run(
        command,
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        return f"Error: {result.stderr}"

    count = result.stdout.strip()

    return f"Total SharePoint Sites Count: {count}"
