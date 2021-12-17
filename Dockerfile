FROM python:3.9

WORKDIR parking_space
# Setup env
ENV PYTHONUNBUFFERED=1

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY . /parking_space/.

EXPOSE 8080
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8080"]



