
FROM python:3.5-alpine

WORKDIR /ball8bot

ADD . /ball8bot

RUN pip install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 80

CMD ["python", "main.py"]