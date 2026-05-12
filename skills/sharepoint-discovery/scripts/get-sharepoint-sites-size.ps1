<#
.SYNOPSIS
    Returns total size of SharePoint Online site collections.

.DESCRIPTION
    Connects to SharePoint Online Admin Center using PnP PowerShell
    and retrieves the combined storage size of all site collections.

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

    $totalSizeMB = 0

    foreach ($site in $sites) {
        $totalSizeMB += $site.StorageUsageCurrent
    }

    $totalSizeGB = [math]::Round($totalSizeMB / 1024, 2)

    $result = @{
        TotalSizeGB = $totalSizeGB
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