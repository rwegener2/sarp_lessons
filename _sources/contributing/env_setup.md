# Contributing to SARP Lessons

## Set up the docs environment locally

This repo can be cloned from github using the clone url:

```bash
git clone https://github.com/rwegener2/sarp_lessons.git
```

This copies the files from Github to your local computer.

To build this website you'll need an environment seperate from the environment used
by the students. You'll need additional libraries only necessary for development, such as [Jupyter Book](https://jupyterbook.org/en/stable/intro.html), which automatically complies jupyter notebooks into nicely formatted web pages.

To install an environment with the required developer dependencies run the following from the root folder:

```bash
conda env create -f developer_env.yml
```

This will create an environment called `sarp_docs` for building and updating the website. It can be activated with `conda activate sarp_docs`.

(Also, if you're not using [mamba](https://mamba.readthedocs.io/en/latest/) yet, check it out! It's a great package that really speeds up conda commands.)

## Build the documentation

Once you have an environment created you can build the docs. This website is setup as a series of Jupyter notebooks, which Jupyter Book complies into HTML. After making changes to the Jupyter notebooks you need to re-compile the HTML to create updated website source code.

To build the website HTML use:

```bash
jupyter-book build .
```
After that command has completed a new folder should appear in the root, `_build`, which contains the website HTML files. You can view these files in the browser by running (also from the project root):
```bash
python -m http.server --directory _build/html/
```
This starts a local server by default on port 8000. Go to the browser, type  `localhost:8000` into the url box, and the locally compiled website should appear.

### Development process

You only need to build the environment once, but when making changes to the website you may go through the build process multpile times. A typical cycle after creating the development environment would be:

1. Change the juptyerbook/markdown files with your content
2. Build the HTML
3. Open the server to view the compiled changes
4. Repeat until you're happy with how the new website looks

Once this cycle is complete you are ready to commit your changes.

## Commit changes to Github

Once a new change is made to the repository it can be added to Github. In good development practice, new changes should be make on a [branch](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-branches). Create a new branch with:

```bash
git checkout -b BRANCH_NAME
```

Good branch names are short but provide a hint of the change (ex. `contrib_guide`, `netcdf_lesson`, `formatting_updates`).

Integrating your changes into the repository involves **commiting** them. A nice dive into what the commit command is can be found [here](https://careerfoundry.com/en/blog/web-development/git-commit-command/). The steps to commiting are:

1. See what files have been changed with [`git status`](https://github.com/git-guides/git-status).

`git status` shows all the files that have been changed in the course of your work. These are the options availble for adding (next step).

2. Add each of the relevant files with [`git add FILENAME`](https://github.com/git-guides/git-add).

`git add FILENAME` adds the files to a Staging Area, meaning they are queued up and ready to be commited.

3. Make the final commit with [`git commit -m "COMMIT MESSAGE"`](https://github.com/git-guides/git-commit)

This takes your changes and officially logs them as part of your local repository. The git message will appear on Github as note to other developers what the change did. Examples include "add additional section for HDF files", "update tabular data practice problems" or "fix errors in geospatial data lesson".

Now the changes are in your local website repository, but they aren't yet available on the remote repository. No one else other than you can see them. To move your changes from the local repository to the remote one where it will be publically available we **push**.

```
git push origin BRANCH_NAME
```
At this point you may be prompted to enter your Github username and password. If it is your first time pushing to this branch you may also be prompted to add the `--set-upstream` option. Once the push is successful you should see your branch and the changes on the public repo!: https://github.com/rwegener2/sarp_lessons/branches.

### Pull Request

You can commit and push many times in the development process. Your changes will all stay on your own branch, so they won't be reflected in the `main` source code. To integrate your changes into `main` you create a pull request. I typically do this step in the browser. [This guide](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request) walks through those steps.

### Autodeployment

The website is auto-deployed using Github pages. Github pages uses a [Github Action](https://github.com/features/actions) to build HTML from the Juptyer notebooks and deploy it to the public url. While I believe this can be configured to happen on merge to the repo, right now the deploy command needs to be run manually. For now we can discuss who will deploy in the PR, it can be anyone, not just the person who created the changes.
