FROM pypy:3.6

RUN pip install --upgrade pip

WORKDIR /opt/web-framework-test

COPY deps/tornado.in ./deps/tornado.in

RUN pip install -r deps/tornado.in

COPY . ./

RUN pip install -e .[tornado]
