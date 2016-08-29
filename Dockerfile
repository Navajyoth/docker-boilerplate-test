FROM ubuntu:14.04

MAINTAINER Navajyoth MS

RUN apt-get update
RUN apt-get upgrade -y

RUN apt-get install -y python-pip libpq-dev python-dev \
        git \
        python \
        python-dev \
        python-setuptools \
        nginx \
        postgresql postgresql-contrib
        DEBIAN_FRONTEND=noninteractive apt-get install -y -q \
        postgresql-9.3 \
        postgresql-contrib-9.3 \

RUN rm -v /etc/nginx/nginx.conf
COPY nginx-app.conf /etc/nginx/sites-available/default
COPY supervisor.conf /etc/supervisor/conf.d/

ADD postgresql.conf /etc/postgresql/9.3/main/postgresql.conf
ADD pg_hba.conf /etc/postgresql/9.3/main/pg_hba.conf
RUN chown postgres:postgres /etc/postgresql/9.3/main/*.conf
ADD run.sh /usr/local/bin/run.sh
RUN chmod +x /usr/local/bin/run.sh

VOLUME ["/var/lib/postgresql"]
EXPOSE 5432
CMD ["/usr/local/bin/run.sh"]

COPY requirements.txt /home/app
RUN virtualenv --no-site-packages /home/env
RUN . /home/env/bin/activate

COPY . /home/app/
RUN pip install -r requirements.txt

VOLUME ["var/log"]

RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN python manage.py migrate --noinput
RUN python manage.py collectstatic --noinput

EXPOSE 80
CMD ["supervisord", "-n"]
