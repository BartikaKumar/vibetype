# VibeType

An offline, keyboard-first typing application built with Python and Textual.

VibeType is designed as a distraction-free space to type for fun, improve speed, and optionally learn through themed sentence packs.

## Features

### Typing Modes

- Random word practice
- Themed sentence packs
  - DSA
  - Pokémon
  - Anime Quotes

### Statistics

- Persistent local statistics
- Category-wise filtering
- Stores WPM, Raw WPM and Accuracy
- Average and maximum values
  - All-time
  - Latest 10 tests

### Philosophy

- Offline first
- Keyboard-first interface
- No accounts
- No telemetry

## Tech Stack

- Python
- Textual
- Rich
- SQLite

## Installation

Clone the repository:

```bash
git clone https://github.com/BartikaKumar/vibetype.git
cd vibetype
```

### Using uv

```bash
uv sync
uv run vibetype
```

### Using pip

(venv optional but recommended)

```bash
python3 -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
```

Install and run:

```bash
pip install .
vibetype
```

Alternatively, without installing the package:

```bash
pip install -r requirements.txt
python3 -m vibetype
```

## Future Ideas

- Custom sentence packs
- Import/export custom csvs of sentence packs