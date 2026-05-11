param(
    [string]$Tenant,
    [string]$ClientId
)

Connect-PnPOnline `
    -Url "https://$Tenant-admin.sharepoint.com" `
    -ClientId $ClientId `
    -Interactive

$sites = Get-PnPTenantSite

$count = $sites.Count

Write-Output $count