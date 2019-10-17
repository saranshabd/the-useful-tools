# the-useful-tools

<br>

These are some sets of tools that come in real handy for handling projects with large number of files to maintain. These commands can also be used to maintain small project files. **The toolkit is available for Linux environment only.**

<br>

## Installation

You can install this console application using `pip3`. **Note, the console application is only compatible with Python3**.
<br>

`pip3 install the-useful-tools`

<br>

Following commands are available in our tookit:

## Github Tools

- `useful git init [-l/--language]`
  <br>
  Initialize git repository with necessary files already created for you. User will also be prompted to create a LICENSE file, but its optional. Following are the supported LICENSE types:

  - MIT
  - Apache 2.0

  <br>

  Following are the files that are created:

  - .gitignore
  - README.md (with title set as the project directory name)
  - LICENSE (optional)
  - LICENSE_NOTICE (created only if LICENSE is created)

- `useful git commit [-m/--message] [-b/--branch]`
  <br>
  Add files for staging, commit changes and push them to remote repository with a single command. Commit message option [-m] is a required option. Remote repository branch can be specified with the [-b] option, but its optional. By default, changes will be pushed to `origin master` (if the user confirms to push).

- `useful git log`
  <br>
  When number of git commits go beyond 5-6, you can't view them all at once. When you execute `git log`, it open them in scrollable fashion. `useful git log` stores the logs in a file `git.log` (this file is ignored for git staging) and opens the file in `gedit`. This really helps the programmers to browse through all their commits.

<br>

## File Management Tools

- `useful touch <file_name>`
  <br>
  Works the same was as regular `touch` UNIX command, except if the LICENSE_NOTICE file is present in the project directory, it creates the new file with license notice already included. Automatic license notice addition is only valid for supported languages.

<br>

#### Supported Programming Languages (with abbreviations)

- C (c)
- C++ (cpp)
- Java (java)
- Python (py)
- JavaScript (js)
