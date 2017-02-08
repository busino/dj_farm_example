FROM python:3.5-alpine
RUN mkdir /setup
ADD . /setup
WORKDIR /setup/farm
RUN apk add --update --no-cache mariadb-client-libs \
	&& apk add --no-cache --virtual .build-deps \
	    mariadb-dev \
	    gcc \
	    musl-dev \
	&& pip install -r requirements.txt \
    && apk del .build-deps
#CMD ["python", "manage.py", "runserver", "0.0.0.0:8008"]