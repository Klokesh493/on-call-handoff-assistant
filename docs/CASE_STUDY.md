# On Call Handoff Assistant walkthrough

## Business problem

Shift transitions can lose unresolved incidents or ownership information. The incoming responder needs an ordered handoff with unassigned work called out.

## Reproduce the workflow

Run `python3 assistant.py example.json` from the repository root. Then run `make verify` to repeat the local checks.

Observed sample output

```text
[
  {
    "id": "INC-1",
    "priority": 1,
    "owner": "unassigned"
  }
]
```

The sample supplies these fields. `id`, `priority`, `status`.

## Verification

Sample command and local checks passed.

## Limitations

The documented run evaluates the bundled sample locally. Results depend on the quality and scope of the input. The demo makes no live infrastructure changes.
