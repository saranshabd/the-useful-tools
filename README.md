# useful-tools

These are some sets of tools that come in real handy for handling projects with large number of files to maintain. These commands can also be used to maintain small project files. **The toolkit is available for Linux environment only.**

<br>

Following commands are available in our tookit:

## Github Tools

- `useful git init [programming-language-abbreviation]`
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

<br>

#### Supported Programming Languages (with abbreviations)

- C (c)
- C++ (cpp)
- Java (java)
- Python (py)
- JavaScript (js)
