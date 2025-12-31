# Quickstart Guide: In-Memory Python Console Todo Application

**Feature**: 001-todo-app
**Date**: 2025-12-30

## Project Setup

### Prerequisites
- Python 3.13+ installed
- UV package manager installed

### Environment Setup
1. Create a new project directory
2. Initialize the project structure with the required directories:
   ```
   src/
   ├── main.py
   ├── models/
   │   └── task.py
   ├── managers/
   │   └── todo_manager.py
   └── ui/
       └── console.py
   ```

### Dependency Management
1. Initialize UV in the project directory:
   ```
   uv init
   ```
2. No additional dependencies required beyond Python standard library for this application

## Running the Application

### Direct Execution
1. Navigate to the project root directory
2. Run the application:
   ```
   python src/main.py
   ```

### Expected Output
- The application will start and display a menu of available operations
- Users can add, view, update, delete, and mark tasks as complete/incomplete
- All data is stored in-memory only and will be lost when the application closes

## Basic Operations

### Adding a Task
1. Select the "Add Task" option from the menu
2. Enter the task title when prompted
3. Optionally enter a description
4. The system will assign an auto-incremented ID

### Viewing Tasks
1. Select the "View Tasks" option from the menu
2. All tasks will be displayed with their ID, title, description, and completion status

### Updating a Task
1. Select the "Update Task" option from the menu
2. Enter the task ID when prompted
3. Enter the new title and/or description

### Deleting a Task
1. Select the "Delete Task" option from the menu
2. Enter the task ID when prompted
3. Confirm the deletion

### Marking Task Complete/Incomplete
1. Select the "Mark Task Complete" or "Mark Task Incomplete" option
2. Enter the task ID when prompted

## Testing the Application

### Manual Testing
1. Add multiple tasks with different titles and descriptions
2. Verify that task IDs are auto-incremented correctly
3. Test viewing the task list
4. Update a task and verify the changes
5. Mark tasks as complete and incomplete
6. Delete tasks and verify they are removed
7. Test error handling for invalid task IDs

### Expected Behavior
- All operations should complete without errors
- Task data should be maintained correctly in-memory
- Invalid inputs should be handled gracefully with appropriate error messages
- The application should not crash under normal usage