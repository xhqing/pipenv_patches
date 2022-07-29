import os
import sys
from commonException import *

if __name__ == "__main__":
    try:
        package_name = sys.argv[1]
    except IndexError:
        raise CommandError(f"""\033[01;31;01m `python uninstall.py package_name`\033[01;31;01m""")

    os.system(f"pipenv uninstall --skip-lock {package_name}")
    os.system(f"pipenv run pip uninstall {package_name}")
