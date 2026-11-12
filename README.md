# On-call Handoff Assistant

Build a priority-ordered handoff list from an exported incident list. Resolved incidents are omitted and missing owners are marked `unassigned`. Lower priority numbers appear first.

## Run

Save the following as `incidents.json`, then run `python3 assistant.py incidents.json`.

```json
[{"id":"INC-1","priority":1,"status":"open"},{"id":"INC-2","priority":2,"status":"resolved","owner":"Platform"}]
```

The result contains `INC-1`, priority `1`, and owner `unassigned`. The tool reads local JSON and makes no changes to incident records.
