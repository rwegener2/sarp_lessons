# SARP Lessons

This repository holds the Jupyter notebooks that were used for instruction during the [NASA SARP summer internship](https://www.nasa.gov/centers/ames/earthscience/programs/airbornescience/studentairborneresearchprogram).

## Organization
The content is organized into a few folders:
1. `lessons` - notebooks used in an organized lecture format.  Each one also has practice problems
2. `additional_lectures` - supplemental notebooks used throughout the summer for quick code talks.  No practice problems
3. `snippets` - useful pieces of code that were written to support student project, but aren't always organized well or consistently commented
4. `language_agnostic_content` - PDFs that were used to teach coding concepts broader than just sytnax

## Environments

The `environment.yml` file in the root directory builds an enviroment that can be used to execute the notebooks. There is not currently an environment.yml for building the docs, but one could be make by starting with the student environment.yml environment and then adding `conda install -c conda-forge jupyter-book`.  You may also need to install some sphinx extensions. 

# Developer Notes
## Running the book
`conda activate sarp_docs`
`jupyter-book build .` from root
`python -m http.server --directory _build/html/`

## Deploy
[link](https://jupyterbook.org/start/publish.html#publish-your-book-online-with-github-pages)
