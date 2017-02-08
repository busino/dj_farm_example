FROM python:3.5-alpine
RUN mkdir /install
COPY ./requirements.txt /install 
WORKDIR /install
RUN apk add --update --no-cache mariadb-client-libs py-gunicorn \
	&& apk add --no-cache --virtual .build-deps \
	    mariadb-dev \
	    gcc \
	    musl-dev \
	&& pip install -r requirements.txt \
    && apk del .build-deps
CMD ["python", "manage.py", "runserver", "0.0.0.0:8008"]