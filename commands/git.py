import click
from datetime import datetime
import subprocess

# import utils
from utils.language import is_supported_language
import utils.git as git_utils


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
    git_utils.create_license()

    # create README.md
    git_utils.create_readme()

    # create .gitignore
    if language is not None:
        git_utils.create_gitignore(language)
