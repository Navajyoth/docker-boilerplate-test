FROM ubuntu:16.04

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

RUN apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys B97B0AFCAA1A47F044F244A07FCC7D46ACCC4CF8
RUN echo "deb http://apt.postgresql.org/pub/repos/apt/ precise-pgdg main" > /etc/apt/sources.list.d/pgdg.list
RUN apt-get update && apt-get install -y python-software-properties software-properties-common postgresql-9.3 postgresql-client-9.3 postgresql-contrib-9.3

RUN rm -v /etc/nginx/nginx.conf
COPY nginx.conf /etc/nginx/sites-available/default
COPY supervisor.conf /etc/supervisor/conf.d/

ADD postgresql.conf /etc/postgresql/9.3/main/postgresql.conf
ADD pg_hba.conf /etc/postgresql/9.3/main/pg_hba.conf
RUN chown postgres:postgres /etc/postgresql/9.3/main/*.conf
ADD run.sh /usr/local/bin/run.sh
RUN chmod +x /usr/local/bin/run.sh

VOLUME ["/var/lib/postgresql"]
EXPOSE 5432
CMD ["/usr/local/bin/run.sh"]

#COPY requirements.txt /home/app
#RUN virtualenv --no-site-packages /home/env
#RUN . /home/env/bin/activate

COPY . /home/app/
RUN pip install virtualenv virtualenvwrapper
RUN mkdir -p /opt/virtualenvs
ENV WORKON_HOME /opt/virtualenvs
RUN /bin/bash -c "source /usr/local/bin/virtualenvwrapper.sh \
    && mkvirtualenv env \
    && workon env \
    && pip install -r /home/app/requirements.txt"


#COPY . /home/app/
#RUN pip install -r requirements.txt

VOLUME ["var/log"]

RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN cd /home/app/django-boilerplate && workon env && python manage.py migrate --noinput
RUN cd /home/app/django-boilerplate && workon env && python manage.py collectstatic --noinput

EXPOSE 80
CMD ["supervisord", "-n"]
