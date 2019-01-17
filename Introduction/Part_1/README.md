# Part 1

## Basic GIT:
### Installing GIT For Windows:
* Navigate to [GIT for Windows](https://gitforwindows.org/) download page.
* Download and walk through install wizard.

### Basic CLI GIT
* Initializing Repository:
	* Create a directory where you would like to store the project.
	* Right click the directory and select "GIT BASH Here".
	* type "git clone https://github.com/theastrocat/PyDS_101_PK.git"

#### Some Basic BASH Syntax for CLI navigation:
`pwd` : Print Working Directory -- Where you currently are in the windows file system.
`ls` : List Directory -- Lists files and sub-folders in your current directory.
`cd` : Change Directory -- Allows you to step into a directory.
> For instance: I can do `cd ..` to step UP one directory from the path displayed in `pwd`
> Or `cd New\ Dir` to step into my directory called "New Dir"
Notes:
* Tab auto-complete is your friend.
* All spaces need to be *escaped* with `\`

## Installing Python 3.7 with Anaconda Suite:
* Navigate to [Anaconda download page](https://www.anaconda.com/download/)
* Click to download and install Python 3.7 for Windows using the installer.
* When prompted please click "Add Anaconda to my PATH environment variable".

## Launching Jupyter:
* Right click inside the directory where this file was cloned to.
* Click GIT BASH Here
* Run `jupyter notebook`
* When they Jupyter Notebook kernel GUI appears in your default web browser, click on `Part_0.ipynb`.
