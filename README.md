# Smscr

This project provides a minimal interface to query the Trafikverket API.

## Installation

Create a virtual environment and install dependencies:

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Usage

The library exposes a helper function `get_train_announcements` which
retrieves train announcements from the Trafikverket API:

```python
from trafikverket import get_train_announcements

# Replace with your Trafikverket API key
announcements = get_train_announcements("YOUR_API_KEY", limit=5)
print(announcements)
```

## Running Tests

Tests rely on `pytest` and use mocked HTTP responses. To execute the test suite:

```bash
pytest
```

Ensure dependencies are installed as described above.
