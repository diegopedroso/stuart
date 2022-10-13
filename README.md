# Stuart API demo

This document describes a Stuart platform REST-API, with the complete code stack, tests, automation and multi-environment scalable deployment within Kubernetes.


### Dependencies

* python 3
* docker-cli
* kubectl

## Install the setup

To reproduce the local setup:

```bash
poetry install
poetry shell
```

## CLI

```bash
stuart --help

Usage: stuart [OPTIONS] COMMAND [ARGS]...

  Stuart Couriers Application

Options:
  --install-completion [bash|zsh|fish|powershell|pwsh]
                                  Install completion for the specified shell.
  --show-completion [bash|zsh|fish|powershell|pwsh]
                                  Show completion for the specified shell, to
                                  copy it or customize the installation.
  --help                          Show this message and exit.

Commands:
  add-parameters  Adds new Couriers Parameters
  list            Lists Couriers Parameters from the database
```

```bash
stuart add-parameters --max-capacity 30
🏍 New Couriers Capacity Added 🚚
```

```bash
stuart list

Stuart Couriers informations (in liters).
┏━━━━┳━━━━━━━━━━━━━━┓
┃ id ┃ max_capacity ┃
┡━━━━╇━━━━━━━━━━━━━━┩
│ 1  │ 30           │
│ 2  │ 100          │
│ 3  │ 50           │
│ 4  │ 30           │
│ 5  │ 40           │
│ 6  │ 50           │
└────┴──────────────┘
```

## API


Exemple to POST Couriers capacity using API: 

```bash
curl -X 'POST' \
  'http://localhost:8000/stuart' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "max_capacity": 100
}'
```

Exemple to GET Couriers capacity using API:

```bash
curl -X 'GET' \
  'http://localhost:8000/capacity_required?max_capacity=10' \
  -H 'accept: application/json'
```

Exemple to UPDATE Couriers capacity using API:

```bash
curl -X 'PUT' \
  'http://localhost:8000/update_capacity/2' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "max_capacity": 19
}'
```

# API Documentation

http://localhost:8000/docs

## Tests

```bash
pytest -v

collected 6 items                                                                                                                                                                                   

tests/test_core.py::test_add_event_source PASSED                                                                                                                                              [ 16%]
tests/test_core.py::test_get_event_source PASSED                                                                                                                                              [ 33%]
tests/test_functional_api.py::test_create_event_via_api PASSED                                                                                                                                [ 50%]
tests/test_functional_api.py::test_update_event_via_api PASSED                                                                                                                                [ 66%]
tests/test_functional_api.py::test_list_events PASSED                                                                                                                                         [ 83%]
tests/test_functional_cli.py::test_add_parameters PASSED                                                                                                                                      [100%]

```
# Build and Deploy



```bash
docker build -t stuart-api:v1 -f docker/Dockerfile .
sed -i "s/stuart-api:v1/$DOCKER_IMAGE/g" kubernetes/deployment.yaml
kubectl apply -f kubernetes/
```

The Kubernetes will deploy:

- Namespace - Isolate the stuart application
- Resource Quota - Secure resources
- Deployment - Application configuration
- Service - Expose the service
- HPA - Escale the service