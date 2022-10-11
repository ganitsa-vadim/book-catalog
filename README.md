# Book catalog



## Requirements

* python >=3.10, <4.0

## Development

Steps for Development such as setup, linting and testing can be run via `make` commands.

### Setup env and install dependencies

`make setup` - creates virtual environment in `.venv/` folder and installs required packages.

#### Adding new dependencies

For dependencies management [pipenv](https://pipenv.pypa.io/) is being used.

### Run

#### Activate venv

`source .venv/bin/activate`

#### Run

`make run` - runs django application

`make runworker` runs celery worker

`make migrate` executing migration

`make shell` runs django shell
