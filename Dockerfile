FROM python:3.11-bookworm as base
WORKDIR /app
EXPOSE 5000

COPY ./Src /app/Src
COPY ./Utils /app/Utils
COPY ./settings.json /app/settings.json
COPY ./main.py /app/main.py

RUN pip install flask
CMD ["python3", "main.py"]