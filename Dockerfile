FROM python:3.10-slim

WORKDIR /app
# RUN pip3 install poetry
# COPY pyproject.toml poetry.lock ./
COPY forbidden_words.txt ./
# RUN poetry install --no-dev # Установка без зависимостей для разработки
COPY requirements.txt ./
RUN pip install -r requirements.txt


COPY /app /app
CMD [ "python" , "aiogram_run.py"]

# ENV PYTHONUNBUFFERED=1 \
#     PIP_DISABLE_PIP_VERSION_CHECK=on \
#     PIP_NO_CACHE_DIR=off \
#     USE_DOCKER=1 \
# 	# poetry:
# 	# POETRY_VERSION=1.2.0 \
# 	POETRY_VIRTUALENVS_CREATE=false \
# 	POETRY_CACHE_DIR='/var/cache/pypoetry'
