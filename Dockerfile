FROM python:3.6

COPY . /myproject
WORKDIR /myproject
RUN pip install -e .

CMD ["myproject", "run"]
