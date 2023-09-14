# Python 3.11 Template 2023

This repo provides some basic setup you might want for your own python project, including:
* tox set up to run pytest, black, and pylint,
* pytest set up with coverage results,
* pyproject.toml,
* Github CI integration,
* and some example boilerplate code.

This repo does *not* include:
* A setup.py, which is deprecated,
* automatically building requirements files, e.g. with pip-compile,
* automated documentation builders.

This repo is designed to use *Python 3.11*, but it should be pretty trivial to change with
`grep py311` and `grep 3.11`. You can create an env with `conda` using

```
conda create --name <your_project> python=3.11
```

and then install all the requirements with

```
pip install -r requirements.txt
```

and verify the install with

```
tox
```
