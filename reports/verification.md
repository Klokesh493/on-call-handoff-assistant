# Local verification

Command: `make verify`

Result: **PASS**

````text
python3 -B -m unittest discover -v
python3 assistant.py example.json
[
  {
    "id": "INC-1",
    "priority": 1,
    "owner": "unassigned"
  }
]
test_orders_open_incidents_and_marks_missing_owner (test_assistant.HandoffTest) ... ok

----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
````
