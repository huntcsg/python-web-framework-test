FROM pypy:3.6

RUN pip install --upgrade pip

WORKDIR /opt/web-framework-test

COPY deps/pyramid.in ./deps/pyramid.in

RUN pip install -r deps/pyramid.in

COPY . ./

RUN pip install -e .[pyramid]
