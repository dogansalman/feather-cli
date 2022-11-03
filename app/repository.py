from git.remote import RemoteProgress
import git
import os

feather_repo = 'https://github.com/dogansalman/feather-erp.git'
default_to_path = f"{os.getcwd()}/feather_erp"

class Progress(RemoteProgress):
    def update(self, op_code, cur_count, max_count=None, message=""):
         if message:
            print(self._cur_line)
            print(message)

def feather_clone_repo(to_local_path):
    # Create a new directory because it does not exist
    isExist = os.path.exists(to_local_path)
    if not isExist:
        os.makedirs(to_local_path)
   
    git.Repo.clone_from(feather_repo, to_local_path, branch='master', progress=Progress())
    print(f"Feather erp application installed to: {to_local_path}")


def feather_update():
    pass
