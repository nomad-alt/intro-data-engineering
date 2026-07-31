# Day 2: Control Flow

## What control flow is
Control flow describes the order in which Python executes statements in a program. It is how the program decides whether to run certain blocks of code, repeat tasks, or choose between alternatives. Control flow is managed with statements like `if`, `elif`, `else`, `for`, and `while`.

## What loops are
Loops are control flow structures that repeat a sequence of statements until a condition changes. In Python, `for` loops iterate over items in a collection, while `while` loops continue running as long as a condition is true. Loops help automate repeated work without writing the same code multiple times.

## Why functions improve code reuse
Functions let you package a block of code under one name and call it whenever needed. This makes code easier to read, easier to test, and easier to maintain. When the same logic is needed in several places, a function keeps the code from being duplicated and helps avoid mistakes.

## What you built today
Today I built examples for control flow and reusable logic. I wrote comparisons with `==`, `!=`, `>`, and `>=`, and used boolean variables to decide if data was ready to process. I also created a function that filters sales values with a threshold by using a list comprehension.

## Challenges you encountered
The biggest challenge was understanding how Python finds modules during testing. The test import `from src.functions import square` failed until I ran `pytest` from the correct folder or set `PYTHONPATH` so `src` became importable. Another challenge was making sure condition logic matched the validation checks I wanted.

## Key takeaways
- Control flow determines whether code runs, and loops let code repeat automatically.
- Functions make code reusable and reduce duplication.
- Proper testing setup is important so imports resolve correctly.
- Boolean values such as `True` and `False` are useful for tracking validation and processing state.