FROM python

WORKDIR /app

COPY requirements.txt /app

RUN pip install -r requirements.txt

COPY  . /app

# VOLUME [ "/app/sentence" ]

EXPOSE 8000

# CMD ["python", "manage.py", "migrate"]

CMD ["python", "manage.py", "runserver", "0:8000"]


