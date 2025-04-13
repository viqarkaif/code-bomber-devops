# Code Bomber DevOps

**Code Bomber DevOps** is a Python-based project designed to demonstrate fundamental DevOps principles and Git best practices. The project includes proper use of **Git version control**, **branching strategies**, **pull requests**, and clear project documentation. It showcases how to manage code using Git, perform tasks like creating feature branches, using pull requests for code review, and maintaining an organized Git history.

## 🚀 Project Overview

The **Code Bomber DevOps** project is focused on applying **DevOps principles** through version control and Git best practices. The project is structured to demonstrate:

- **Branching strategies**: Including dev, feature, and main branches.
- **Commit best practices**: Writing descriptive and meaningful commit messages.
- **Pull Requests**: Using PRs for code review before merging into the main development branch.
- **Documentation**: Clear project documentation using Markdown.

---

## 🛠️ Tech Stack

- **Git** – Version control system used to track changes in the codebase.
- **GitHub** – Hosting platform for version control and collaboration.
- **Python** – Programming language used for this project.
- **Markdown** – Used for documentation in `README.md`.

---

## ⚙️ Setup and Installation

To set up the **Code Bomber DevOps** project locally, follow these steps:

1. Clone the Repository

Clone the repository to your local machine:
git clone https://github.com/viqarkaif/code-bomber-devops.git

2.Install Python and Dependencies

Since this is a Python-based application, ensure that you have Python installed on your local machine.

  -> Install Python from the official Python website.

  -> Install necessary dependencies using pip (Python’s package manager)

  bash: pip install -r requirements.txt
  Note: The requirements.txt file should contain all the libraries/dependencies required by the application.

3. 🖥️ Running the Application Locally (Windows)
Since this is a CLI-based Python application, it is designed to run in a Command Line Interface (CLI). To run this application locally on Windows, follow these steps:

Step 1: Open Command Prompt or PowerShell
You can do this by typing cmd or PowerShell in the Start menu and opening the respective program.

Step 2: Navigate to the Project Directory
Once you have cloned the repository and installed dependencies, navigate to the project directory.

  bash: cd path\to\your\project\code-bomber-devops
  
Step 3: Run the Python Script
Assuming the entry point is a script called main.py (or any script you have defined), you can run it using.

  bash: python main.py
4. 🌐 Branching Strategy
This project follows the following Git branching strategy:

main: The production-ready branch containing stable code.

dev: The development branch where the integration of features occurs.

feature/: Feature branches for developing new features or bug fixes. Example: feature/login-feature.

To start working on a new feature, create a new branch from dev:

bash: git checkout dev
git pull origin dev
git checkout -b feature/your-feature

📸 Screenshots
Below are some key screenshots showing various stages of the project and workflows.

1. Directory Structure
![Screenshot 2025-04-13 153444](https://github.com/user-attachments/assets/addb9446-3dcf-4656-b00f-6f5b2365760f)


1. Repository Structure
The repository structure includes the main branches like main, dev, and feature branches.
![Screenshot 2025-04-13 162852](https://github.com/user-attachments/assets/ca1054b8-c3cc-4389-9736-c7fe8d12cb2d)


2. GitHub Pull Requests
Shows a pull request open for code review and integration into the dev branch.
![Screenshot 2025-04-13 183215](https://github.com/user-attachments/assets/b4185583-2e59-4ba5-a74d-d2427ed28416)
![Screenshot 2025-04-13 183201](https://github.com/user-attachments/assets/5c780035-b2ca-413a-ba1a-6f87d2398811)


3. Branch Creation
How to create a feature branch for implementing new features.
![Screenshot 2025-04-13 154954](https://github.com/user-attachments/assets/c4f97af5-4016-450e-84c6-25ee8d930779)

5. Commit History
This shows the history of commits made with meaningful commit messages.
