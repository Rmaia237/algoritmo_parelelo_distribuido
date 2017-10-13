FROM centos

COPY requirements.txt /

RUN curl "https://bootstrap.pypa.io/get-pip.py" -o "get-pip.py" && \
    python get-pip.py && \
    rm get-pip.py && \
    pip install --user -r requirements.txt

COPY *.py /server/
WORKDIR /server

EXPOSE 5000

ENTRYPOINT ["python"]
CMD ["-u", "start.py"]
