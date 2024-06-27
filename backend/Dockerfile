FROM python:3.8-slim-buster

# # run this before copying requirements for cache efficiency
# RUN pip install --upgrade pip

RUN apt-get update && apt-get install -y libpq-dev build-essential

#set envionment variables
ENV PYTHONUNBUFFERED=1

#set work directory early so remaining paths can be relative
WORKDIR /backend

# Adding requirements file to current directory
# just this file first to cache the pip install step when code changes
COPY requirements.txt /backend/requirements.txt

#install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# copy code itself from context to image
COPY . /backend/

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]