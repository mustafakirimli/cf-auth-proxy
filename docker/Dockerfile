FROM python:3.7.4-stretch
RUN pip install -r requirements
COPY . /app
WORKDIR /app
EXPOSE 80
ENTRYPOINT ["python3"]
CMD ["app.py"]
