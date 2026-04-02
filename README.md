# Python Pytest Test Project

A Python test project template using pytest.

## Project Structure

```
.
├── .gitignore
├── README.md
├── pytest.ini           # Pytest configuration
├── requirements.txt    # Dependencies
├── config/             # Configuration files
│   └── __init__.py
├── core/               # Core business logic
│   └── __init__.py
├── data/               # Data files / test data
│   └── __init__.py
├── src/                # Source code
│   ├── __init__.py
│   └── calculator.py
├── testcases/          # All test cases
│   ├── __init__.py
│   ├── conftest.py     # Pytest fixtures
│   ├── unit/           # Unit tests
│   └── integration/    # Integration tests
└── utils/              # Utility functions / helpers
    └── __init__.py
```

**Directory Purposes:**
- `config/` - Configuration settings, environment configs
- `core/` - Core business logic and main functionality
- `data/` - Test data files, datasets
- `src/` - Source code / main modules
- `testcases/` - All test cases (unit, integration, etc.)
- `utils/` - Helper functions, common utilities

## Setup

### 1. Create and activate virtual environment

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

## Running Tests

Run all tests:
```bash
pytest
```

Run with coverage:
```bash
pytest --cov=src
```

Run only unit tests:
```bash
pytest -m unit
```

Run only integration tests:
```bash
pytest -m integration
```

Run with verbose output:
```bash
pytest -v
```

## Writing Tests

- Place unit tests in `testcases/unit/`
- Place integration tests in `testcases/integration/`
- Follow naming convention: `test_*.py` for test files
- Use `test_*` prefix for test functions
- Add fixtures in `testcases/conftest.py`

## Example Test

Create `testcases/unit/test_example.py`:

```python
def test_example():
    assert 1 + 1 == 2
```

## Code Quality

Check with flake8:
```bash
flake8 src/ testcases/ config/ core/ data/ utils/
```

Format with black:
```bash
black src/ testcases/ config/ core/ data/ utils/
```

## 常用 Git 命令

```bash
# 查看状态
git status

# 查看提交历史
git log --oneline

# 添加文件到暂存区
git add <file>
git add .                  # 添加所有修改

# 提交代码
git commit -m "commit message"

# 拉取远程最新代码
git pull origin main

# 推送本地提交到远程
git push origin main

# 创建新分支
git checkout -b <branch-name>

# 切换分支
git checkout <branch-name>

# 查看所有分支
git branch

# 合并分支到当前分支
git merge <branch-name>
```
