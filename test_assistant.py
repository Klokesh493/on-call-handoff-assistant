import unittest

from assistant import handoff


class HandoffTest(unittest.TestCase):
    def test_orders_open_incidents_and_marks_missing_owner(self):
        incidents = [
            {"id": "INC-3", "priority": 2, "status": "open", "owner": "Platform"},
            {"id": "INC-2", "priority": 1, "status": "resolved"},
            {"id": "INC-1", "priority": 1, "status": "open"},
        ]
        self.assertEqual(handoff(incidents), [
            {"id": "INC-1", "priority": 1, "owner": "unassigned"},
            {"id": "INC-3", "priority": 2, "owner": "Platform"},
        ])
