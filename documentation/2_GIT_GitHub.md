# Configuring VS Code and GitHub
>Version 1.0  
>Date: Fall 2025
---
## Introduction
To fully integrate Visual Studio Code (VS Code) with Git and GitHub, you will push your local repository from your machine to GitHub. Below are instructions for pushing and pulling files to/from GitHub.

### Configure Git Global Configurations

Before you can use Git, you must define your global user information. This is necessary because Git tracks your identity for every commit you make. Setting up this configuration ensures that each commit has the correct author information attached to it.

 **Open a new terminal in VS Code**
1. Enter the following command to set your e-mail address
   - `git config --global user.email "{your-email-address}"`
     - Ensure that you replace the `{your-email-address}` with your e-mail address.
     - This email is associated with your commits and important for identifying authorship.

   
2. Enter the following command to set your username
   - `git config --global user.name "{your-name}"`
     - Ensure you replace the `{your-name}` with your name.
     - This sets the name that will be associated with your commits. This helps identify who made the changes, which is especially useful for collaboration in shared repositories.

Using the --global flag applies this configuration to every repository on your system. You can override these settings on a per-repository basis by omitting --global and running the commands inside a specific repo folder.


### Pushing from VS Code to GitHub

Once you have created a repository on your local machine using VS Code, you must connect it to a remote repository on GitHub. You only need to set up this connection once, and VS Code will remember it for future use.

 **Open a new terminal in VS Code**

1. Configure your Git global configurations for user name and email, if they aren't already configured.

2. Connect your local repository to the remote repository on GitHub by running this command (replace `{your-git-hub-username}` and `{name-of-repo}` with your actual GitHub username and repository name):
   - `git remote add origin https://github.com/{your-git-hub-username}/{name-of-repo}.git`

3. Push your local repository to GitHub:
   - `git push -u origin main`

    The `-u` flag in the `git push` command stands for **"upstream"**. It tells Git to remember the remote repository (in this case, `origin`) and the branch (in this case, `main`) that you're pushing to. This establishes a tracking relationship between your local and remote branches, simplifying future Git commands.

**NOTE:** Do not create files directly on GitHub before pushing your local repository. If you do, GitHub will create a branch called `main`. This can cause confusion and result in two branches when you push from your local machine.

### Pulling from GitHub to a New VS Code Setup

If you have an existing repository on GitHub and want to work on it from a different machine (e.g., a new PC or a work/school computer), you'll need to pull the repository from GitHub to your new machine. Follow these steps to set up the repository on your new computer and access your files:

1. **On the new machine**, create a folder where you want to store the repository. This will serve as the location for the files you pull from GitHub.

2. **In VS Code**, open the newly created folder to make it your workspace. This sets up your environment for the new project.

3. **In the Source Control tab**, initialize the local repository to setup Git for the workspace.

4. **Open a new terminal in VS Code** and issue the following commands:
   - Git Global Configurations, if they aren't already configured on the new machine.
   - Add the GitHub repository as the remote origin (replace `{your-git-hub-username}` and `{name-of-repo}` with your actual GitHub username and repository name):
     - `git remote add origin https://github.com/{your-git-hub-username}/{name-of-repo}.git`
   - Pull the latest changes from the GitHub repository to your local machine.:
      - `git pull origin main`

This will download the latest repository version from GitHub to your local machine, so you can start working on it in VS Code.
<br> </br>

## Contact Information
Bruce Link  
Monroe Community College  
Information & Computer Technologies Department  
blink@monroecc.edu


