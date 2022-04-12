# SARP Lessons

This repository holds the Jupyter notebooks that were used for instruction during the [NASA SARP summer internship](https://www.nasa.gov/centers/ames/earthscience/programs/airbornescience/studentairborneresearchprogram).

## Organization
The content is organized into a few folders:
1. `lessons` - notebooks used in an organized lecture format.  Each one also has practice problems
2. `additional_lectures` - supplemental notebooks used throughout the summer for quick code talks.  No practice problems
3. `snippets` - useful pieces of code that were written to support student project, but aren't always organized well or consistently commented
4. `language_agnostic_content` - PDFs that were used to teach coding concepts broader than just sytnax

## Getting Setup (Student)

_Instructions and environment for building the docs are in the `docs/` folder_

If you are running this on a SARP laptop then great news - you are already set up! If you are getting set up on a personal computer you can follow the steps below to create a coding environment there.

1. Install Anaconda 
Go to the [Anaconda website](https://docs.anaconda.com/anaconda/install/index.html), find your operating system, and follow the instructions. This step puts a version of Python on your computer that you will use for analysis. Anaconda is also an environment manager and a package manager.

2. Configure your base environment
**Part A**
Add conda-forge as an anaconda channel and set it as the default
```
conda config --add channels conda-forge
conda config --set channel_priority strict
```

**Part B**
Install jupyter lab, as well as an additional library that allows juptyer lab to see other conda environments on your system.
```
install -n base nb_conda_kernels
install -n base -c conda-forge jupyterlab
```

3. Create a work environment
From the root of this repository, run the command:
```
conda env create -f environment.yml
```
This will create a new enviornment called `sarp` with all the packages that are used in this repository in it. It may take several minutes for the dependencies to solve.


## Opening your work environment
From a new command line window (or your **base** conda environment) run:
```
jupyter-lab
```
A new Jupyter Lab session should open! When prompted to choose an enviroment, or anytime you create a new notebook,  select `Python [conda env:sarp]` as the kernel.

Happy coding!
