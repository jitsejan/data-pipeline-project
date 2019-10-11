# Data pipeline project
This project aims to work on different aspects of a data pipeline. It is meant to learn new technologies, but hopefully it also helps other people to get inspired. Note that this repository will (slowly) change and get more functionality.

## Objectives
The fictive story I will base this repository on is Mario, since I like to use a theme to work on my project. I will gather some character data and create events to fake the characters moving through different Mario worlds. To do this I will use Python (code), Kafka (Spark streaming) and minIO (object storage). All other tools will follow during the implementation of this project.

- **Data crawler** to get character data
- **Data connection** with minIO storage
- **Event generator** to create the (fake) events
- **Kafka producer** to put events on the Kafka bus
- **Spark Stream reader** to ingest the events
- **Spark Stream parser** to combine ingested data with the character data
- **Dashboard** to visualize the events

## Setting up virtual environment

I use `pipenv` with Python version 3.7.3 to setup the environment.

```bash
$ pipenv --python=3.7
Creating a virtualenv for this project…
Pipfile: /Users/jitsejan/code/data-pipeline-project/Pipfile
Using /Library/Frameworks/Python.framework/Versions/3.7/bin/python3 (3.7.3) to create virtualenv…
⠸ Creating virtual environment...Using base prefix '/Library/Frameworks/Python.framework/Versions/3.7'
New python executable in /Users/jitsejan/.local/share/virtualenvs/data-pipeline-project-DUniwI99/bin/python3
Also creating executable in /Users/jitsejan/.local/share/virtualenvs/data-pipeline-project-DUniwI99/bin/python
Installing setuptools, pip, wheel...
done.
Running virtualenv with interpreter /Library/Frameworks/Python.framework/Versions/3.7/bin/python3

✔ Successfully created virtual environment!
Virtualenv location: /Users/jitsejan/.local/share/virtualenvs/data-pipeline-project-DUniwI99
Creating a Pipfile for this project…
$ pipenv shell
Launching subshell in virtual environment…
 . /Users/jitsejan/.local/share/virtualenvs/data-pipeline-project-DUniwI99/bin/activate
```

## Installing libraries
Note that `pipenv install` should be used rather than `pip` or `pip3` install when using `pipenv`.

```bash
$ pipenv install lxml
Installing lxml…
Adding lxml to Pipfile's [packages]…
✔ Installation Succeeded
Pipfile.lock not found, creating…
Locking [dev-packages] dependencies…
Locking [packages] dependencies…
✔ Success!
Updated Pipfile.lock (b70304)!
Installing dependencies from Pipfile.lock (b70304)…
  🐍   ▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉ 1/1 — 00:00:01
```

## Testing code
The following will run the tests and the coverage check simultaneously. 

```bash
$ pytest --cov=. -v 
```

Convert the results to HTML for better visiblity on the coverage results.

```bash
$ coverage html
$ open htmlcov/index.hml
```


## Minio

https://docs.min.io/docs/python-client-api-reference.html
