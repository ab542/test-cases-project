# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

### Setup
```bash
# Activate virtual environment (Windows)
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Running Tests
```bash
# Run all tests
pytest

# Run all tests with verbose output
pytest -v

# Run a single test file
pytest testcases/unit/test_calculator.py

# Run a single test
pytest testcases/unit/test_calculator.py::TestCalculator::test_add

# Run only unit tests
pytest -m unit

# Run only integration tests
pytest -m integration

# Run with coverage report
pytest --cov=src
```

### Code Quality
```bash
# Check with flake8
flake8 src/ testcases/ config/ core/ data/ utils/

# Format with black
black src/ testcases/ config/ core/ data/ utils/
```

### Git
```bash
git status
git add <file>
git commit -m "message"
git pull origin main
git push origin main
```

## Project Structure

```
.
├── config/          # Configuration files
├── core/            # Core business logic
├── data/            # Raw data, PRD documents, PDF -> md extracted content
├── docs/            # Analysis documents, requirements analysis
├── src/             # Source code modules
├── testcases/       # All test cases (pytest tests + test case docs)
│   ├── unit/          # Unit tests
│   ├── integration/   # Integration tests
│   └── conftest.py    # Pytest fixtures configuration
└── utils/            # Utility functions and helpers
```

## Key Files

- `pytest.ini` - Pytest configuration with markers (unit, integration, smoke, regression)
- `requirements.txt` - Project dependencies (pytest, pytest-cov, flake8, black, PyPDF2)
- `README.md` - Project setup instructions + common Git commands
- `docs/requirements-analysis.md` - Requirements analysis for "组织架构" feature: core functions, business rules, constraints, high-risk modules, test scope
- `testcases/organization-architecture-test-cases.md` - Generated comprehensive test cases for organization architecture feature

## Current Project Context

This is a test case management project based on Python + pytest. It stores:
1. PRD/requirement documents in `data/`
2. Requirements analysis in `docs/`
3. Generated structured test cases in `testcases/`
4. Example Python code with corresponding pytest tests

When adding new features:
- Follow existing directory structure
- Keep test cases in `testcases/` with proper marker (`@pytest.mark.unit`, `@pytest.mark.integration`)
- Add requirements analysis to `docs/`
