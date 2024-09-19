FROM python:3.11.10-slim-bullseye
RUN pip3 install pandas==2.2.2
COPY renamer.py .