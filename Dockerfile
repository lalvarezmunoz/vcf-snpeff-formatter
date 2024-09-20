FROM python:3.12.6
RUN pip3 install pandas==2.2.2
RUN mkdir -p renamer
COPY renamer.py /renamer
WORKDIR /renamer