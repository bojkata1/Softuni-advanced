from project.task import Task
class Section:
    def __init__(self, name):
        self.name = name
        self.tasks = []
    def add_task(self, new_task: Task):
        if new_task in self.tasks:
            return f"Task is already in the section {self.name}"
        self.tasks.append(new_task)
        return f"Task {new_task.details()} is added to the section"
    def complete_task(self, task_name: Task):
        if task_name not in self.tasks:
            return f"Could not find task with the name {task_name.name}"
        task_name.completed = True
        return f"Completed task {task_name.name}"
    def clean_section(self):
        removed_tasks = 0
        for task in self.tasks:
            if task.completed is True:
                self.tasks.remove(task)
                removed_tasks += 1
        return f"Cleared {removed_tasks} tasks."
    def view_section(self):
        res = f"Section {self.name}:\n"
        for task in self.tasks:
            res += task.details()+"\n"
        return res
