FROM python:3.7.4

ENV DJANGO_SETTINGS_MODULE core.settings
ENV PYTHONPATH /usr/src/gdemo_django

COPY --chown=8000:8000 / /usr/src

RUN pip install -r /usr/src/requirements.txt
