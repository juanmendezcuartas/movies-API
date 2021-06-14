FROM python:3.9.5-alpine3.12

WORKDIR /app

COPY . /app

RUN pip3 install -r requirements.txt

CMD [ "python3" , "src/app.py" ]