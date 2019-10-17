import click
import subprocess
from datetime import datetime
import os

"""
    Copyright 2019 Shabd Saran

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""


def init() -> None:
    """utility function to initialize git repository"""

    try:
        subprocess.call('git init', shell=True)
    except:
        click.echo('ERROR: failed to initialize git repository')
        return


def check_git() -> bool:
    """utility function to check if git repository exists"""

    return os.path.isdir('.git')


def add() -> None:
    """utility function to add all files for staging"""

    subprocess.call('git add .', shell=True)
    subprocess.call('git status', shell=True)


def commit(message: str) -> None:
    """utility function to commit changes"""

    subprocess.call(f"git commit -m '{message}'", shell=True)


def push(branch: str) -> None:
    """utility function to push changes to remote repository"""

    # get all unique remotes associated with current remote repository
    remotes: str = os.popen('git remote -v').read()
    remotes: list = remotes.split('\n')[:-1]
    for i in range(len(remotes)):
        remotes[i] = remotes[i].split('\t')[0]
    remotes = list(set(remotes))

    if 1 == len(remotes):
        # since there is only one remote, push changes
        if branch is None:
            os.system(f'git push {remotes[0]} master')
        else:
            os.system(f'git push {remotes[0]} {branch}')
    else:
        # prompt the user to select one of the remotes
        remote: str = click.prompt(
            'which remote?', default=remote[0], type=click.Choice(remotes, case_sensitive=False))

        # push changes to the given remote
        if branch is None:
            os.system(f'git push {remote} master')
        else:
            os.system(f'git push {remote} {branch}')
