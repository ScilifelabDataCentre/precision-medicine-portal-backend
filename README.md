# Precision Medicine Portal

This is the source code for the DDLS Data Science Node Precision Medicine Portal:
(Link to be added).

- [Introduction](#introduction)
- [Development](#development)
    - [Step 1: Clone the repository](#step-1-clone-the-repository)
    - [Step 2: Create a branch and develop](#step-2-create-a-branch-and-develop)
    - [Step 3: Make a pull request](#step-3-make-a-pull-request)

## Introduction

The [Data Driven Life Science](https://www.scilifelab.se/data-driven/) (DDLS) initiative has appointed four [Data Science Nodes](https://www.scilifelab.se/news/ddls-data-science-nodes-to-be-launched/) (DSNs) to serve as database, data and bioinformatics support for data driven research in life science. This repository contains the code for a Precision Medicine Portal by the Precision Medicine DSN, which is hosted at [Karolinska Institutet](https://ki.se/en) and [SciLifeLab](https://www.scilifelab.se).

The short term aim of this portal is to host static content related to precision medicine as a starting point for the project.


### Step 1: Clone the Repository

#### Git setup

Clone the repository to your machine:

```bash
git clone https://github.com/ScilifelabDataCentre/precision-medicine-portal.git
```

To make it easier to pull in changes made by others, you can add the main repository as a remote:

```bash
git remote add upstream https://github.com/ScilifelabDataCentre/precision-medicine-portal.git
```

Then you can fetch changes at any time from this remote:

```bash
git pull upstream dev
```

The required packages and their versions are logged in the file "requirements.txt". It is recommended to set up a virtual environment of your choice (for example [venv](https://docs.python.org/3/library/venv.html)) for the project, to handle versioning of Python and required packages. 

To set up a venv on MacOS or Linux (might differ slightly on Windows):

```bash
python3 -m venv .venv
```

To activate the venv:

```bash
source .venv/bin/activate 
```

Once you have set that up, install requirements using pip:

```bash
pip install -r requirements.txt
```

With the requirements installed you can then run the flask app locally for testing purposes:

```bash
python3 run.py
```

You will see that a local development server starts running. You can access the web page by opening a web browser and visiting the URI "localhost:5000". To stop the server press CTRL+C in the terminal.


#### Docker

You can use the provided Dockerfile to build and run a container.


### Step 2: Create a branch and develop

Note that commits need to be signed as per SciLifeLab policy. There are many different ways to sign github commits and how to set it up may vary based on your operating system. An example of how to set it up for MacOS can be seen here: 

https://gist.github.com/troyfontaine/18c9146295168ee9ca2b30c00bd1b41e

To create a new branch and start developing in it:

```bash
git branch my_branch
git checkout my_branch
```

After doing this you can make any changes you want. You must then either add all changed files or specific changed files to your commit:

```bash
git add -A
```

or

```bash
git add my_changed_file
```

You can then commit and push to your branch:

(NOTE: DO NOT FORGET TO SIGN YOUR COMMITS, by policy only signed commits can be merged into the main branches.)

```bash
git commit -S -m "My commit"
git push origin my_branch
```

The code is now in my_branch in the repository, but you it does not get merged into the main branches without being reviewed as a pull request.


### Step 3: Make a pull request

Once you're finished with your edits and they are committed and pushed to your branch, it's time to open a pull request.

You can find full documentation on the [GitHub help website](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/about-pull-requests), however in short:

- Visit the main repository: [https://github.com/ScilifelabDataCentre/data.scilifelab.se](https://github.com/ScilifelabDataCentre/data.scilifelab.se)
- Find the branch my_branch that you created and pushed to
- Click the button that reads _"New Pull Request"_
- Add/change title as well as a description of what you've done
- Add reviewers from the organization to review your pull request
- Click Create Pull Request

Once created, a member of the website team will review your changes.
Once approved, they will be merged and deployed.

## How to get help

If in doubt, you can ask for help by emailing [datacentre@scilifelab.se](mailto:datacentre@scilifelab.se).

## Credits

The portal was built by the DDLS Precision Medicine Data Science Node with colleagues at SciLifeLab.
