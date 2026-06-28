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

Recommended:

```bash
pipx install vibetype
```

or using uv:

```bash
uv tool install vibetype
```

Alternatively, install it with pip:

```bash
pip install vibetype
```

## Run

```bash
vibetype
```

## Future Ideas

- Custom sentence packs
- Import/export custom csvs of sentence packs
