FROM python:3.8-slim

WORKDIR /app

COPY . .

RUN pip install -e .

ENTRYPOINT ["trolyso"]
CMD ["chat"] 