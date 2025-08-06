[CmdletBinding()]
param (
    [Parameter(Mandatory = $true, HelpMessage = "Path to the pyproject.toml file to update.")]
    [ValidateNotNullOrEmpty()]
    [string]$ProjectPath,

    [Parameter(Mandatory = $true, HelpMessage = "Version string to update in pyproject.toml.")]
    [ValidateNotNullOrEmpty()]
    [string]$Version
)

$pyproject = Get-Content -Path $ProjectPath 
$pyproject = $pyproject -replace 'version = ".*"', "version = ""$(Version)"""
$pyproject | Set-Content -Path $ProjectPath

Write-Host "Updated version to: $Version" -ForegroundColor Green