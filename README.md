# **Learning CREW AI**

[![crew-only-logo.png](https://i.postimg.cc/G3xn0D6W/crew-only-logo.png)](https://postimg.cc/F1zB3Yrp)

### **Overview**

- CREW AI is a Python library for creating and training AI models. It provides a simple and intuitive API for building and deploying AI models.
- HERE'S THE CREW AI OFFICIAL DOCUMENTATIONS[Crew_AI Documentation](https://docs.crewai.com/introduction).

### **Installation**

### Prerequisites:

Before you start, make sure you have Python 3.10 or higher but less than 3.13. If you have Python 3.13 or higher, you may encounter errors during the installation process.
To check your Python version

```bash
python3 --version

```

## **Downgrading Python Version (If Needed)**

If you encounter errors because your global Python version is too high (e.g., Python 3.13), you can downgrade to Python 3.12.8 using pyenv.

### **FACED Alot of ERROR ON Downgrading Python Version**

- **Error Encountered:** I encountered errors because my global Python version was too new (Python 3.13.1) for some dependencies in the project.
- **Solution:** I used `pyenv` to downgrade my Python version to 3.12.8 as recommended by the Crew AI docs.
- I have the **3.13.1 python version** installed on my system. I will install the required version of python using **pyenv**.

- ## SOLUTION:

1. ### First, install **pyenv** using the following command:

- For MacOS/Linux:

  ```bash
  brew install pyenv

  ```

- For Windows:
  First open the command prompt as administrator then run the following command:

  1. Install Chocolatey

     ```powershell
     Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.SecurityProtocolType]::Tls12; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))

     ```

  2. Install pyenv using Chocolatey:

     ```powershell
     choco install pyenv

     ```

  3. Verify the installation:
     ```powershell
     pyenv --version
     ```

2. #### Now Install Python Version 3.12.8 using pyenv:

- **For MacOS/Linux**:
  ```bash
  pyenv install 3.12.8
  ```
  - Run this command in your project directory:
    ```bash
    pyenv local 3.12.8
    ```
- **For Windows**:
  ```powershell
  pyenv install 3.12.8
  ```
  - Run this command in your project directory:
    ```powershell
    pyenv local 3.12.8
    ```

3. ### Now Install pyenv-vitualenv
   - **For MacOS/Linux**:

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

- **For windows**:

  1.  ### Navigate to the project directory

  2.  ### Run the following command in the command prompt:
      ```powershell
      pyenv local 3.12.8
      ```
      This will set the local Python version to 3.12.8. in your project directory.
  3.  ### verify
      ```powershell
      pyenv version # This should show Python 3.12.8
      ```
  4.  ### Create the virtual environment
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
Test change
