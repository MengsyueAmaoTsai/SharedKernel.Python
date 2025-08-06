[CmdletBinding()]
param (
    [Parameter(Mandatory = $true, HelpMessage = "Revision number for the build version.")]
    [ValidateNotNullOrEmpty()]
    [ValidateRange(0, 9999)]
    [string]$Revision)

Write-Host "Generating build version ..."

$now = Get-Date
$version = "{0}.{1}.{2}.{3}" -f $now.ToString("yy"), $now.Month, $now.Day, $Revision

Write-Host "Generated build version: $version" -ForegroundColor Green
Write-Output $version
