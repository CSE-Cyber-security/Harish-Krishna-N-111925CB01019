# Harish-Krishna-N-111925CB01019
# Simple Calculator

A small command-line calculator written in Python.

## Features

- Addition, subtraction, multiplication and division
- Handles invalid input and division by zero
- Runs in a loop until you quit

## Requirements

- Python 3.6 or newer (no external packages)

## Usage

```bash
python calculator.py
```

Example session:

```
Simple Calculator
Operator (+, -, *, /) or q to quit: +
First number: 12
Second number: 8
12 + 8 = 20
```

Type `q` at the operator prompt to exit.

## Output

Basic operations:

![Basic operations](screenshots/screenshot1_basic_operations.png)

Error handling (division by zero, unknown operator, invalid input):

![Error handling](screenshots/screenshot2_error_handling.png)

## Project Structure

```
.
├── calculator.py
├── README.md
└── screenshots/
    ├── screenshot1_basic_operations.png
    └── screenshot2_error_handling.png
```

## License

MIT
