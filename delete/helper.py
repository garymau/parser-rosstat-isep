from pathlib import Path

#UNPACK_RAR_EXE = str(find_repo_root() / 'bin' / 'UnRAR.exe') 

def find_repo_root():
    """Returns root folder for repository.
    
    Current file is assumed to be at:
        <repo_root>/helper.py
        
    """
    levels_up = 0
    return Path(__file__).parents[levels_up]

def md(folder):
    """Create *folder* if not exists"""
    if not folder.exists():
        folder.mkdir()

class DataFolder:
    data_root = find_repo_root() / 'data'
    raw = data_root  / 'raw'
    interim = data_root  / 'interim'
    processed = data_root  / 'processed'   