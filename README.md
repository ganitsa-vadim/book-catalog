# Book catalog

## Configuration

* Project uses `.env` file or environment variables for configuration. There is an example: `book_catalog/bool_catalog/.env.example`.

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


#### Run API

`make run` - runs django application.

`make migrate` executing migration.

`make shell` runs django shell.

### Lint

`make lint` - runs configured linter.

### Clean

`make clean` - removes everything, except source code.

### Documentaion

`http://127.0.0.1:8000/swagger/` - open swagger documentation.

