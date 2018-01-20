FROM devtc/ubuntu-django-react:0.1
ENV PYTHONUNBUFFERED 1
RUN apt update && apt install -y binutils libproj-dev
RUN mkdir /code/src
WORKDIR /code
ADD requirements.txt src/code/
RUN pip install -r src/requirements.txt
ADD . /code/
