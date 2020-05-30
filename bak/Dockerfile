from python:3.7
WORKDIR /testPython/test
COPY requirements.txt ./
RUN pip3 install -r requirements.txt

COPY . .

CMD ["gunicorn", "testServer:app", "-c", "./gunicorn.conf.py"]