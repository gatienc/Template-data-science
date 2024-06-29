[![Copier](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/copier-org/copier/master/img/badge/badge-grayscale-border.json)](https://github.com/copier-org/copier)

# Data science project template

This is a project template for a data science project. It is based on copier.

If you don't have copier installed, you can install it with the following command:

```bash
    pip install copier
```

To create a new project from this template, you can use the following command:


After you have created a new project from this template, you can use the following commands to get started:

```bash
    git init
    git add *
    git commit -m 'Initial commit'
```

if you want to use poetry, you can use the following commands:

```bash
    poetry init
    poetry install
```

if you want to use venv, you can use the following commands:

```bash
    python3 -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
```



don't forget to add the following lines to your .gitconfig file to use nbstripout with jupyter notebooks:

```
[filter "nbstripout"]
    clean = nbstripout --strip
    smudge = cat %f
    required = true
```
