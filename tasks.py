import os

from invoke import task


os.environ.update({"UID": str(os.getuid())})


@task
def init(c):
    c.run(
        "docker-compose run --rm frontend yarn install",
        # env={"UID": str(os.getuid())},
        pty=True,
    )


@task
def build(c):
    c.run(
        "docker-compose run --rm frontend node_modules/.bin/webpack --mode development",
        pty=True,
    )
