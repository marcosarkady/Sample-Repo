import sys
import pyperclip

# git
# source d:/DesktopD/myscript/start/venv/Scripts/activate
# powershell
# d:/DesktopD/myscript/start/venv/Scripts/activate.ps1

# strg+shift+P

# python -m venv ProjektName
# d:/DesktopD/myscript/start/venv/Scripts/Activate.ps1
# deactivate
# rmdir ProjektName /s (for subtrees)

# python -m venv projektname --system-site-packages
# pip list --local
# pip freeze
# pip install -r requirements.txt


print(sys.version)
print(sys.executable)
pyperclip.copy("Hey")


def greet(who_to_greet):
    greeting = "Hello, {}".format(who_to_greet)
    return greeting


print(greet("World"))
print(greet("Marco"))
