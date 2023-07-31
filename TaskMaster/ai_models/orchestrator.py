```python
from ai_models.git_operations import GitOperationsModel
from ai_models.pdf_processing import PDFProcessingModel
from ai_models.code_processing import CodeProcessingModel
from ai_models.real_time_updates import RealTimeUpdatesModel

class OrchestratorModel:
    def __init__(self):
        self.git_operations = GitOperationsModel()
        self.pdf_processing = PDFProcessingModel()
        self.code_processing = CodeProcessingModel()
        self.real_time_updates = RealTimeUpdatesModel()

    def orchestrate_task(self, task_type, task_input):
        if task_type == "Clone a Git Repository":
            repository_url = task_input
            self.git_operations.clone_repository(repository_url)
            self.real_time_updates.update_task_status("Cloning Git Repository")
        elif task_type == "Upload a PDF":
            pdf_file = task_input
            self.pdf_processing.process_pdf(pdf_file)
            self.real_time_updates.update_task_status("Processing PDF")
        elif task_type == "Upload Code":
            code_file = task_input
            self.code_processing.process_code(code_file)
            self.real_time_updates.update_task_status("Processing Code")
        else:
            raise ValueError("Invalid task type")
```