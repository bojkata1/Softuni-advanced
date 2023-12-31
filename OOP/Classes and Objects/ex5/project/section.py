from project.task import Task
from typing import List


class Section:
    def __init__(self, name):
        self.name = name
        self.tasks: List[Task] = []

    def add_task(self, new_task: Task):
        if new_task in self.tasks:
            return f"Task is already in the section {self.name}"
        self.tasks.append(new_task)
        return f"Task {new_task.details()} is added to the section"

    def complete_task(self, task_name: Task):
        for task in self.tasks:
            if task_name == task.name and task.completed is False:
                task.completed = True
                return f"Completed task {task.name}"
        return f"Could not find task with the name {task_name}"

    def clean_section(self):
        removed_tasks = 0
        for task in self.tasks:
            if task.completed is True:
                self.tasks.remove(task)
                removed_tasks += 1
        return f"Cleared {removed_tasks} tasks."

    def view_section(self):
        res = [f"Section {self.name}:"]
        for task in self.tasks:
            res.append(task.details())
        return "\n".join(res)
