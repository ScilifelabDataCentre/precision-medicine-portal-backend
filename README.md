**Important: The Backend is currently not used in the portal. It is a work in progress and will be used in the future once features requiring backend functionality are needed.**

# Precision Medicine Portal (Backend)

The Precision Medicine Portal is a national resource developed and maintained by SciLifeLab Data Centre. It is intended to serve as a resource for professionals in the field of precision medicine, and content will be added continuously.

The portal supports researchers in precision medicine by providing information on available datasets, including national quality registries, research cohorts, and other structured data relevant to clinical and translational research. Moreover, it provides links to customised dashboards and resources for navigating data management challenges. Researchers can also find guidance on handling sensitive data.

## Table of Contents

- [Background](#background)
- [Cite this portal](#cite-this-portal)
- [Contributing](#contributing)
- [How to get help](#how-to-get-help)
- [Credits](#credits)
- [Development](#development)
  - [Architecture Overview](#architecture-overview)
  - [Running a local copy of the portal](#running-a-local-copy-of-the-portal)

## Background

The [Data Driven Life Science](https://www.scilifelab.se/data-driven/) (DDLS) initiative has appointed four [Data Science Nodes](https://www.scilifelab.se/news/ddls-data-science-nodes-to-be-launched/) (DSNs) to serve as database, data and bioinformatics support for data driven research in life science. This repository contains the code for the backend of a Precision Medicine Portal by the Precision Medicine DSN, which is hosted at [Karolinska Institutet](https://ki.se/en) and [SciLifeLab](https://www.scilifelab.se).

The portal is one of our main projects. Other projects the team has been or is involved in are presented on the portal.

## Cite this portal

Click on 'Cite this repository' near the top right of this repository to see how to formally cite this repository. Also see the [citation and license](https://precision-medicine-portal.scilifelab.se/citation-and-license) site for detailed information.

## Contributing

We welcome contributions, small and large, to our codebase, dashboards and documentation. They will be published after review and approval by the Precision Medicine Portal team. Fork, open a pull request, or contact us to discuss ideas!
Information on the technical details of the portal can be found in the [development](#development) section.

## How to get help

If you have any questions regarding any of the code or content associated with the portal, please get in touch by emailing us at [precisionmedicine@scilifelab.se](mailto:precisionmedicine@scilifelab.se).

## Credits

The website was built and is maintained by a team at SciLifeLab Data Centre and Karolinska Institutet. We are grateful to many collaborators for their contributions.

## Development

### Architecture Overview

This repository contains the backend API for the Precision Medicine Portal built with the following architecture, technologies, and tools:

#### Core Technologies

- **Framework**: Flask (Python web framework)
- **Language**: Python 3.x
- **Database**: SQLite with SQLAlchemy ORM
- **Database Migrations**: Alembic

#### Backend Architecture

- **API**: RESTful API endpoints
- **Authentication**: JWT-based authentication system
- **Data Models**: SQLAlchemy models for articles and other entities
- **Validation**: Pydantic-like schema validation
- **Security**: Password hashing and JWT token management

#### Key Features & Libraries

- **Database**: SQLAlchemy for ORM and database operations
- **Migrations**: Alembic for database schema versioning
- **Security**: JWT tokens, password hashing with werkzeug
- **API**: Flask-RESTful for API endpoint management
- **Validation**: Custom schema validation system

#### Development Tools

- **Package Management**: pip with requirements.txt
- **Containerization**: Docker with multi-stage builds
- **Database**: SQLite for development, configurable for production

#### Project Structure

```
precision-medicine-portal-backend/
├── app.py              # Main Flask application
├── db.py               # Database configuration and setup
├── models/             # SQLAlchemy data models
├── resources/          # API endpoint resources
├── schemas.py          # Data validation schemas
├── security.py         # Authentication and security utilities
├── utils/              # Utility functions
├── migrations/         # Alembic database migrations
└── requirements.txt    # Python dependencies
```

### Running a local copy of the portal and contributing to the codebase

#### Step 1: Fork and clone the repository

**Important**: You must work through a fork of the repository. Do not commit directly to the main repository.

1. Fork the repository: Click the "Fork" button at the top right of the [main repository page](https://github.com/ScilifelabDataCentre/precision-medicine-portal-backend) to create your own copy.

2. Clone your fork: Clone your forked repository to your local machine:

   ```bash
   git clone https://github.com/YOUR_USERNAME/precision-medicine-portal-backend.git
   ```

3. Add the upstream remote: Add the original repository as an upstream remote to keep your fork updated:
   ```bash
   git remote add upstream https://github.com/ScilifelabDataCentre/precision-medicine-portal-backend.git
   ```

Please note that we require all commits to be verified, so you must sign your commits. For information on how to set this up, see the GitHub documentation [here](https://docs.github.com/en/authentication/managing-commit-signature-verification/signing-commits).

Fetch changes at any time from this remote:

```bash
git pull upstream dev
```

#### Step 2: Set up your development environment

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
python3 app.py
```

You will see that a local development server starts running. You can access the API by opening a web browser and visiting the URI "localhost:5000". To stop the server press CTRL+C in the terminal.

##### Docker

You can use the provided Dockerfile to build and run a container.

#### Step 3: Create a branch and develop

Please note that we require all commits to be verified, so you must sign your commits. For information on how to set this up, see the GitHub documentation [here](https://docs.github.com/en/authentication/managing-commit-signature-verification/signing-commits).

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

The code is now in your branch on your fork, but it does not get merged into the main repository without being reviewed as a pull request.

#### Step 4: Make a pull request

Once you're finished with your edits and they are committed and pushed to your branch, it's time to open a pull request from your fork to the main repository.

You can find full documentation on the [GitHub help website](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/about-pull-requests). In short:

- Visit your fork: `https://github.com/YOUR_USERNAME/precision-medicine-portal-backend`
- Find the branch `my_branch` that you created and pushed to
- Click the button that reads _"New Pull Request"_
- GitHub will automatically detect that you want to create a pull request to the upstream repository
- Add/change title as well as a description of what you've done
- Add reviewers from the organization to review your pull request
- Click Create Pull Request

Once created, a member of our team will review your changes and reach out to you if they have any questions or requests for changes.
Once approved, they will be merged and deployed in the next release.
