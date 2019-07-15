FROM python:3.7.4-alpine
COPY . /app
WORKDIR /app
RUN apk add gcc musl-dev python3-dev libffi-dev openssl-dev
RUN pip install -r requirements
RUN apk del gcc musl-dev python3-dev libffi-dev openssl-dev
EXPOSE 80
ENTRYPOINT ["python3"]
CMD ["app.py"]
