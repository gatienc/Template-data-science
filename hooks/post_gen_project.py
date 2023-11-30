import subprocess
import json

cookiecutter = json.load(open('cookiecutter.json', 'r', encoding="utf-8"))


def git_init():
    subprocess.call(['git', 'init'])
    subprocess.call(['git', 'add', '*'])
    subprocess.call(['git', 'commit', '-m', 'Initial commit'])


def github_init():
    subprocess.call(['gh', 'repo', 'create',
                    cookiecutter.repo_name, '--private', '--source=.', '--remote=upstream'])


if __name__ == '__main__':
    git_init()

    if cookiecutter.use_github == 'y':
        github_init()
