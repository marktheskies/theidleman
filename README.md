# TheIdleMan.com

TheIdleMan.com is a fictional website for TheIdleMan, a clothing retailer targeted at young men. This site has been created for the purposes of education by students of Curtin.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

You'll need to ensure that you have python 3 installed on your system. You can check which version you have by running the following command.

```
python --version
```

If Python 3 is not installed, install Python at https://www.python.org/downloads/.

### Installing

First, clone the repo to your local machine.

```
git clone https://github.com/marktheskies/theidleman.git
```

Then, set up a virtual environment to ensure that we don't install Django to the system's Python. The following command uses Python 3's virtualenv module to create a virtual environment in the folder `venv/` and activates it.

```
python3 -m virtualenv venv
source venv/bin/activate
```

Next, install the required Python packages to your virtual environment.

```
pip install -r requirements.txt
```

Then, run the migrations to prepare the application's database. Note that we will be using Sqlite in the development environment.

```
python manage.py migrate
```

Next, install the frontend deps such as Bootstrap.

```
yarn
# OR
npm install
```

Finally, test your setup by starting up the Django development server.

```
python manage.py runserver
```

### Editing styles with SASS

To make updates to the sites styles, you'll need to update its SASS stylesheet and compile the changes. The easiest way is to have SASS watch for changes.

First, install SASS to your machine if needed.

```
yarn global install sass
# OR
npm -g install sass
```

Finally, start a process to compile CSS on the fly. This will take the SCSS from `core/static/scss` and compile it down to browser-readable CSS in `core/static/css`.

```
sass --watch core/static/scss:core/static/css
```

## Running the tests

TODO: Document the testing process

### Break down into end to end tests

TODO: Explain what these tests test and why

```
Give an example
```

### And coding style tests

TODO: Explain what these tests test and why

```
Give an example
```

## Deployment

TODO: Document production deployment steps

## Contributing

To make a contribution to the codebase, start by creating a branch based on the feature that you are working on.

```
git checkout -b some-feature-name
# For example...
# git checkout -b customer-checkout
```

Make your changes and commit them. Please add a good description.

```
git add filethatyouchanged.html someothernewfile.png
git commit -m "A description of what you did"
git push
```

Finally, create a pull request for your branch. During our sprint review, we will use this to merge your changes into the main branch. For information on how to create a pull request, see https://docs.github.com/en/free-pro-team@latest/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request.

## Authors

As you contribute to the codebase, please add your name and role to this list.

* **Mark Harris** - *Backend/Frontend Developer*
