# Mind Map API

We want you to design a [mind map](https://en.wikipedia.org/wiki/Mind_map) web service.

Your service must provide REST API endpoints to create a mind map and store its data in a backend.

Your solution must be written in **Python**.

## Requirements

The provided `./bin/run.sh` script must be enough to build and / or start the REST API.

Please give us your final version in a Git repository (github, gitlab, ...).

We expect that you provide at least:

* Unit tests (min coverage: 30%).
* Persistence: data can be saved in file(s).

If you need support, feel free to contact us.

## Review

These are some of the things my colleagues will be looking at when reviewing your test:

* The API should conform to the specifications (correct endpoints and it should work).
* Focus on code quality before starting bonus requirements.
* Don’t reinvent the wheel, use best practices, use the right tool for the job.
* Your REST API has to start easily without errors (you can provide us a README file to explain how to start it).

## Specifications

### Create a mind map

```bash
curl -X [verb] [something] -H 'content-type: application/json' -d '{"id": "my-map"}'
```

### Add a leaf (path) to the map

```bash
$ curl -X [verb] [something] \
  -H 'content-type: application/json' \
  -d '{
    "path": "i/like/potatoes",
    "text": "Because reasons"
}'
```

### Read a leaf (path) of the map

```bash
$ curl -X [verb] [something] -H 'content-type: application/json'

Expected response:
{
    "path": "i/like/potatoes",
    "text": "Because reasons"
}
```

### Pretty print the whole tree of the mind map

```bash
$ curl -X [verb] [something] 

Expected output:
root/
    i/
        like/
            potatoes
        eat/
            tomatoes
```

## BONUS Requirements

If you have time, feel free to add improvements.

Here are some ideas:

* Unit tests coverage to 75%.
* If not already done, a nice storage backend (SQL Database, ...).
* Docker image.
* Pipeline to build the docker image, execute the unit tests (example, github + travis CI).
* Deployment in a Cloud service (Heroku, GCP AppEngine...)
