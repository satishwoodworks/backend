FROM python:3.10

# cd to working directory
WORKDIR /usr/src/app

# copy the whole source code 
COPY ./ /usr/src/app

# install requirements
RUN pip install --no-cache-dir --upgrade -r /usr/src/app/requirements.txt
