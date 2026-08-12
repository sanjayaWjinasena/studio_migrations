# studio_migrations

Landing zone for `x_studio_*` field ports that don't have a proper
domain module yet.

## What this is

Odoo Studio-created fields need Python declarations for a fresh install
to work on a clean DB. As the BugFix-* modules were built up
(BugFix-Sales, BugFix-Purchase, BugFix-Analytics) and Fix-repair
absorbed the helpdesk-repair workflow, many Studio-owned fields moved
into those repos.

But some Studio fields live on models whose domain doesn't yet have a
dedicated BugFix-* repo — for example accounting fields, HR fields, and
scattered singletons. Those go here, one branch per cluster, until the
proper domain repo exists.

## Branches

| Branch | Cluster | Migration target |
|---|---|---|
| `main` | README only | — |
| `repair-related` | Studio fields on stock / product / project models Fix-repair touches | Will move to a future BugFix-Stock / BugFix-Product repo |

## Migration lifecycle

1. Field lives in Studio (`state=manual`, `modules=studio_customization`)
2. Field ported to a branch here → Python declaration, `state=base`
3. Later: proper domain repo created (e.g. `BugFix-Accounting`)
4. Field moved to the domain repo; removed from this repo
5. When a branch is empty, the branch is deleted
