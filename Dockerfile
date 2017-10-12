FROM centos

RUN curl "https://bootstrap.pypa.io/get-pip.py" -o "get-pip.py" && \
    python get-pip.py && \
    rm get-pip.py

COPY . /server
WORKDIR /server

RUN pip install --user -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["python"]
CMD ["start.py"]
