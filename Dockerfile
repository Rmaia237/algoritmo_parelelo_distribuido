FROM python:3-alpine

COPY *.py /server/
WORKDIR /server

EXPOSE 5000

ENTRYPOINT ["python"]
CMD ["-u", "start.py"]
