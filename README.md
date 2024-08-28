# References

- PEP 8 guidelines, see [Resource](Resource.md) for links to PEP 8 guidelines and checker resource.
- for max line width, vscode, settings, search for autopep8 `"python.formatting.autopep8Args": ["--max-line-length=120"]`, does not work in github codespace. used `.pep8` file in workspace
- https://code.visualstudio.com/docs/python/environments
- https://docs.python.org/3/tutorial/venv.html

## mac setup

check brew installation path

```
$ brew info python@3.11
==> python@3.11: stable 3.11.0 (bottled)
Interpreted, interactive, object-oriented programming language
https://www.python.org/
/usr/local/Cellar/python@3.11/3.11.0 (3,212 files, 62.7MB) *
  Poured from bottle on 2022-12-17 at 21:50:20
From: https://github.com/Homebrew/homebrew-core/blob/HEAD/Formula/python@3.11.rb
License: Python-2.0
==> Dependencies
Build: pkg-config ✔
Required: mpdecimal ✔, openssl@1.1 ✔, sqlite ✔, xz ✔
==> Caveats
Python has been installed as
  /usr/local/bin/python3.11

Unversioned and major-versioned symlinks `python`, `python3`, `python-config`, `python3-config`, `pip`, `pip3`, etc. pointing to
`python3.11`, `python3.11-config`, `pip3.11` etc., respectively, have been installed into
  /usr/local/opt/python@3.11/libexec/bin

If you do not need a specific version of Python, and always want Homebrew's `python3` in your PATH:
  brew install python3

You can install Python packages with
  pip3.11 install <package>
They will install into the site-package directory
  /usr/local/lib/python3.11/site-packages

tkinter is no longer included with this formula, but it is available separately:
  brew install python-tk@3.11

gdbm (`dbm.gnu`) is no longer included in this formula, but it is available separately:
  brew install python-gdbm@3.11
`dbm.ndbm` changed database backends in Homebrew Python 3.11.
If you need to read a database from a previous Homebrew Python created via `dbm.ndbm`,
you'll need to read your database using the older version of Homebrew Python and convert to another format.
`dbm` still defaults to `dbm.gnu` when it is installed.

For more information about Homebrew and Python, see: https://docs.brew.sh/Homebrew-and-Python
==> Analytics
install: 369,399 (30 days), 536,718 (90 days), 536,718 (365 days)
install-on-request: 9,873 (30 days), 21,254 (90 days), 21,254 (365 days)
build-error: 236 (30 days)
```

### weird jq bug

Previously installed conda on mac. Ran into a weird issue that the conda `jq` is overriding and behavior is different comparing to regular `jq`.

### vs code virtual env

1. use command palette (cmd+shift+p), python: create environment, pick the python 3.11 (`bisect` with `key` function available in 3.11) interpreter installed with brew.
1. command palett, python: select interpreter, select the virtual env just created
1. this will create a virtual env named `.venv` in workspace root, can activate on command line
1. run file button will activate the virtual env as well
1. python test explorer extension can run tests without activation of the virtual env


### virtual env on command line

```
python3 -m venv test1
cd test1
source bin/activate
which python
which pip
pip install requests
pip list
```

## windows setup

Used IntelliJ community edition. Installed python community edition plugin. Menu: "Project structure", "SDK", "Add Python SDK from disk", chose to download python 3.12 from python.org, SDK location set to <project_path>\venv, made it globally available for other projects. 
