FROM xhq123/ubuntu-pipenvpy36

WORKDIR /app/workdir
RUN mkdir test_project_dir
RUN git clone https://github.com/xhqing/pipenv_patches.git
RUN mv pipenv_patches ~/
CMD ["/bin/zsh"]

