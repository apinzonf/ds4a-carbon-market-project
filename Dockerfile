FROM python:3.8-slim-buster

WORKDIR /project

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY /app /project/app
COPY /assets /project/assets
COPY /data /project/data
COPY /notebooks /project/notebooks
COPY app.py /project/app.py
COPY version /project/version

CMD [ "python3", "app.py"]