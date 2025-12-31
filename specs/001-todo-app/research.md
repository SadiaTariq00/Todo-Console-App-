# Research: In-Memory Python Console Todo Application

**Feature**: 001-todo-app
**Date**: 2025-12-30

## Decision Log

### Decision: Auto-increment task ID generation approach
**Rationale**: Using a simple counter that increments with each new task is the most straightforward approach for in-memory storage. The counter will be maintained in the TodoManager class and will start from 1, incrementing for each new task created.

**Alternatives considered**:
- Using UUIDs: Would be overkill for a simple console application and doesn't provide any benefit
- Using current timestamp: Could cause issues with rapid task creation and doesn't provide sequential IDs as expected

### Decision: Internal data structure for task storage
**Rationale**: Using a Python dictionary with task IDs as keys provides O(1) lookup time for retrieving, updating, or deleting tasks by ID. This is efficient for the expected use case and allows for easy management of tasks.

**Alternatives considered**:
- List/array: Would require O(n) search time to find tasks by ID
- Set: Doesn't allow for key-value mapping needed to access tasks by ID

### Decision: Responsibility boundaries between UI, manager, and model layers
**Rationale**: Following clean architecture principles:
- Models (task.py): Define the data structure and basic validation
- Managers (todo_manager.py): Handle business logic, data operations, and maintain state
- UI (console.py): Handle user input/output and delegate operations to managers

**Alternatives considered**:
- Combining layers: Would violate separation of concerns and make testing difficult

## Technical Research Findings

### Python 3.13+ Features
- Using standard Python 3.x features that are compatible with 3.13+
- No special 3.13+ features required for this simple application
- Standard library modules: `dataclasses` for model definition, basic I/O for console interaction

### In-Memory Storage Implementation
- Using a class attribute in TodoManager to store tasks
- Dictionary for O(1) access by task ID
- Instance variables to maintain application state during runtime
- No persistence across program restarts as required by constraints

### Console UI Design
- Using Python's built-in `input()` function for user interaction
- Print statements for displaying information
- Simple menu-based interface for task operations
- Error handling for invalid inputs and task IDs

## Architecture Patterns

### Model-Manager-UI Pattern
- Models define data structures and basic validation
- Managers handle business logic and data operations
- UI handles presentation and user interaction
- Clear separation of concerns for maintainability

### Single Responsibility Principle
- Each class has a single, well-defined purpose
- Task class manages task data
- TodoManager handles all task-related operations
- ConsoleUI manages user interaction
- Main function orchestrates the application flow