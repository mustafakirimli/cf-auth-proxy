FROM python:3.7.4-stretch
COPY . /app
WORKDIR /app
RUN pip install -r requirements
EXPOSE 80
ENTRYPOINT ["python3"]
CMD ["app.py"]
