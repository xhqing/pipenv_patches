import os, sys
from commonException import *

if __name__ == "__main__":
    """
    args: 
    python_version: "python:3.9.12", "python:3.6.13"
    """
    try:
        python_version = sys.argv[1]
    except IndexError:
        raise CommandError(f"""\033[01;31;01m `python create_venv.py python_version(python:3.9.12 or python:3.6.13)`\033[01;31;01m""")

    os.system("pipenv --rm")
    if python_version == "python:3.6.13":
        os.system("pipenv --python /Users/mac/opt/anaconda3/envs/python36/bin/python3.6")
    elif python_version == "python:3.9.12":
        os.system("pipenv --python /Users/mac/opt/anaconda3/envs/py39/bin/python3.9")
    else:
        raise CommandError(f"""\033[01;31;01m `python create_venv.py python_version("python:3.9.12" or "python:3.6.13")`\033[01;31;01m""")
