FROM node:10 AS node
COPY . /app
WORKDIR /app
RUN npm install
RUN npm rebuild node-sass
RUN node_modules/gulp/bin/gulp.js build


FROM python:3.5 AS django
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE=config.settings.production

# Requirements have to be pulled and installed here, otherwise caching won't work
COPY ./requirements /requirements
RUN pip install -r /requirements/production.txt \
    && groupadd -r django \
    && useradd -r -g django django

COPY --from=node /app /app
RUN chown -R django /app

COPY gunicorn.sh /gunicorn.sh
RUN sed -i 's/\r//' /gunicorn.sh \
    && chmod +x /gunicorn.sh \
    && chown django /gunicorn.sh

WORKDIR /app
ENTRYPOINT ["/bin/bash", "-c", "/gunicorn.sh"]
