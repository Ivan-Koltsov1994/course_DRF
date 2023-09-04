FROM python:3.11-slim

WORKDIR /app_DRF

COPY requirements.txt /app_DRF/

RUN pip install -r requirements.txt

COPY . /app_DRF/

CMD ["python", "manage.py", "runserver"]