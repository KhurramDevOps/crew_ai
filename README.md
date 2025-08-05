# **Learning CREW AI!**

[![crew-only-logo.png](https://i.postimg.cc/G3xn0D6W/crew-only-logo.png)](https://postimg.cc/F1zB3Yrp)

### **Overview!**

- CREW AI is a Python library for creating and training AI models. It provides a simple and intuitive API for building and deploying AI models.
- HERE'S THE CREW AI OFFICIAL DOCUMENTATIONS[Crew_AI Documentation](https://docs.crewai.com/introduction).

### **Installation!**

### Prerequisites:

Before you start, make sure you have Python 3.10 or higher but less than 3.13. If you have Python 3.13 or higher, you may encounter errors during the installation process.
To check your Python version

```bash
python3 --version

```

## Install CREW AI IF YOU HAVE Python 3.10 or higher but less than 3.13

### FOR WINDOWS

- Open your terminal or command prompt.
- first check the python

```powershell
python --version
```

- Install CREW AI using pip

```powershell
pip install crewai crewai-tools
```

- If you encounter any errors during the installation process, Then You have to Install the crewai Tools here's the link below

  ### [Click Here To download](https://visualstudio.microsoft.com)

  - Now you will see this page:

  [![c++ credentials.png](https://i.postimg.cc/fbZqVSsW/Screenshot-2025-01-25-at-18-48-15.png)](https://postimg.cc/bZC9MJd4)

  -After installation , you have to open the downlaoded file and follow the instructions

- ### You have to tick the check box

- MSVC v143 - VS 2022 C++ x64/x86Windows 10 SDK
- You have to check this
- Now you will see this page:
  [![crewai check box](https://i.postimg.cc/kgzh738N/Screenshot-2025-01-27-at-20-37-24.png)](https://postimg.cc/mP3SSnmh)
- Now you have to click on the install button

#### now u see this page

[![downloading screen.png](https://i.postimg.cc/SKL5d12W/Screenshot-2025-01-27-at-20-37-42.png)](https://postimg.cc/4KdBN51d)

-  you have to wait for the installation process to complete

#### Now try again to install CREWAI

```powershell
pip install crewai crewai-tools
```

### Hope so it will downloaded

## **Downgrading Python Version (If Needed)**

If you encounter errors because your global Python version is too high (e.g., Python 3.13), you can downgrade to Python 3.12.8 using pyenv.

### **FACED Alot of ERROR ON Downgrading Python Version**

- **Error Encountered:** I encountered errors because my global Python version was too new (Python 3.13.1) for some dependencies in the project.
- **Solution:** I used `pyenv` to downgrade my Python version to 3.12.8 as recommended by the Crew AI docs.
- I have the **3.13.1 python version** installed on my system. I will install the required version of python using **pyenv**.

- ## SOLUTION FOR MacOS/LINUX:

1. ### First, install **pyenv** using the following command:

- **For MacOS/Linux**

  ```bash
  brew install pyenv

  ```

2. #### Now Install Python Version 3.12.8 using pyenv:.

```bash
  pyenv install 3.12.8
```

- Run this command in your project directory:
  ```bash
  pyenv local 3.12.8
  ```

3. ### Now Install pyenv-vitualenv

```bash
brew install pyenv-virtualenv

```

4. ### set up Shell Configuration
   ```bash
   echo 'if which pyenv > /dev/null; then eval "$(pyenv init --path)"; eval "$(pyenv init -)"; eval "$(pyenv virtualenv-init -)"; fi' >> ~/.zshrc
   source ~/.zshrc
   ```
5. ### Verify the Plugin Installation

   ```bash
   pyenv commands | grep virtualenv

   ```

6. ### Create the Virtual Environment
   ```bash
   pyenv virtualenv 3.12.8 crew_ai_env
   ```



9. **NOwW**:

1. ### Navigate to the project directory

1. ### Run the following command in the command prompt:
   ```powershell
   pyenv local 3.12.8
   ```
   This will set the local Python version to 3.12.8. in your project directory.
1. ### verify
   ```powershell
   pyenv version # This should show Python 3.12.8
   ```
1. ### Create the virtual environment
   ```powershell
   python -m venv myenv
   ```
   This will create a virtual environment named myenv in your project directory.USing python 3.12.8

### **Installing Crew AI**

1. Install CrewAI:
   Install Crew AI with the recommended tools:

   ```Terminal
   pip install crewai crewai-tools

   ```

2. Upgrade CrewAI (If Needed):

   If you already have an older version, use:

   ```Terminal
   pip install --upgrade crewai crewai-tools

   ```

3. Verify the Installation:

   Run the following to check the installed versions:

   ```Terminal
   pip freeze | grep crewai
   ```

   You should see something like:

   ```bash
   crewai==0.95.0
   crewai-tools==0.25.8
   ```

## **Troubleshooting Tips**

1. **Python Version Compatibility**: Ensure you're using a compatible version of Python (3.10 to 3.12). If you face issues, downgrade to a supported version using pyenv.

2. **Environment Issues**: If you encounter problems related to the virtual environment, always ensure that you're activating the correct one. You can check your environment with:

```bash
pyenv version
```

3. **Missing Modules**: If you get errors related to missing modules, verify that all dependencies are installed correctly with pip install.

## References:

- [Crew AI Documentation](https://crew.ai/docs/)
- [Installation Guide](https://docs.crewai.com/installation)

### Installation successful! You’re ready to create your first crew.
