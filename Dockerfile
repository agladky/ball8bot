
FROM python:3.5-alpine

WORKDIR /ball8bot

ADD . /ball8bot

RUN apk add --no-cache gcc musl-dev libffi-dev openssl-dev

RUN pip install --upgrade pip
RUN pip install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 80

CMD ["python", "main.py"]