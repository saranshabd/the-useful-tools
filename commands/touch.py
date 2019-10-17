import click

# import utils
import utils.file as file_utils
import utils.language as lang_utils

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


@click.command()
@click.argument('file_name', type=str)
def touch(file_name: str):
    """create new file"""

    if 'LICENSE' == file_name.upper():
        # create a license file

        file_utils.create_license()

    else:
        # check if LICENSE_NOTICE file exists
        if file_utils.check_license_notice() is True:
            # create a new file with included license notice

            # check if the programming language of the file is supported
            file_extension: str = file_name.split('.')[-1]
            if lang_utils.is_supported_language(file_extension) is False:
                click.echo(
                    f"ERROR: '{file_extension}' file extension not supported")
                return

            # create new file with license notice included
            file_utils.create_file_with_license_notice(
                file_name, file_extension)

        else:
            # create a regular new file

            file_utils.create_empty_file()
