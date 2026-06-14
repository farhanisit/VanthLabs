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

## Hands-On Session 02 — KQL Aggregation Functions
Source: Microsoft Learn — "Tutorial: Use aggregation functions"
Environment: dataexplorer.azure.com, help cluster, StormEvents table

### Operators & Functions Covered
count()              - count all rows
countif(condition)   - count rows where condition is true
avg()                - average of a column
min()                - minimum value
max()                - maximum value
sum()                - sum of a column
bin(col, interval)   - group values into time/size buckets
render barchart      - visualize as bar chart
render piechart      - visualize as pie chart
render timechart     - visualize as time series

### LESSON 4 — summarize without grouping = one bucket
countif(DamageCrops > 0)            -> returns 1491 (total across ALL states)
countif(DamageCrops > 0) by State   -> returns one row per state
RULE: no 'by' clause = entire table collapses into one row.

### LESSON 5 — count() vs sum() — critical distinction
count()        = how many EVENTS (rows) matched
sum(column)    = total VALUE across those rows
Changing the filter threshold (e.g. > 100 vs > 10M) affects count().
To measure actual damage: use sum(DamageCrops), not count().
On the job: this distinction causes dashboard misreads. Slow down and check.

### LESSON 6 — Adding columns to 'by' increases granularity
by State                        -> ~67 rows (one per state)
by State, bin(StartTime, 7d)    -> 218 rows (one per state per week)
Every column added to 'by' = more specific groups = more output rows.

### LESSON 7 — render changes the question, not the data
render barchart  -> "how many events happened?"
render piechart  -> "what share does each group represent?"
render timechart -> "how did this change over time?"
Same data. Same query. Different render = different analytical question.

### LESSON 8 — Anomaly detection instinct
Max = Min = Avg = same value -> only one record exists, OR all values identical.
This is a data quality / anomaly signal. Note it, investigate it.

### LESSON 9 — sort vs top
sort by X desc   -> organises all rows, no limit
top N by X       -> limits AND sorts in one step
sort by StartTime asc -> restores chronological order when dates look chaotic

### Key Pattern: Time-bucketed anomaly hunting
StormEvents
| where DamageCrops > 10099999
| summarize EventCount = count() by bin(StartTime, 7d)
| render timechart
Plain English: "During which weeks did extreme crop-damage storms cluster?"
This is your first real anomaly-hunting style query.

### SPL → KQL Bridge (aggregation layer)
| stats count by State       -> | summarize count() by State
| stats avg(X) by Y          -> | summarize avg(X) by Y
| timechart count            -> | summarize count() by bin(T,1h) | render timechart
| eval col = ...             -> | extend col = ...

## Session 04 — Aggregation Module Complete (11 June 2026)
Completed: make_set(), case(), bin(), sliding window concept

### make_set()
Creates array of unique values from grouped rows
StormEvents | where DeathsDirect > 0
| summarize StormTypesWithDeaths = make_set(EventType) by State
| sort by array_length(StormTypesWithDeaths)

### case()
Conditional bucketing — IF/ELSE IF/ELSE logic
extend InjuriesBucket = case(
    InjuriesCount > 50, "Large",
    InjuriesCount > 10, "Medium",
    InjuriesCount > 0,  "Small",
    "No injuries")

### Sliding Window vs Fixed Window
bin(TimeGenerated, 7d)  = fixed buckets (Week1, Week2, Week3)
sliding window          = rolling calculation (Days1-7, Days2-8, Days3-9)
SOC use: failed login trends, alert volume baselines, DNS activity spikes

### Key insight locked today
Changing the population changes the percentages.
Filter before summarize = different story than filter after summarize.
Temporary columns (from summarize) are available to all downstream operators.

### Lesson 16 operator checklist — COMPLETE
where, project, extend, sort, top, render
summarize, count(), countif(), sum(), avg(), min(), max()
make_set(), case(), bin(), toscalar(), todouble()
Sliding window (concept) — implementation next session

### Next: Lesson 16.1
Move off StormEvents tutorial data onto real Sentinel tables:
SecurityEvent, SigninLogs, DeviceEvents
Build actual threat hunting queries — brute force, account compromise

## Session 05 — Join Data from Multiple Tables (13 June 2026)
Source: Microsoft Learn — "Tutorial: Join data from multiple tables"

### Core concept
JOIN = combine two tables using a common column (matching key)
      to add context/data that the first table didn't have

Event table  = source of what happened (logs, telemetry)
Context table = source of extra information (user info, device info)
Matching key  = column that exists in BOTH tables

### join vs lookup
join   = full flexibility, multiple kinds (inner, left, right, anti)
lookup = simplified join, optimised for enriching a fact table
         with columns from a smaller context/dimension table
Use lookup when you just want to add context columns.
Use join when the table relationship is complex.

### SOC translation
SigninLogs | join EmployeeDirectory on UserPrincipalName
→ adds Department, Manager, Location to login events

DeviceEvents | join DeviceInfo on DeviceId  
→ adds OS, owner, risk level to endpoint events

FailedLogins | join UserDirectory on Username
→ adds Department to brute force investigation

### join kinds
kind=inner         = only rows that match in BOTH tables
kind=innerunique   = inner join, deduplicates right table matches
kind=leftouter     = all left rows, matching right rows (nulls if no match)
kind=anti          = rows in left that have NO match in right
                     (find users with no MFA registered, etc.)

### Notebook card
JOIN = attach context from Table B onto Table A using a shared column
lookup = simple enrichment join (fact table + dimension table)
join   = flexible multi-kind joining
Matching key = the column both tables share

## Session 06 — Real Security Detection Queries (14 June 2026)
Dataset: help.SecurityLogs (Azure Data Explorer)
Tables: AuthenticationEvents, ProcessEvents, FileCreationEvents,
        PassiveDns, Email, InboundBrowsing, OutboundBrowsing, Employees

### Detection Query 1 — Brute Force Detection
AuthenticationEvents
| where result == "Failed Login"
| summarize FailCount = count() by username
| where FailCount >= 5
| sort by FailCount desc
Result: 106 accounts with 5+ failed logins. jadenman top at 22.

### Detection Query 2 — Account Takeover (Failures + Successful Login)
let failures = AuthenticationEvents
| where result == "Failed Login"
| summarize FailedCount = count() by username
| where FailedCount >= 5;
let successes = AuthenticationEvents
| where result == "Successful Login"
| summarize SuccessCount = count() by username
| where SuccessCount >= 1;
failures
| join kind=inner successes on username
| project username, SuccessCount, FailedCount
| sort by FailedCount desc
Result: 97 accounts — failed logins AND at least one success.

### Analyst triage logic
Low success rate (jadenman 2/22 = 9%) = brute force/credential stuffing
High success rate = misconfigured app or legitimate user issue
Priority: low success rate + high failure count = investigate first

### Lessons locked this session
- case sensitivity burned again: "Failed login" vs "Failed Login"
- let = named sub-query, reusable in the same query
- join kind=inner = only usernames in BOTH tables survive
- ratio matters more than raw count in triage
- two where clauses in one query = filter rows THEN filter aggregated results
