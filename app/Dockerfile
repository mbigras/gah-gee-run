FROM python:3.11.3-bullseye

WORKDIR /app

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY app.py entrypoint.sh entrypoint2.sh ./

ENTRYPOINT ["/app/entrypoint.sh"]
