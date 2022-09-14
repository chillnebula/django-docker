#Pull base image
FROM python:3-alpine

# Set environment variables
#ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

# Install dependencies
COPY ./requirements.txt .
RUN pip install -r requirements.txt
#RUN sudo service postgresql start

# Copy project
COPY . .