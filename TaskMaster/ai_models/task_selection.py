```python
class TaskSelection:
    def __init__(self):
        self.tasks = {
            "clone_git": "Clone a Git Repository",
            "upload_pdf": "Upload a PDF",
            "upload_code": "Upload Code"
        }

    def select_task(self, task_id):
        if task_id not in self.tasks:
            raise ValueError(f"Invalid task id: {task_id}")
        return self.tasks[task_id]
```