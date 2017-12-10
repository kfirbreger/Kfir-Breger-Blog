FROM python:slim

EXPOSE 80

RUN apt-get update && \
    apt-get install -y nginx

RUN mkdir -p /app/output
ADD nginx.conf /etc/nginx/
# Blog
RUN pip install pipenv

WORKDIR /app

COPY Pipfile* /app/
RUN pipenv install --system --deploy

COPY src /app/src
COPY images /app/output/images
COPY pelican.conf.py  /app/

# Make nginx the owner
RUN chown www-data:www-data -R /app/output

COPY docker-entrypoint.sh /app/docker-entrypoint.sh

CMD /app/docker-entrypoint.sh
