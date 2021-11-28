import os

def modify_activate(file: str, old_str: str, new_str: str):
    """
    usage: modify_activate(f"{user_path}/.local/share/virtualenvs/autogbm-sgajus1C/bin/activate", "((autogbm) )", "(autogbm-sgajus1C)")
    note: only one {old_str} in the whole file, then replace; otherwise, do nothing.
    """
    with open(file, "r", encoding="utf-8") as f1:
        count = 0
        for line in f1:
            if old_str in line:
                count += 1

    if count != 1:
        print("\033[01;31;01mWarning: not only one '{}' in the whole file (activate) !!\033[01;00;00m ".format(old_str))
    else:
        with open(file, "r", encoding="utf-8") as f1, open("%s.bak" % file, "w", encoding="utf-8") as f2:
            for line in f1:
                if old_str in line and not os.path.exists(f"{user_path}/.zshrc"):
                    line = line.replace(old_str, new_str+" ")
                elif old_str in line and os.path.exists(f"{user_path}/.zshrc"):
                    line = line.replace(old_str, "")
                f2.write(line)
    
    os.remove(file)
    os.rename("%s.bak" % file, file)
    print("Modify `activate` file succeed.")

    if os.path.exists(f"{user_path}/.zshrc"):
        source_reset_ps1 = f"source {user_path}/pipenv_patches/reset_ps1.sh"
        with open(f"{user_path}/pipenv_patches/reset_ps1.sh", "w") as rp:
            rp.write(f"""PS1="{new_str} $[PS1-]"\n""".replace("[","{").replace("]","}"))
            rp.write("export PS1")
        with open(f"{user_path}/.zshrc", "r") as zf:
            zfc = zf.read()
        if source_reset_ps1 not in zfc:
            with open(f"{user_path}/.zshrc", "a") as zf:
                zf.write("\n# >>> pipenv patches >>>\n")
                zf.write("if [ $PIPENV_ACTIVE ];then\n")
                zf.write(f"    {source_reset_ps1}\n")
                zf.write("fi\n")
                zf.write("# <<< pipenv patches <<<\n")
        print("Add >>> pipenv patches >>> settings to ~/.zshrc file succeed.")
        
if __name__ == "__main__":

    print("Runing ~/pipenv_patches/modify_prompt.py...")
    user_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    base = f"{user_path}/.local/share/virtualenvs/"
    proj_dir = os.path.abspath(".").split("/")[-1]

    base_dirlist = os.listdir(base)
    target = False
    for name in base_dirlist:
        if name[:-9] == proj_dir:
            target = base + name + "/bin/activate"
            venvdir_name = name
            break

    if not target:
        print("\033[01;31;01mWarning: not found target file (activate) !!\033[01;00;00m ")
    
    print("Modifing `activate` file...")
    print("Target file (activate) location: {}".format(target))
    modify_activate(target, "(({}) ) ".format(proj_dir), "({})".format(venvdir_name))
    
    print("Done.")




