# In-Memory Python Console Todo Application

A command-line interface (CLI) todo application built with Python that allows users to manage tasks in memory. This project demonstrates spec-driven development using the Spec-Kit Plus framework and Claude Code.

## 📋 Features

- ✅ Add tasks with auto-incremented IDs
- ✅ View all tasks with detailed information
- ✅ Update task titles and descriptions
- ✅ Delete tasks with confirmation
- ✅ Mark tasks as complete/incomplete
- ✅ Colorful console interface with emojis
- ✅ Task completion timestamps
- ✅ Input validation and error handling

## 🛠️ Tech Stack

- **Language**: Python 3.13+
- **Architecture**: Model-Manager-UI pattern
- **Dependencies**: Managed with UV package manager (colorama, plotext)
- **Development**: Spec-driven development with Claude Code

## 🚀 Setup Instructions

### Prerequisites

- Python 3.13+ installed on your system
- UV package manager for dependency management (required)

### Installation

1. Clone or download the repository to your local machine
2. Navigate to the project directory:
   ```bash
   cd todo-console
   ```

3. Install dependencies using UV package manager:
   ```bash
   uv sync
   ```

4. Run the application:
   ```bash
   uv run python src/main.py
   ```

## 🎯 Usage

Run the application using UV:

```bash
uv run python src/main.py
```

The application will start and display a menu with the following options:
1. Add Task
2. View Tasks
3. Update Task
4. Delete Task
5. Mark Task Complete
6. Mark Task Incomplete
7. Exit

### Basic Operations

#### Adding a Task
- Select "Add Task" from the menu
- Enter the task title when prompted
- Optionally enter a description
- The system will assign an auto-incremented ID

#### Viewing Tasks
- Select "View Tasks" from the menu
- All tasks will be displayed with their ID, title, description, and completion status
- Tasks are shown in a formatted table with color coding

#### Updating a Task
- Select "Update Task" from the menu
- Enter the task ID when prompted
- Enter the new title and/or description

#### Deleting a Task
- Select "Delete Task" from the menu
- Enter the task ID when prompted
- Confirm the deletion

#### Marking Task Complete/Incomplete
- Select "Mark Task Complete" or "Mark Task Incomplete"
- Enter the task ID when prompted

## 🏗️ Architecture

The application follows a clean **Model-Manager-UI** architectural pattern:

- **Models** (`src/models/task.py`): Data structures and validation
- **Managers** (`src/managers/todo_manager.py`): Business logic and in-memory data operations
- **UI** (`src/ui/console.py`): Presentation layer and user interaction

## 🧪 Testing

The project includes comprehensive tests in the `tests/` directory covering:
- Individual functionality tests
- End-to-end tests
- Integration tests

To run tests, use your preferred Python test runner:
```bash
python -m pytest tests/
```

## ⚠️ Limitations

- **In-Memory Storage**: All data is stored in memory only and will be lost when the application closes
- **Single User**: No user authentication or multi-user support
- **No Advanced Features**: No priorities, deadlines, tags, or external integrations

## 📁 Project Structure

```
src/
├── main.py                 # Application entry point
├── models/
│   └── task.py             # Task data model
├── managers/
│   └── todo_manager.py     # Business logic layer
└── ui/
    └── console.py          # Console UI layer
tests/                      # Test files
specs/                      # Specification files
history/                    # Prompt History Records
```

## 🤝 Contributing

This project was developed following the agentic dev stack workflow:
1. Specification (`spec.md`) - requirements and user stories
2. Implementation plan (`plan.md`) - architectural decisions
3. Tasks (`tasks.md`) - testable implementation steps
4. Implementation - following the mandatory folder structure

## 📄 License

This project is open source and available under the MIT License.

##  Acknowledgments

- Built with Claude Code and the Spec-Kit Plus framework
- Following spec-driven development methodology
- Designed for the todo app hackathon