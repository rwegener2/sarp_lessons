# SARP Lessons

This repository holds the less content that is used for instruction during the [NASA Student Airborne Research Program (SARP)](https://www.nasa.gov/centers/ames/earthscience/programs/airbornescience/studentairborneresearchprogram)  summer internship.

## Organization
The content is organized into a few folders:
1. `lessons` - notebooks used in an organized lecture format.  Each one also has practice problems
2. `additional_lectures` - supplemental notebooks used throughout the summer for quick code talks.  No practice problems
3. `snippets` - useful pieces of code that were written to support student project, but aren't always organized well or consistently commented
4. `language_agnostic_content` - PDFs that were used to teach coding concepts broader than just sytnax

## Environments

The `environment.yml` file in the root directory builds an enviroment that can be used to execute the notebooks. There is not currently an environment.yml for building the docs, but one could be make by starting with the student environment.yml environment and then adding `conda install -c conda-forge jupyter-book`.  You may also need to install some sphinx extensions. 

## Getting Setup (Student)

_Instructions and environment for building the docs are in the `docs/` folder_

If you are running this on a SARP laptop then great news - you are already set up! If you are getting set up on a personal computer you can follow the steps below to create a coding environment there.

1. Install Anaconda 
Go to the [Anaconda website](https://docs.anaconda.com/anaconda/install/index.html), find your operating system, and follow the instructions. This step puts a version of Python on your computer that you will use for analysis. Anaconda is also an environment manager and a package manager.

2. Configure your base environment
**Part A**
Add conda-forge as an anaconda channel.
```
conda config --add channels conda-forge
```

**Part B**
Install jupyter lab, as well as an additional library that allows juptyer lab to see other conda environments on your system.
```
conda install -n base nb_conda_kernels
conda install -n base -c conda-forge jupyterlab
```

After installing the two packages above, you can set `conda-forge` to be your default channel.
```
conda config --set channel_priority strict
```
_Note: You could do this step right after adding `conda-forge` as a channel, but some issues have been reported due to `nb_conda_kernels` using the Conda Forge installation in this case. The safest route is to set the channel priority after installing `nb_conda_kernels` and `jupyterlab`._

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

# Developer Notes
## Running the book
* `conda activate sarp_docs`
* `jupyter-book build .` from root
* `python -m http.server --directory _build/html/`

## Deploy
[link](https://jupyterbook.org/start/publish.html#publish-your-book-online-with-github-pages)
1. Build book
`jupyter-book build .`
2. trigger the ghp-import utility to do its magic
`ghp-import -n -p -f _build/html`
