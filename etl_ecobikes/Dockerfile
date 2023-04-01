FROM python:3.9-slim-buster

ADD requeriments.txt requeriments.txt
RUN pip install -r requeriments.txt
COPY . .

CMD [ "python","-u","main.py" ]