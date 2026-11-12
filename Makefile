PYTHON ?= python3

.PHONY: verify
verify:
	$(PYTHON) assistant.py example.json
