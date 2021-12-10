FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY . /opt/chat
WORKDIR /opt/chat
RUN pip freeze > requirements.txt
