FROM python:3.10



WORKDIR /alert_project


RUN curl -sSL https://install.python-poetry.org | python3 -

ENV PATH /root/.local/bin:$PATH

COPY pyproject.toml poetry.lock ./

COPY ./data .

RUN poetry config virtualenvs.create false \
  && poetry install --no-interaction --no-ansi


COPY . /alert_project




CMD [ "python", "./main.py", "./startup.sh" ]