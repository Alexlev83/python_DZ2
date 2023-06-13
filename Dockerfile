FROM python

WORKDIR /app

COPY .  .

CMD ["python", "php docker.py"]