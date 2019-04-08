FROM python:3
COPY helloflask.py /

RUN pip install Flask


RUN pip install Flask

#run a command inside

ENV VAR1=hello
ENV VAR2=cainthus


LABEL ROLE=web-server
# test with docker inspect

EXPOSE 8080/TCP

CMD [ "python", "./helloflask.py" ]
