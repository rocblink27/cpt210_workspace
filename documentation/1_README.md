# CPT210_Workspace
>Version 1.0  
>Date: Fall 2025
---
## Introduction
This document explains how the CPT-210 workspace is structured and how to use it effectively within Visual Studio Code (VS Code) during the semester.

Visual Studio Code is a lightweight, extensible code editor that supports a wide range of programming languages and development tools. In this course, VS Code will serve as your Integrated Development Environment (IDE), allowing you to write, organize, and manage your code on a remote Raspberry Pi 5. VS Code supports both C and Python programming.

In VS Code, a workspace is a container that groups together related files, folders, and settings — in this case, all the components you'll need to complete your lab assignments. The workspace provided in this repository is pre-configured to help you stay organized, reuse code efficiently, and build projects consistently.



## What This Document Is Not

This document does not provide installation instructions for Visual Studio Code (VS Code) or detailed documentation about how to use VS Code itself. It assumes that you already have VS Code installed and configured on your computer.

If you need help installing VS Code or configuring Remote SSH, please refer to the official Microsoft documentation or the setup guides provided in the course.

For official VS Code installation instructions, see:  
[https://code.visualstudio.com/docs/setup/setup-overview](https://code.visualstudio.com/docs/setup/setup-overview)  

For Remote SSH extension details, see:  
[https://code.visualstudio.com/docs/remote/ssh](https://code.visualstudio.com/docs/remote/ssh)

## Hardware
This workspace is developed specifically for the Raspberry Pi 4 or 5 Single Board Computer.

The Raspberry Pi Single Board Computer is essential for the course's development exercises. They provide a hardware platform for interacting with the microprocessor and facilitating input/output operations.

It is assumes the following system information for the Raspberry Pi
- OS: Raspberry Pi OS Bookworm 64-bit
- Kernel: Linux 6.12.20+rpt-rpi-2712 (SMP PREEMPT)
- Architecture: aarch64 (ARM64)
- libgpiod version: 1.6.3


## Setting up Project for CPT-210 Lab Assignments

This workspace contains a default project called **"Default_project"**. This project contains a template file that can be used to start writing your code. The **"Default_project"** should **not** be edited directly. Instead, you should create a **copy** of this project to avoid making changes to the original files.

### Steps to Duplicate the Project and Rename It

1. **Duplicate the Default Project:**
   - Right-click on the **"Default_project"** in your VS Code workspace.
   - Select **"Duplicate"** from the context menu.
   - This will create a copy of the project, leaving the original untouched.

2. **Rename the Project:**
   - After duplicating the project, right-click on the new copy and select **"Rename"**.
   - Rename the project to an appropriate name for your lab. For example, if you're working on **Lab 2**, rename the project to **"Lab2"**.
   
3. **Rename the main.py File:**
   - In your newly duplicated project, find the **main.py** file.
   - Right-click on **main.py** and select **"Rename"**.
   - Rename the file to **lab2_part3.c** (or a similar name corresponding to your project).
   
### Why Rename the Project and main.py?

- **Avoid Confusion**: When working on multiple projects or labs, having **unique names** for each project and **main.py** file ensures that you don't accidentally edit the wrong file or project.
- **Better Organization**: Renaming the file helps keep your workspace organized, especially as you move through different labs or assignments.
<br> </br>

## Contact Information
Bruce Link  
Monroe Community College  
Information & Computer Technologies Department  
blink@monroecc.edu


