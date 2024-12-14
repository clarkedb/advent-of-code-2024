init_day:
	@mkdir -p src/$(day)
	@if [ ! -f src/$(day)/__init__.py ]; then \
		echo "from typing import TextIO" > src/$(day)/__init__.py; \
		echo "" >> src/$(day)/__init__.py; \
		echo "def part1(input: TextIO) -> str:" >> src/$(day)/__init__.py; \
		echo "    raise NotImplementedError(\"day $(day) part 1 not implemented\")" >> src/$(day)/__init__.py; \
		echo "" >> src/$(day)/__init__.py; \
		echo "def part2(input: TextIO) -> str:" >> src/$(day)/__init__.py; \
		echo "    raise NotImplementedError(\"day $(day) part 2 not implemented\")" >> src/$(day)/__init__.py; \
		printf "Created src/$(day)/__init__.py\\n"; \
	else \
		printf "File src/$(day)/__init__.py already exists\\n"; \
	fi
