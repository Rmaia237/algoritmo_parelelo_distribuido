FROM python:3-alpine

EXPOSE 5000

WORKDIR /usr/src/app

#COPY requirements.txt ./
#RUN pip install --no-cache-dir -r requirements.txt

COPY *.py ./

ENTRYPOINT ["python"]
CMD ["-u", "./start.py"]
