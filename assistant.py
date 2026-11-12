"""Generate a priority-ordered handoff from a local incident export."""
import argparse
import json
from pathlib import Path


def handoff(incidents):
    active = [incident for incident in incidents if incident["status"] != "resolved"]
    active.sort(key=lambda incident: (incident["priority"], incident["id"]))
    return [
        {
            "id": incident["id"],
            "priority": incident["priority"],
            "owner": incident.get("owner") or "unassigned",
        }
        for incident in active
    ]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    args = parser.parse_args()
    try:
        incidents = json.loads(args.input.read_text(encoding="utf-8"))
        print(json.dumps(handoff(incidents), indent=2))
    except (OSError, ValueError, TypeError, KeyError) as error:
        parser.error(str(error))


if __name__ == "__main__":
    main()
