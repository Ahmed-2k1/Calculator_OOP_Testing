# Python OOP Calculator

This project is a Python-based calculator that follows object-oriented programming principles, aiming to demonstrate key concepts like SOLID, DRY, GRASP, and Separation of Concerns. The calculator supports basic arithmetic operations—addition, subtraction, multiplication, and division—while also storing a history of calculations.

## Features
- Perform basic arithmetic: Add, Subtract, Multiply, Divide.
- Exception handling for division by zero.
- Stores calculation history for easy retrieval.
- Follows best practices for OOP, including static methods, class methods, and instance methods.
- 100% test coverage with `pytest` and parameterized testing.

## Installation
1. Clone the repository:
   ```bash
   git clone 
   cd Calculator_OOP_Testing
  
## Running the commands
2. python -m venv venv
source venv/bin/activate  

3. pip install -r requirements.txt

# Command for testing:
4. pytest
5. pytest --cov=calculator --cov-report=term-missing
6. pytest --cov=calculator --cov-report=html

7. pylint calculator.py calculation.py history.py




