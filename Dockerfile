FROM centos

RUN curl "https://bootstrap.pypa.io/get-pip.py" -o "get-pip.py" && \
    python get-pip.py && \
    rm get-pip.py

COPY . /server
WORKDIR /server

RUN pip install Flask
RUN pip install --user requests

ENTRYPOINT ["python"]
CMD ["start.py"]

