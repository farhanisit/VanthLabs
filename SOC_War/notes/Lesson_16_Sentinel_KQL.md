# SOC Lesson 16 — Microsoft Sentinel & KQL
Date: 03-06-2026

## Why Sentinel
- Cloud-native SIEM + SOAR built on Azure
- European/German enterprise standard
- Same detection logic as Splunk, different syntax
- Splunk = SIEM only | Sentinel = SIEM + SOAR

## KQL Core Structure
TableName
| operator1
| operator2
| operator3

## SPL → KQL Bridge
| SPL                        | KQL                              |
|----------------------------|----------------------------------|
| index=main *               | SecurityEvent                    |
| index=main status=failed   | SecurityEvent | where EventID==4625|
| stats count                | summarize count()                |
| stats count by user        | summarize count() by Account     |
| earliest=-24h              | where TimeGenerated > ago(24h)   |
| head 10                    | take 10                          |
| sort -count                | order by count_ desc             |
| table user, src, action    | project Account, IpAddress, Activity|

## KQL Operators
- where     = filter rows
- summarize = aggregate/count
- project   = select columns
- order by  = sort (desc/asc)
- ago()     = time window (1h, 24h, 7d)
- let       = create variable/sub-query
- join      = combine two result sets

## Key Sentinel Tables
| Table                | Contains                          |
|----------------------|-----------------------------------|
| SecurityEvent        | Windows Security Event Log        |
| Syslog               | Linux syslog                      |
| SigninLogs           | Azure AD login events             |
| AzureActivity        | Azure resource changes            |
| DeviceProcessEvents  | Endpoint process telemetry        |
| DeviceNetworkEvents  | Endpoint network connections      |
| DeviceLogonEvents    | Endpoint logon events             |
| CommonSecurityLog    | Firewall/network device logs      |

## Detection Queries

### Query 1 — Brute Force
SecurityEvent
| where EventID == 4625
| where TimeGenerated > ago(1h)
| summarize FailCount = count() by Account, IpAddress
| where FailCount >= 5
| order by FailCount desc

### Query 2 — Account Takeover (Failures + Success)
let failures = SecurityEvent
| where EventID == 4625
| where TimeGenerated > ago(1h)
| summarize FailCount = count() by Account;
SecurityEvent
| where EventID == 4624
| where TimeGenerated > ago(1h)
| join kind=inner failures on Account
| where FailCount >= 5
| project TimeGenerated, Account, IpAddress, FailCount

### Query 3 — New User Created (Persistence)
SecurityEvent
| where EventID == 4720
| where TimeGenerated > ago(24h)
| project TimeGenerated, Account, SubjectAccount,
          SubjectDomainName, Activity

### Query 4 — Privilege Escalation
SecurityEvent
| where EventID == 4732
| where TimeGenerated > ago(24h)
| project TimeGenerated, Account, MemberName,
          GroupName, Activity

### Query 5 — Lateral Movement (Network Logon)
SecurityEvent
| where EventID == 4624
| where LogonType == 3
| where TimeGenerated > ago(1h)
| summarize count() by Account, IpAddress, WorkstationName
| order by count_ desc

## Azure Setup Steps
1. portal.azure.com → Start Free ($200 credit)
2. Create Log Analytics Workspace
   - Resource group: VanthSOC
   - Workspace name: vanth-sentinel-lab
   - Region: West Europe
3. Enable Microsoft Sentinel on that workspace
4. Data connectors → Windows Security Events via AMA

## Hands-On Session 01 — KQL Common Operators
Source: Microsoft Learn — "Tutorial: Learn common operators"
URL: learn.microsoft.com/kusto/query/tutorials/learn-common-operators
Environment: dataexplorer.azure.com, help cluster, StormEvents table (free, public)

### Operators worked through this session
count                - count rows in a table
take N               - return N arbitrary rows (preview data shape)
project              - SELECT a subset of columns (and rename/calculate)
distinct <col>       - list unique values in a column
where                - filter rows by condition
between (a .. b)     - filter by date/time range
sort by <col>        - sort rows (default desc; asc for ascending)
top N by <col>       - first N rows sorted by column
extend <new> = ...   - ADD a calculated column to the end of the table

### LESSON 1 — String comparison is CASE-SENSITIVE
==  is case-sensitive:  'Texas' != 'TEXAS' -> ZERO rows, no error
=~  is case-insensitive: 'texas' =~ 'TEXAS' -> matches
RULE: for strings, default to =~ unless casing is known.
#1 cause of "query ran fine but returned nothing."

### LESSON 2 — project vs extend (Microsoft's own framing)
project = SELECT only the columns you want to view
extend  = ADD a calculated column to the END of the full table
Without project, ALL columns return by default.
(The docs' extend output uses "..." to collapse the middle columns
 for page-fit — the data still has every column. Same result as mine.)

Example (project — clean view):
  StormEvents
  | where State == 'TEXAS' and EventType == 'Flood'
  | top 5 by DamageProperty desc
  | project StartTime, EndTime, Duration = EndTime - StartTime, DamageProperty

Example (extend — full table + new col):
  StormEvents
  | where State == 'TEXAS' and EventType == 'Flood'
  | top 5 by DamageProperty desc
  | extend Duration = EndTime - StartTime

### LESSON 3 — Operator order matters
KQL transforms data in sequence. 'top' before 'where' gives a
different result than 'where' before 'top'. Filter first, then top.

### Next session
Continue series: "Use aggregation functions" (summarize, count(), avg, etc.)
Then map each KQL operator to its Splunk SPL equivalent.
