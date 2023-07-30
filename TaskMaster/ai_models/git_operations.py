```python
import git
from git import Repo

class GitOperationsModel:
    def __init__(self):
        pass

    def clone_repository(self, repository_url, destination):
        try:
            Repo.clone_from(repository_url, destination)
            return True
        except git.GitCommandError as e:
            print(f"Error: {str(e)}")
            return False
```
