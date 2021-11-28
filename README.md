# pipenv_patches
## Description
Mainly solving two problems of pipenv:
1. Correctly showing the beautiful prompt virtualenvs' name of current project in the `~/.local/share/virtualenvs`;
2. Protect the virtualenv's name of current project from disappearing when using the `source ~/.zshrc` command.

if you don't use zsh terminal and .zshrc file, this patches can also solve the first problem.

## Usage
```
cd ~
git clone git@github.com:xhqing/pipenv_patches.git
```
and then, config your `~/.zshrc` file for convenient when creating your pipenv virtualenv in the root dir of your current project:
```
vim ~/.zshrc # open your .zshrc file, add alias as follows 

# it's a suggestion, some params depends on you 
alias pipenvPython="pipenv install --dev --skip-lock --python /path/to/xxx/python36/bin/python3.6 && pipenv run python ~/pipenv_patches/modify_prompt.py"
```
then
```
source ~/.zshrc
```
now, you can using `pipenvPython` to create your virtualenv in the root dir of your project.

if you dont use `.zshrc` file, maybe you need config your `.bashrc` file or others, but i dont know the second problem if exists in other shell yet,
currently the second problem can be solved only when you use zsh.

## Test
Development in MacOS Python3.6, test in Ubuntu Python3.6, not support windows yet.
Test with Ubuntu docker images, you can use `Dockerfile` in current dir to build container for test as follows:
```
docker build test_pipenv_patches .
docker run -it --name=test_pipenv_patches test_pipenv_patches 
```
or pull test images i have built as follows:
```
docker pull xhq123/test_pipenv_patches
``` 
have fun.

## License
This project is licensed under the terms of the MIT license. See [LICENSE](https://github.com/xhqing/pipenv_patches/blob/master/LICENSE) for additional details.  
