# Use the official Python image as the base image
FROM python:3.13

# Install Poetry
RUN pip install poetry

# Set the working directory (no need for copying)
WORKDIR /app

# Install project dependencies using Poetry (poetry.lock will be used)
COPY ./pyproject.toml ./poetry.lock /app/
RUN poetry update
RUN poetry install --no-interaction --no-ansi --no-root

CMD ["poetry", "run", "python", "main.py"]
