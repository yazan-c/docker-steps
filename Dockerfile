FROM python:3
COPY helloflask.py /

RUN pip install Flask

EXPOSE 8080/TCP
CMD [ "python", "./helloflask.py" ]
