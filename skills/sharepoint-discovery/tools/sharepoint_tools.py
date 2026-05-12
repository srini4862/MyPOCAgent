from pathlib import Path
import subprocess
import json

from langchain.tools import tool


# Resolve skill root dynamically
SKILL_ROOT = Path(__file__).resolve().parent.parent

# Script base path
SCRIPT_BASE_PATH = SKILL_ROOT / "scripts"


@tool
def get_sharepoint_sitecount(
    tenant_name: str,
    client_id: str
) -> dict:
    """
    Returns the total number of SharePoint Online site collections.

    Use this tool when the user asks about:
    - SharePoint site count
    - SharePoint discovery
    - SharePoint inventory
    - migration sizing
    - SharePoint assessment

    Parameters:
    - tenant_name: Microsoft 365 tenant name
    - client_id: Azure AD App Registration Client ID

    Returns:
    {
        "TotalSiteCount": number
    }
    """
    SCRIPT_PATH = SCRIPT_BASE_PATH / "get-sharepoint-sitecount.ps1"
    command = [
        "pwsh",
        str(SCRIPT_PATH),
        "-TenantName",
        tenant_name,
        "-ClientId",
        client_id
    ]

    result = subprocess.run(
        command,
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        raise Exception(
            f"PowerShell script execution failed: {result.stderr}"
        )

    stdout = result.stdout.strip()

    if not stdout:
        raise Exception("Script returned empty output")

    return json.loads(stdout)


@tool
def get_sharepoint_sites_size(
    tenant_name: str,
    client_id: str
) -> dict:
    """
    Returns the total size of all SharePoint Online site collections in GB.

    Use this tool when the user asks about:
    - SharePoint storage size
    - SharePoint total size
    - SharePoint migration sizing
    - SharePoint storage assessment
    - SharePoint capacity analysis
    - SharePoint inventory sizing

    Parameters:
    - tenant_name: Microsoft 365 tenant name
    - client_id: Azure AD App Registration Client ID

    Returns:
    {
        "TotalSizeGB": number
    }
    """

    SCRIPT_PATH = SCRIPT_BASE_PATH / "get-sharepoint-sites-size.ps1"

    command = [
        "pwsh",
        str(SCRIPT_PATH),
        "-TenantName",
        tenant_name,
        "-ClientId",
        client_id
    ]

    result = subprocess.run(
        command,
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        raise Exception(
            f"PowerShell script execution failed: {result.stderr}"
        )

    stdout = result.stdout.strip()

    if not stdout:
        raise Exception("Script returned empty output")

    return json.loads(stdout)
