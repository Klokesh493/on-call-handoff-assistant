PYTHON ?= python3

.PHONY: verify
verify:
	$(PYTHON) -B -m unittest discover -v
	$(PYTHON) assistant.py example.json

.PHONY: replay
replay:
	$(PYTHON) tools/replay_examples.py --report reports/replay.md
