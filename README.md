# Gdemo - A demo site for GstackProject

## Development Setup

### Requirements

This guide was written for Linux development, tested on Ubuntu 18.04.
You will need `python3`, `docker-ce`, `direnv` and `openssl` installed.
Your user has to be able to run `docker` commands, i.e. you have to
be the member of the `docker` group.

### Steps to set up a the environment

- Clone the repo.
- After first entering the project directory
  you will need to allow `direnv` to use the `.envrc` file.
  Just run

  ```sh
  direnv allow
  ```

- Set up the python virtual environment in the project directory:
  ```sh
  pip install --upgrade pip && pip install -r requirements.txt
  ```

At this point you are able to call the `invoke` command. Make sure

### `.env` file

In development all environment variables and secrets can be set in the `.env` file in the project root directory.

| variable/secret | description |
| --------------- | ----------- |
| HOST_NAMES      |             |

### SSL certificates for development

From the root directory run

```sh
config/ssl/generate.py
```

Install the `ssl_CA.crt` in the browser.

### The `files` folder

Django stores user uploaded files in this folder. Nginx also needs to be able to read these files to be able to serve them.
In order for the permissions to be correct we set the setgid bit and change the owner/group owner of this directory as follows:

```sh
mkdir -p files && sudo chown 8000:101 files && sudo chmod 2750 files
```

### Docker build
