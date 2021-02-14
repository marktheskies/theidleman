# TheIdleMan.com

TheIdleMan.com is a fictional website for TheIdleMan, a clothing retailer targeted at young men. This site has been created for the purposes of education by students of Curtin.

## Local Development

Follow these steps to set up a development environment and start working.

### Prerequisites

Before you start, make sure you have the following installed.

- [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)
- [Git](https://git-scm.com/downloads)
- [Virtualenv](https://pypi.org/project/virtualenv/)

### 1. Clone the repo and configure git Heroku integration

```
git clone https://github.com/marktheskies/theidleman.git
cd theidleman
heroku git:remote -a theidleman
```

### 2. Setup environment variables

Create a file called `.env` in the same folder as `manage.py`, then copy the contents of `.env.example` into it. Update `SECRET_KEY`, `DEBUG`, and `CLOUDINARY_URL` as appropriate.

To find the Cloudinary URL from production, run:

```
heroku config
```

### 3. Setup virtualenv with Python 3.8

On Linux/MacOS:

```
virtualenv -p python3.8 venv
source venv/bin/activate
pip install -r requirements.txt
```

On Windows:

```
virtualenv -p python3.8 venv
venv\Scripts\activate
pip install -r requirements.txt
```

### 4. Run database migrations

```
heroku local:run python manage.py migrate
```

### 5. Install package.json dependencies

```
yarn install
```

### 6. Start the development server

```
heroku local
```

## Production Deployment

To deploy code from the main branch to production, run:

```
git push heroku main
```

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

- **Mark Harris** - _Backend/Frontend Developer & Initial Setup_
- **Jessica Matterson-Jones** - _Frontend Developer_
- **Scott Lockett** - _Information Architect/UX/Front-End/Project Manager_
- **Honorata Trojanowska** - _Backend Developer_
