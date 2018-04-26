FROM debian:latest

RUN apt-get update -q
RUN apt-get install -yq \
    build-essential pkg-config libestr-dev zlib1g-dev \
    uuid-dev libgcrypt20-dev liblogging-stdlog-dev libhiredis-dev uuid-dev \
    libgcrypt11-dev liblogging-stdlog-dev flex bison wget autoconf libtool \
    git libtool libcurl3-dev


RUN git clone https://github.com/rsyslog/libfastjson.git
RUN cd libfastjson \
    && sh autogen.sh \
    && ./configure \
    && make && make install


ENV RSYSLOG_VERSION 8.34.0
RUN wget https://github.com/rsyslog/rsyslog/archive/v"$RSYSLOG_VERSION".tar.gz
RUN tar -xzf v"$RSYSLOG_VERSION".tar.gz
RUN cd rsyslog-"$RSYSLOG_VERSION"/ \
    && autoreconf -fvi \
    && ./configure --enable-omhiredis \
    && make && make install

EXPOSE 514 514/udp
VOLUME [ "/var/log", "/etc/rsyslog.d" ]

COPY rsyslog.conf /etc/rsyslog.conf

ENTRYPOINT [ "rsyslogd", "-n" ]
