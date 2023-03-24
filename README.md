# QML ListModel Example

This repository contains example code demonstrating basic use of a `QAbstractListModel`
bound to a QML `ListView`.

## Environment Setup

### Installing Python

You'll need to have a Python interpreter installed (I used Python 3.10, but any
current version should work fine). On a Windows PC, I recommend [downloading and
installing from python.org](https://www.python.org/downloads/). On my machine,
the interpreter is located at `C:\Python310\python.exe`, but this may differ for
your installation. After installation, note the location of `python.exe`.

### Configuring the Virtual Environment

Using your system's terminal application (in my case, Microsoft's PowerShell),
navigate to the directory into which you cloned this repository. Then, create
a new virtual environment (replace the path to `python.exe` based on where it
is installed on your machine):

`& "C:\Python310\python.exe" -m venv venv`

When it completes, there will be a new directory in there called `venv`. Activate it
by running:

`.\venv\Scripts\activate`

You'll notice that your command prompt is now prefixed with `(venv)` to indicate that
you are in your new Python virtual environment. Now we will install required Python
packages in the virtual environment:

`pip install -r .\requirements.txt`

## Running the Application

In order to run the application, you must first activate a properly-configured
virtual environment if you haven't already (see above). Then, from the root
directory of your cloned repository, run:

`python run-sample.py`

