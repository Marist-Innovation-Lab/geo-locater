FROM ubuntu:16.04
MAINTAINER Daniel Gisolfi
RUN apt-get update -y
RUN apt-get install -y \
    python-pip  \
    python-dev \
    build-essential \
    libpq-dev \
    tzdata \
&& pip install --upgrade pip

#Set the TimeZone 
RUN cp /usr/share/zoneinfo/America/New_York /etc/localtime
RUN dpkg-reconfigure tzdata

EXPOSE 8080
WORKDIR /geo-locater
COPY /geo-locater/ .
COPY requirements.txt .
RUN pip install -r requirements.txt
CMD ["python","-u","app.py"]
