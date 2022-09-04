import os

first = ["3"]
second = [str(x) for x in range(6,11)]
third = [str(x) for x in range(14)]
versions = []
for f in first:
    for s in second:
        for t in third:
            versions.append(f+"."+s+"."+t)

for v in versions:
    try:
        os.system(f"wget https://npm.taobao.org/mirrors/python/{v}/Python-{v}.tar.xz -P ~/.pyenv/cache/")
    except:
        continue
