FROM centos

COPY . /server
WORKDIR /server

RUN curl "https://bootstrap.pypa.io/get-pip.py" -o "get-pip.py" && \
    python get-pip.py && \
    rm get-pip.py && \
    pip install -r requirements.txt

ENTRYPOINT ["python"]
CMD ["server.py"]

