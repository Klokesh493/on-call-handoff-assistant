# On Call Handoff Assistant architecture

Build a priority-ordered handoff list from an exported incident list. Resolved incidents are omitted and missing owners are marked `unassigned`. Lower priority numbers appear first.

```mermaid
flowchart LR
    N0["example.json"]
    N1["assistant.py"]
    N2["Exclude resolved incidents, sort active incidents by priority, and flag missing ownership."]
    N3["Result for operator review"]
    N0 --> N1 --> N2 --> N3
```

## Operational boundaries

The documented run evaluates the bundled sample locally. Results depend on the quality and scope of the input. The demo makes no live infrastructure changes.
