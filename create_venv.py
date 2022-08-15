import os, sys
from commonException import *

if __name__ == "__main__":
    """
    args: 
    python_version: "py39", "py36"
    """
    try:
        python_version = sys.argv[1]
    except IndexError:
        raise CommandError(f"""\033[01;31;01m `python create_venv.py python_version("py39" or "py36")`\033[01;31;01m""")

    os.system("pipenv --rm")
    if python_version == "py36":
        os.system("pipenv --python /Users/mac/opt/anaconda3/envs/python36/bin/python3.6")
    elif python_version == "py39":
        os.system("pipenv --python /Users/mac/opt/anaconda3/envs/py39/bin/python3.9")
    else:
        raise CommandError(f"""\033[01;31;01m `python create_venv.py python_version("py39" or "py36")`\033[01;31;01m""")
