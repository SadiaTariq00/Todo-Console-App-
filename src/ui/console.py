"""
Console UI for the In-Memory Python Console Todo Application.

This module handles presentation and user interaction.
"""

from managers.todo_manager import TodoManager
from models.task import Task
import sys

# Import plotext for chart visualization (optional dependency)
try:
    import plotext as plt
except ImportError:
    plt = None  # plotext is optional, so we handle the import gracefully

# Function to detect if the system supports emojis
def supports_emojis():
    """Check if the system can properly display emojis."""
    try:
        # Try to print a simple emoji to see if it works
        test_emoji = "✅"
        print(test_emoji, end='')
        return True
    except UnicodeEncodeError:
        return False
    finally:
        # Clear the test output
        print('\r', end='')

# Determine if emojis are supported
EMOJIS_SUPPORTED = supports_emojis()

# Function to safely print text with emojis or fallback
def safe_print(text):
    """Print text safely, handling Unicode/emoji issues on Windows."""
    if not EMOJIS_SUPPORTED:
        # Remove emojis if they're not supported
        import re
        # Remove emoji characters (Unicode range)
        clean_text = re.sub(r'[\U0001f600-\U0001f64f\U0001f300-\U0001f5ff\U0001f680-\U0001f6ff\U0001f1e0-\U0001f1ff\U00002600-\U000027bf\U0001f900-\U0001f9ff\U0001f018-\U0001f270\U000023f0-\U000023ff\U00002190-\U000021ff\U000025a0-\U000025ff\U00002b00-\U00002bff]+', '', text)
        print(clean_text)
    else:
        print(text)

# Color codes for Windows/Linux compatibility
class Colors:
    RED = '\033[31m' if sys.platform != 'win32' else ''
    GREEN = '\033[32m' if sys.platform != 'win32' else ''
    YELLOW = '\033[33m' if sys.platform != 'win32' else ''
    BLUE = '\033[34m' if sys.platform != 'win32' else ''
    MAGENTA = '\033[35m' if sys.platform != 'win32' else ''
    CYAN = '\033[36m' if sys.platform != 'win32' else ''
    WHITE = '\033[37m' if sys.platform != 'win32' else ''
    BOLD = '\033[1m' if sys.platform != 'win32' else ''
    RESET = '\033[0m' if sys.platform != 'win32' else ''

# For Windows compatibility, we'll use colorama if available
try:
    from colorama import init, Fore, Back, Style
    init(autoreset=True)  # Initialize colorama and auto-reset colors

    # Override color constants with colorama colors
    Colors.RED = Fore.RED
    Colors.GREEN = Fore.GREEN
    Colors.YELLOW = Fore.YELLOW
    Colors.BLUE = Fore.BLUE
    Colors.MAGENTA = Fore.MAGENTA
    Colors.CYAN = Fore.CYAN
    Colors.WHITE = Fore.WHITE
    Colors.BOLD = Style.BRIGHT
    Colors.RESET = Style.RESET_ALL
except ImportError:
    # If colorama is not available, we'll use basic ANSI codes or no colors
    pass


class ConsoleUI:
    """
    Console-based user interface for the todo application.

    Handles user input/output and delegates operations to the TodoManager.
    """

    def __init__(self):
        """Initialize the ConsoleUI with a TodoManager instance."""
        self.todo_manager = TodoManager()

    def display_menu(self):
        """Display the main menu options to the user."""
        print(f"\n{Colors.CYAN}{'='*50}")
        print(f"{Colors.CYAN}📋 TODO APPLICATION MENU{Colors.RESET}")
        print(f"{Colors.CYAN}{'='*50}{Colors.RESET}")
        print(f"{Colors.WHITE}1. 📝 Add Task{Colors.RESET}")
        print(f"{Colors.WHITE}2. 📋 View Tasks{Colors.RESET}")
        print(f"{Colors.WHITE}3. ✏️  Update Task{Colors.RESET}")
        print(f"{Colors.WHITE}4. 🗑️  Delete Task{Colors.RESET}")
        print(f"{Colors.WHITE}5. ✅ Mark Task Complete{Colors.RESET}")
        print(f"{Colors.WHITE}6. 🔄 Mark Task Incomplete{Colors.RESET}")
        print(f"{Colors.WHITE}7. 🚪 Exit{Colors.RESET}")
        print(f"{Colors.CYAN}{'.'*50}{Colors.RESET}")

    def get_user_choice(self):
        """Get the user's menu choice."""
        try:
            choice = input("Enter your choice (1-7): ").strip()
            return choice
        except EOFError:
            return "7"  # Treat as exit

    def add_task(self):
        """Add a new task to the todo list."""
        print(f"\n{Colors.YELLOW}--- 📝 Add New Task ---{Colors.RESET}")
        title = input(f"{Colors.GREEN}Enter task title: {Colors.RESET}").strip()

        if not title:
            print(f"{Colors.RED}Error: Task title cannot be empty!{Colors.RESET}")
            return

        description = input(f"{Colors.GREEN}Enter task description (optional): {Colors.RESET}").strip()
        try:
            task = self.todo_manager.create_task(title, description)
            print(f"{Colors.GREEN}✅ Task added successfully!{Colors.RESET}")
            print(f"{Colors.CYAN}🆔 ID: {task.id}{Colors.RESET}")
            print(f"{Colors.BLUE}📅 Created: {task.created_at.strftime('%Y-%m-%d %H:%M:%S')}{Colors.RESET}")
        except ValueError as e:
            print(f"{Colors.RED}❌ Error: {e}{Colors.RESET}")

    def display_tasks(self):
        """Display all tasks in the todo list with chart visualization."""
        print(f"\n{Colors.BLUE}--- 📋 All Tasks ---{Colors.RESET}")
        tasks = self.todo_manager.get_all_tasks()

        if not tasks:
            print(f"{Colors.YELLOW}📭 No tasks found.{Colors.RESET}")
            return

        for task in tasks:
            status_emoji = "✅" if task.completed else "⏳"
            status_color = Colors.WHITE  # Use white color for all tasks

            print(f"{status_color}[{status_emoji}] {Colors.CYAN}🆔 ID: {task.id}{Colors.RESET} | {Colors.BOLD}{task.title}{Colors.RESET}")

            if task.description:
                print(f"{Colors.WHITE}   📝 Description: {task.description}{Colors.RESET}")

            # Show creation date
            print(f"{Colors.WHITE}   📅 Created: {task.created_at.strftime('%Y-%m-%d %H:%M:%S')}{Colors.RESET}")

            # Show completion date if completed
            if task.completed and task.completed_at:
                print(f"{Colors.WHITE}   ✅ Completed: {task.completed_at.strftime('%Y-%m-%d %H:%M:%S')}{Colors.RESET}")

            print(f"{Colors.CYAN}{'.'*50}{Colors.RESET}")

        print(f"{Colors.WHITE}Total tasks: {len(tasks)}{Colors.RESET}")

        # Display chart visualization
        self.display_tasks_chart(tasks)

    def display_tasks_chart(self, tasks):
        """Display a table visualization of tasks with date, time, ID, and description."""
        print(f"\n{Colors.MAGENTA}📋 TASKS TABLE VIEW{Colors.RESET}")
        print(f"{Colors.MAGENTA}{'='*80}{Colors.RESET}")

        # Table header
        print(f"{Colors.CYAN}{'ID':<5} {'Status':<8} {'Date':<12} {'Time':<10} {'Description':<35}{Colors.RESET}")
        print(f"{Colors.CYAN}{'-'*5} {'-'*8} {'-'*12} {'-'*10} {'-'*35}{Colors.RESET}")

        if not tasks:
            print(f"{Colors.YELLOW}No tasks to display.{Colors.RESET}")
        else:
            # Display each task in table format
            for task in tasks:
                status = "✅" if task.completed else "⏳"
                task_id = str(task.id)
                date_str = task.created_at.strftime('%Y-%m-%d')
                time_str = task.created_at.strftime('%H:%M:%S')
                description = task.description if task.description else task.title
                # Truncate description if too long
                if len(description) > 35:
                    description = description[:32] + "..."

                # Color coding for completed vs pending tasks
                if task.completed:
                    color = Colors.GREEN
                else:
                    color = Colors.WHITE

                print(f"{color}{task_id:<5} {status:<8} {date_str:<12} {time_str:<10} {description:<35}{Colors.RESET}")

        print(f"{Colors.MAGENTA}{'='*80}{Colors.RESET}")

    def update_task(self):
        """Update an existing task."""
        print(f"\n{Colors.YELLOW}--- ✏️  Update Task ---{Colors.RESET}")
        try:
            task_id = int(input(f"{Colors.GREEN}Enter task ID to update: {Colors.RESET}"))
        except ValueError:
            print(f"{Colors.RED}❌ Error: Please enter a valid task ID (number).{Colors.RESET}")
            return

        # Check if task exists
        existing_task = self.todo_manager.get_task_by_id(task_id)
        if not existing_task:
            print(f"{Colors.RED}❌ Error: Task with ID {task_id} not found.{Colors.RESET}")
            return

        print(f"{Colors.CYAN}Current task: {existing_task.title}{Colors.RESET}")
        if existing_task.description:
            print(f"{Colors.CYAN}Current description: {existing_task.description}{Colors.RESET}")

        new_title = input(f"{Colors.GREEN}Enter new title (or press Enter to keep current): {Colors.RESET}").strip()
        new_description = input(f"{Colors.GREEN}Enter new description (or press Enter to keep current): {Colors.RESET}").strip()

        # Prepare updates (only update if user provided new values)
        title_update = new_title if new_title else None
        description_update = new_description if new_description else None

        try:
            success = self.todo_manager.update_task(
                task_id,
                title_update if title_update != "" else None,
                description_update if description_update != "" else None
            )
            if success:
                print(f"{Colors.GREEN}✅ Task updated successfully!{Colors.RESET}")
                # Show updated task info
                updated_task = self.todo_manager.get_task_by_id(task_id)
                print(f"{Colors.CYAN}🆔 ID: {updated_task.id}{Colors.RESET}")
                print(f"{Colors.CYAN}📝 Title: {updated_task.title}{Colors.RESET}")
                if updated_task.description:
                    print(f"{Colors.CYAN}📖 Description: {updated_task.description}{Colors.RESET}")
            else:
                print(f"{Colors.RED}❌ Error updating task.{Colors.RESET}")
        except ValueError as e:
            print(f"{Colors.RED}❌ Error: {e}{Colors.RESET}")

    def delete_task(self):
        """Delete a task."""
        print(f"\n{Colors.RED}--- 🗑️  Delete Task ---{Colors.RESET}")
        try:
            task_id = int(input(f"{Colors.GREEN}Enter task ID to delete: {Colors.RESET}"))
        except ValueError:
            print(f"{Colors.RED}❌ Error: Please enter a valid task ID (number).{Colors.RESET}")
            return

        # Get the task before deletion to show its info
        task_to_delete = self.todo_manager.get_task_by_id(task_id)
        if task_to_delete:
            print(f"{Colors.YELLOW}⚠️  About to delete task: {task_to_delete.title}{Colors.RESET}")
            confirm = input(f"{Colors.RED}Type 'DELETE' to confirm: {Colors.RESET}").strip()
            if confirm != 'DELETE':
                print(f"{Colors.YELLOW}❌ Deletion cancelled.{Colors.RESET}")
                return

        success = self.todo_manager.delete_task(task_id)
        if success:
            print(f"{Colors.RED}🗑️  Task with ID {task_id} deleted successfully!{Colors.RESET}")
        else:
            print(f"{Colors.RED}❌ Error: Task with ID {task_id} not found.{Colors.RESET}")

    def mark_task_complete(self):
        """Mark a task as complete."""
        print(f"\n{Colors.GREEN}--- ✅ Mark Task Complete ---{Colors.RESET}")
        try:
            task_id = int(input(f"{Colors.GREEN}Enter task ID to mark complete: {Colors.RESET}"))
        except ValueError:
            print(f"{Colors.RED}❌ Error: Please enter a valid task ID (number).{Colors.RESET}")
            return

        # Get task before marking complete to show its info
        task = self.todo_manager.get_task_by_id(task_id)
        if task:
            print(f"{Colors.CYAN}Marking task as complete: {task.title}{Colors.RESET}")

        success = self.todo_manager.mark_task_complete(task_id)
        if success:
            completed_task = self.todo_manager.get_task_by_id(task_id)
            print(f"{Colors.GREEN}✅ Task with ID {task_id} marked as complete!{Colors.RESET}")
            print(f"{Colors.GREEN}📅 Completed at: {completed_task.completed_at.strftime('%Y-%m-%d %H:%M:%S')}{Colors.RESET}")
        else:
            print(f"{Colors.RED}❌ Error: Task with ID {task_id} not found.{Colors.RESET}")

    def mark_task_incomplete(self):
        """Mark a task as incomplete."""
        print(f"\n{Colors.YELLOW}--- 🔄 Mark Task Incomplete ---{Colors.RESET}")
        try:
            task_id = int(input(f"{Colors.GREEN}Enter task ID to mark incomplete: {Colors.RESET}"))
        except ValueError:
            print(f"{Colors.RED}❌ Error: Please enter a valid task ID (number).{Colors.RESET}")
            return

        # Get task before marking incomplete to show its info
        task = self.todo_manager.get_task_by_id(task_id)
        if task:
            print(f"{Colors.CYAN}Marking task as incomplete: {task.title}{Colors.RESET}")

        success = self.todo_manager.mark_task_incomplete(task_id)
        if success:
            print(f"{Colors.YELLOW}🔄 Task with ID {task_id} marked as incomplete!{Colors.RESET}")
            print(f"{Colors.YELLOW}📅 Completion status reset{Colors.RESET}")
        else:
            print(f"{Colors.RED}❌ Error: Task with ID {task_id} not found.{Colors.RESET}")

    def run(self):
        """Main application loop."""
        print(f"{Colors.CYAN}{'='*52}{Colors.RESET}")
        print(f"{Colors.CYAN}|{Colors.BOLD}        📋 WELCOME TO THE TODO APPLICATION       {Colors.RESET}{Colors.CYAN}|{Colors.RESET}")
        print(f"{Colors.CYAN}{'='*52}{Colors.RESET}")
        print(f"{Colors.GREEN}💡 Manage your tasks with ease!{Colors.RESET}")

        while True:
            self.display_menu()
            choice = self.get_user_choice()

            if choice == "1":
                self.add_task()
            elif choice == "2":
                self.display_tasks()
            elif choice == "3":
                self.update_task()
            elif choice == "4":
                self.delete_task()
            elif choice == "5":
                self.mark_task_complete()
            elif choice == "6":
                self.mark_task_incomplete()
            elif choice == "7":
                print(f"{Colors.MAGENTA}👋 Thank you for using the Todo Application. Goodbye!{Colors.RESET}")
                break
            else:
                print(f"{Colors.RED}❌ Invalid choice. Please enter a number between 1-7.{Colors.RESET}")

            # Pause to let user see the result before showing menu again
            input(f"\n{Colors.YELLOW}Press Enter to continue...{Colors.RESET}")