import click
from datetime import datetime
import subprocess

# import utils
from utils.language import is_supported_language
import utils.git as git_utils
import utils.file as file_utils


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


@click.group()
def git():
    pass


@git.command()
@click.option('-l', '--language', type=str)
def init(language: str):
    """initialize git repository"""

    # check if programming language is supported
    if language is not None and is_supported_language(language) is not True:
        click.echo(
            f"ERROR: {language} file extension programming language not supported")
        return

    # initialize git repository
    git_utils.init()

    # create LICENSE
    file_utils.create_license()

    # create README.md
    file_utils.create_readme()

    # create .gitignore
    if language is not None:
        file_utils.create_gitignore(language)


@git.command('commit')
@click.option('-m', '--message', required=True, type=str)
@click.option('-b', '--branch', type=str)
def commit(message: str, branch: str):
    """commit changes to git repository"""

    # check if git repository exists
    if git_utils.check_git() is not True:
        click.echo('ERROR: git repository for current directory does not exists')
        return

    # add changes for staging
    git_utils.add()

    # prompt to confirm if the user wants to commit changes
    confirm_commit: bool = click.prompt(
        'confirm commit?', default=True, type=bool)
    if confirm_commit is False:
        return

    # commit changes
    git_utils.commit(message)

    # prompt to check if the user wants to push changes to a remote repository
    confirm_push: bool = click.prompt('push changes?', default=True, type=bool)
    if confirm_push is False:
        return

    # push to remote repository
    git_utils.push(branch)


@git.command()
def log():
    """log git commits"""

    # check if git repository exists
    if git_utils.check_git() is not True:
        click.echo('ERROR: git repository for current directory does not exists')
        return

    # print git repository log
    git_utils.log()
