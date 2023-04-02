FROM python:3.10-alpine

ENV PYTHONPATH="/app/"

RUN pip install --upgrade pip

WORKDIR /app

COPY . /app/

RUN pip3 install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD [ "python", "./app.py" ]