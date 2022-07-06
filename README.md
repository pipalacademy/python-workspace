# Python Workspace

This repository contains instructions to setup a python workspace on your computer, to get ready for a python training from Pipal Academy.

The python workspace is just a simple python virtualenv setup.

## Quick start

Step 1: Clone this repository

```
$ git clone https://github.com/pipalacademy/python-workspace
...
```

And cd to that directory.

```
$ cd python-workspace
```

Step 2: Run a python virtual env

```
$ python3 -m venv venv
```

If that command doesn't work, try giving the complete path to your Python executable. If you are on windows, this could be something like `C:/Program Files/Python39/python.exe`.

Step 3: Activate the virtualenv

If you are on Linux or Mac OS X:

```
$ source venv/bin/activate
```

If you are on Windows:

```
$ venv\bin\activate.bat
```

Step 4: Install required dependencies

```
$ pip install -r requirements.txt
```