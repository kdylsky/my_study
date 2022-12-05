FROM python

WORKDIR /the/workdir/path

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY  . .

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0:8000"]


