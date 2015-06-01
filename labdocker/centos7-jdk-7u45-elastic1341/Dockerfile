FROM mcortinas/centos7-jdk-7u45:v2
MAINTAINER Marc Cortinas <marc.cortinas@gmail.com> (@mcortinas)


#FROM centos
#RUN yum install -y wget
#RUN wget --no-check-certificate --no-cookies --header "Cookie: oraclelicense=accept-securebackup-cookie" http://download.oracle.com/otn-pub/java/jdk/7u45-b18/jdk-7u45-linux-x64.rpm -c -O jdk-7u45-linux-x64.rpm
#RUN rpm -Uvh jdk-7u45-linux-x64.rpm
#RUN rm -f /root/jdk-7u45-linux-x64.rpm

RUN wget https://download.elastic.co/elasticsearch/elasticsearch/elasticsearch-1.3.4.noarch.rpm -O /root/elasticsearch-1.3.4.noarch.rpm
RUN rpm -Uvh /root/elasticsearch-1.3.4.noarch.rpm
RUN rm -f /root/elasticsearch-1.3.4.noarch.rpm

ENV ELASTICSEARCH_VERSION 1.3.4

ENV PATH /usr/share/elasticsearch/bin:$PATH
COPY config /usr/share/elasticsearch/config

VOLUME /usr/share/elasticsearch/data

COPY docker-entrypoint.sh /
ENTRYPOINT ["/docker-entrypoint.sh"]

EXPOSE 9200 9300

CMD ["elasticsearch"]


