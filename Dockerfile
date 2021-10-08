# Most of the time, Alpine is a great base image to start with.
# If we're building a container for Python, we use something different.
# Learn why here: https://pythonspeed.com/articles/base-image-python-docker-images/
# TLDR: Alpine is very slow when it comes to running Python!

# STEP 1: Install base image. Optimized for Python.
FROM python:3.7-slim-buster

ADD . /app
WORKDIR /app
COPY requirements.txt /
RUN pip3 install -r requirements.txt

# STEP 5: Declare environment variables
ENV FLASK_APP=app.py
ENV FLASK_ENV=development

# STEP 6: Expose the port that Flask is running on
EXPOSE 5000

# STEP 7: Run Flask!
CMD ["flask", "run", "--host=0.0.0.0"]