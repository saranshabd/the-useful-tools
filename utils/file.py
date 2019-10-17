import click
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


def create_license() -> None:
    """utility function to create license file"""

    # prompt to check if the user wants to create a license file
    is_license: bool = click.prompt(
        'do you want to create license file?', default=False, type=bool)
    if is_license is True:
        # prompt the user for license owner type
        license_type: str = click.prompt(
            'license type?', type=click.Choice(['MIT', 'Apache 2.0'], case_sensitive=False))
        license_type = license_type.strip().upper()

        # prompt the user for license owner name
        license_owner: str = click.prompt(
            'license owner name?', default="<license-owner>", type=str)
        license_owner = license_owner.strip().upper()

        # prompt the user for license year (default set to current year)
        license_year: int = click.prompt(
            'license year?', default=datetime.now().year, type=int)

        # load license
        if 'MIT' == license_type:
            from data.licenses.MIT import LICENSE
        else:  # apache 2.0
            from data.licenses.APACHE import LICENSE

        # fill license with user details
        LICENSE = LICENSE.replace('[year]', str(license_year))
        LICENSE = LICENSE.replace('[fullname]', license_owner)

        # create license file
        with open('LICENSE', 'w') as file:
            file.write(LICENSE)

        # load license notice
        if 'MIT' == license_type:
            from data.license_notices.MIT import LICENSE as LICENSE_NOTICE
        else:  # apache 2.0
            from data.license_notices.APACHE import LICENSE as LICENSE_NOTICE

        # fill license with user details
        LICENSE_NOTICE = LICENSE_NOTICE.replace('[year]', str(license_year))
        LICENSE_NOTICE = LICENSE_NOTICE.replace('[fullname]', license_owner)

        # create license notice file
        with open('LICENSE_NOTICE', 'w') as file:
            file.write(LICENSE_NOTICE)


def create_readme() -> None:
    """utility function to create README.md"""

    # get project directory name
    dir_name: str = str(os.getcwd()).split('/')[-1]

    # load content
    from data.README import README
    README = README.replace('[title]', dir_name)

    # create file
    with open('README.md', 'w') as file:
        file.write(README)


def create_gitignore(language: str) -> None:
    """utility function to create .gitignore"""

    # load content
    if 'c' == language or 'cpp' == language:
        from data.gitignore.cpp import GITIGNORE
    elif 'java' == language:
        from data.gitignore.java import GITIGNORE
    elif 'py' == language:
        from data.gitignore.py import GITIGNORE
    else:  # js
        from data.gitignore.js import GITIGNORE

    # create file
    with open('.gitignore', 'w') as file:
        file.write(GITIGNORE)
