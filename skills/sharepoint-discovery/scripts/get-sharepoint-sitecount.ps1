<#
.SYNOPSIS
    Returns total SharePoint Online site collection count.

.DESCRIPTION
    Connects to SharePoint Online Admin Center using PnP PowerShell
    and retrieves the total number of site collections.

.OUTPUT
    JSON
#>

param(
    [Parameter(Mandatory = $true)]
    [string]$TenantName,

    [Parameter(Mandatory = $true)]
    [string]$ClientId
)

try {

    $adminUrl = "https://$TenantName-admin.sharepoint.com"

    Connect-PnPOnline `
        -Url $adminUrl `
        -ClientId $ClientId `
        -Interactive

    $sites = Get-PnPTenantSite

    $result = @{
        TotalSiteCount = $sites.Count
    }

    $result | ConvertTo-Json -Compress

    Disconnect-PnPOnline
}
catch {

    $errorResult = @{
        error = $_.Exception.Message
    }

    $errorResult | ConvertTo-Json -Compress

    exit 1
}