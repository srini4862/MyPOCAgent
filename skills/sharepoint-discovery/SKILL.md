---
name: sharepoint-discovery
description: Use this skill for SharePoint Online discovery, inventory, and migration assessment tasks.
license: WFX Team
metadata: 
  author: wfx-org
  version: "1.0"
---

# SharePoint Discovery Skill

## Purpose

This skill helps analyze SharePoint Online environments for:
- discovery
- inventory
- migration assessment
- tenant sizing

## Available Tools

### get_sharepoint_sitecount

Purpose:
Returns the total number of SharePoint Online site collections.

Use this tool when the user asks:
- How many SharePoint sites exist
- SharePoint inventory count
- SharePoint discovery metrics
- Migration assessment sizing

Backend Script:
./scripts/get-sharepoint-sitecount.ps1

Parameters:
- tenant_name
- client_id

Returns:

```json
{
  "TotalSiteCount": 1250
}
```

### get_sharepoint_sites_size

Purpose:
Returns the total storage size of all SharePoint Online site collections in GB.

Use this tool when the user asks:
- Total SharePoint storage size
- SharePoint tenant size
- SharePoint migration sizing
- SharePoint storage assessment
- SharePoint capacity analysis
- Total SharePoint data volume

Backend Script:
./scripts/get-sharepoint-sites-size.ps1

Parameters:
- tenant_name
- client_id

Returns:

```json
{
  "TotalSizeGB": 523.44
}
```