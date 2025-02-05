FROM python:3.9-alpine3.13
LABEL maintainer="python-devs"

ENV PYTHONUNBUFFERED=1

COPY ./requirements.txt /tmp/requirements.txt
COPY ./requirements.dev.txt /tmp/requirements.dev.txt
COPY ./app /app
WORKDIR /app
EXPOSE 8000

ARG DEV=false

# Create a virtual environment and install dependencies
RUN python -m venv /py && \
  /py/bin/pip install --upgrade pip && \
  /py/bin/pip install -r /tmp/requirements.txt && \
  if [ "$DEV" = "true" ]; then \
  /py/bin/pip install -r /tmp/requirements.dev.txt; \
  fi && \
  rm -rf /tmp

# Add django-user and fix ownership
RUN adduser -D -H -s /bin/sh django-user && \
  chown -R django-user /app /py

# Ensure virtualenv binaries are accessible
ENV PATH="/py/bin:$PATH"

# Switch to non-root user
USER django-user
