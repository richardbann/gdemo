FROM python:3.7.4

ENV DJANGO_SETTINGS_MODULE core.settings
ENV PYTHONPATH /usr/src/gdemo_django

RUN pip install --no-cache-dir django==2.2.5
RUN pip install --no-cache-dir sec==0.2.2
RUN pip install --no-cache-dir psycopg2==2.8.3
RUN pip install --no-cache-dir django-improved-user==1.0.0
RUN pip install --no-cache-dir markdown==3.1.1
RUN pip install --no-cache-dir pygments==2.4.2

COPY --chown=8000:8000 / /usr/src
