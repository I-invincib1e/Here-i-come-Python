# Requires GitHub CLI: https://cli.github.com/
# Run: pwsh ./scripts/create_issues.ps1 -Repo "owner/repo"
param(
  [Parameter(Mandatory=$true)] [string] $Repo
)

# Load issues from JSON configuration
$configPath = Join-Path $PSScriptRoot "issues_config.json"
$issues = Get-Content $configPath | ConvertFrom-Json

foreach ($issue in $issues.issues) {
  gh issue create --repo $Repo --title $issue.title --label $issue.labels --body $issue.body
}
