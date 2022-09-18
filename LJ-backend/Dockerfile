FROM python:3.9
ENV TIME_ZONE=Asia/Singapore
ENV BUCKET=sr_notification_dev

# ARG env
# ARG user
# ARG pass
# ARG host
# ARG db

# ENV ENV_MODE=$env
# ENV POSTGRES_USERNAME=$user
# ENV POSTGRES_PASSWORD=$pass
# ENV POSTGRES_HOST=$host
# ENV POSTGRES_DB=$db
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

COPY . /app
WORKDIR /app
RUN apt-get update
RUN apt-get install -y gcc python3-dev
RUN pip install -r backend/requirements.txt

WORKDIR /app/backend
CMD exec gunicorn --bind 0.0.0.0:5000 --workers 1 --worker-class uvicorn.workers.UvicornWorker --threads 2 main:app
# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5000"]
