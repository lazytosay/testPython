FROM python:3.7
MAINTAINER bill
COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt
COPY . .
CMD ["gunicorn", "app_flask:app", "-c", "./gunicorn.conf.py"]
