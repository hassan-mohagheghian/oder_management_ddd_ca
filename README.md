# Order Management App

## Overview

This is a simple order management Python project following **Clean Architecture** and **DDD** principles.

## Project Structure

```bash
root/
├── src/
│    ├── order_app/
│    │   ├── domain/
│    │   │   ├─── entities/ --> entities and their related value objects
│    │   │   └─── value_objects --> common value objects
│    │   └── application/
│    │       └─── use_cases/
│    └── main.py --> order app
└── tests/ --> test with similar folder structure to src folder
```

## Setup / Installation (Local)

1. clone the repository

```bash
git clone https://github.com/hassan-mohagheghian/oder_management_ddd_ca
cd oder_management_ddd_ca
```

1. Create a virtual environment in the root folder

```bash
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
```

1. Use PYTHONPATH

```bash
export PYTHONPATH="${PYTHONPATH}:$(pwd)/src"  # Linux/macOS
```

## Install dependencies

```bash
pip install -r requirements.txt
```

## Running the Application

```bash
python -m src.main
```

## Running Tests

```bash
pytest
```
