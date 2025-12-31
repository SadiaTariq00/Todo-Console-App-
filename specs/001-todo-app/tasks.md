# Tasks: In-Memory Python Console Todo Application

**Feature**: 001-todo-app
**Branch**: 001-todo-app
**Created**: 2025-12-30
**Based on**: specs/001-todo-app/spec.md, specs/001-todo-app/plan.md

## Implementation Strategy

Build the application following the Model-Manager-UI architectural pattern with clear separation of concerns. Implement in priority order: User Story 1 (Add Task) as MVP, then remaining stories incrementally. Each user story should be independently testable.

## Dependencies

- User Story 2 (View Task List) requires User Story 1 (Add Task) to test properly
- User Stories 3, 4, 5 require User Story 1 to create tasks for testing

## Parallel Execution Examples

- Task model creation can run in parallel with manager class setup
- UI menu implementation can run in parallel with business logic implementation
- Different user story phases can be developed sequentially but tested independently

---

## Phase 1: Setup

Initialize project structure and basic configuration.

- [X] T001 Create src directory structure: models/, managers/, ui/
- [X] T002 Create main.py entry point file
- [X] T003 Create models/task.py file
- [X] T004 Create managers/todo_manager.py file
- [X] T005 Create ui/console.py file

---

## Phase 2: Foundational Components

Build core components that all user stories depend on.

- [X] T006 [P] Implement Task data model in src/models/task.py with id, title, description, completed fields
- [X] T007 [P] Implement TodoManager class in src/managers/todo_manager.py with in-memory storage
- [X] T008 [P] Initialize task ID counter in TodoManager to start from 1
- [X] T009 [P] Implement basic console interface in src/ui/console.py with main menu

---

## Phase 3: User Story 1 - Add New Task (Priority: P1)

A user wants to add a new task to their todo list by entering the task title and description in the console application. The system should generate an auto-incremented ID and mark the task as incomplete by default.

**Independent Test**: Can be fully tested by running the application and executing the add task command with a title and description. Delivers the core value of creating tasks that can be managed.

- [X] T010 [US1] Implement create_task method in TodoManager with auto-incremented ID generation
- [X] T011 [US1] Add validation to ensure title is not empty in Task model
- [X] T012 [US1] Implement add_task function in ConsoleUI to get user input
- [X] T013 [US1] Add menu option to call add_task functionality
- [X] T014 [US1] Test adding a task with title and description works correctly

---

## Phase 4: User Story 2 - View Task List (Priority: P1)

A user wants to see all tasks in their todo list with details including ID, title, description, and completion status. This allows them to understand their current tasks and plan their work.

**Independent Test**: Can be fully tested by adding a few tasks and then executing the view task list command. Delivers the core value of allowing users to see their tasks.

- [X] T015 [US2] Implement get_all_tasks method in TodoManager
- [X] T016 [US2] Implement display_tasks function in ConsoleUI to show all tasks
- [X] T017 [US2] Add menu option to call view tasks functionality
- [X] T018 [US2] Format task display with ID, title, description, and completion status
- [X] T019 [US2] Handle case when no tasks exist with appropriate message
- [X] T020 [US2] Test viewing task list after adding multiple tasks

---

## Phase 5: User Story 3 - Mark Task as Complete/Incomplete (Priority: P1)

A user wants to update the status of a task from incomplete to complete when finished, or from complete back to incomplete if the status was marked incorrectly.

**Independent Test**: Can be fully tested by adding a task, then marking it as complete, then viewing the task list to verify the status change. Delivers the core value of allowing users to track task completion.

- [X] T021 [US3] Implement mark_task_complete method in TodoManager
- [X] T022 [US3] Implement mark_task_incomplete method in TodoManager
- [X] T023 [US3] Implement get_task_by_id method in TodoManager for validation
- [X] T024 [US3] Implement mark_task_status function in ConsoleUI to get task ID and status
- [X] T025 [US3] Add menu options to mark tasks as complete/incomplete
- [X] T026 [US3] Test marking tasks as complete and incomplete works correctly
- [X] T027 [US3] Test error handling for invalid task IDs

---

## Phase 6: User Story 4 - Update Task Details (Priority: P2)

A user wants to modify the title or description of an existing task when their plans change or when they need to add more details.

**Independent Test**: Can be fully tested by adding a task, updating its details, then viewing the task to verify the changes. Delivers the value of allowing users to refine their tasks.

- [X] T028 [US4] Implement update_task method in TodoManager
- [X] T029 [US4] Implement update_task function in ConsoleUI to get task ID and new details
- [X] T030 [US4] Add menu option to call update task functionality
- [X] T031 [US4] Test updating task title and description works correctly
- [X] T032 [US4] Test error handling for invalid task IDs during update
- [X] T033 [US4] Validate updated title is not empty

---

## Phase 7: User Story 5 - Delete Task (Priority: P2)

A user wants to remove completed or irrelevant tasks from their todo list to keep the list clean and focused on current priorities.

**Independent Test**: Can be fully tested by adding a task, then deleting it, then viewing the task list to verify the task is removed. Delivers the value of allowing users to manage their task list.

- [X] T034 [US5] Implement delete_task method in TodoManager
- [X] T035 [US5] Implement delete_task function in ConsoleUI to get task ID
- [X] T036 [US5] Add menu option to call delete task functionality
- [X] T037 [US5] Test deleting tasks works correctly
- [X] T038 [US5] Test error handling for invalid task IDs during deletion
- [X] T039 [US5] Verify task ID counter doesn't reset after deletion

---

## Phase 8: Polish & Cross-Cutting Concerns

Final integration, error handling, and validation across all components.

- [X] T040 Implement comprehensive error handling for all user inputs
- [X] T041 Add input validation for all user-facing functions
- [X] T042 Test all menu navigation and user flows
- [X] T043 Handle edge cases like very long titles/descriptions
- [X] T044 Test application with empty task list for all operations
- [X] T045 Verify in-memory storage works throughout application session
- [X] T046 Ensure application doesn't crash under invalid inputs
- [X] T047 Test all user stories together in sequence
- [X] T048 Verify all functional requirements from spec are met
- [X] T049 Run complete end-to-end test of all features
- [X] T050 Document any remaining edge cases and their handling