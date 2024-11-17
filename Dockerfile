FROM python:3.11-slim

ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /bookmarks

COPY ./requirements.txt .

RUN pip install -r requirements.txt

RUN apt-get update && apt-get install -y

COPY bookmarks/ .

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]