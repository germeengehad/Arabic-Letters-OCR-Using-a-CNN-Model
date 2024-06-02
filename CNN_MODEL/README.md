# FastAPI boilerplate

FastAPI template to use for building Python API

## Table of content

- [FastAPI boilerplate](#fastapi-boilerplate)
  - [Table of content](#table-of-content)
  - [Development](#development)
    - [Prerequisites](#prerequisites)
    - [Configuration](#configuration)
    - [Run instructions](#run-instructions)
  - [Docker instructions](#docker-instructions)
    - [For Development](#for-development)
    - [For Production](#for-production)
      - [Build image](#build-image)
      - [Publish image](#publish-image)
      - [Test it](#test-it)
  - [API Details](#api-details)
  
## Development

### Prerequisites

- Python v3.9.12

### Configuration

- Copy [`example.dev.env`](example.dev.env) to `dev.env`

- Adapt `dev.env`

### Run instructions

- Create a virtual environment and install dependencies

```sh
cd api
pip install virtualenv
virtualenv ./env
source env/bin/activate
pip install -r requirements.txt
```

- Load env variables

```sh
# For windows
set -a && source ../dev.env && set +a

# For linux
source dev.env
```

- Start the server

```sh
python src/main.py
```

- Lint src dir

```sh
flake8 src
```

## Docker instructions

### For Development

- Copy [example.dev.env](example.dev.env) to .env file and adapt you variables [See configuration section](#configuration)

- Start development container

```sh
docker-compose -f docker-compose.dev.yml --env-file .env up -d
```

- Connect to it

```sh
docker-compose -f docker-compose.dev.yml --env-file .env exec api /bin/bash
```

- Verify logs file for the api

```sh
docker-compose -f docker-compose.dev.yml --env-file .env logs api
```

### For Production

- Copy [example.env](example.env) to .env file and adapt you variables [See configuration section](#configuration)

#### Build image

```sh
make build
```

#### Publish image

```sh
make publish
```

#### Test it

```sh
docker-compose -f docker-compose.yml up -d
```

## API Details

- [API Details](./api/README.md)
