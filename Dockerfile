FROM python:3
ADD helloflask.py /

RUN pip install Flask

CMD [ "python", "./helloflask.py" ]
