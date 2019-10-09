FROM pypy:3.6

RUN pip install --upgrade pip

WORKDIR /opt/web-framework-test

COPY deps/flask.in ./deps/flask.in

RUN pip install -r deps/flask.in

COPY . ./

RUN pip install -e .[flask]
