# Mocking-AWS-Services
Repository is dedicated for providing examples on how to mock AWS services in Python using the `moto` library.

# Setup
1. Install Python 3.9+ on your system.
2. Once installed, open a terminal or command prompt and install pip using `python3 -m ensurepip --upgrade`.
3. Change the location of current working directory of the terminal to the cloned project's root folder. Your terminal should be inside `Mock-AWS-Services` directory.
4. Run the command `python3 -m venv venv`, which will create a virtual environment for managing python packages for you in the current directory. Make sure there is a `venv` folder present. (Additionally, add this folder to `.gitignore` file by creating a `.gitignore` file inside the `venv` folder and adding `*` entry in that file).
5. Run the command `source venv/bin/activate` to activate the virtual environment for your current terminal. On Windows, the command will look like `.\venv\Scripts\activate`.
6. Finally, install the dependencies using `pip install -r requirements.txt`
7. pip should start installing the dependencies on your virtual environment packages.
