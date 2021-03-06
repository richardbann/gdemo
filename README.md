## Development Setup

### Create a python virtual environment

To create the virtual environment run
```sh
make init
```
For this to work the `python3` command should be available in your system.
On ubuntu the `python3-venv` package should be installed.


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