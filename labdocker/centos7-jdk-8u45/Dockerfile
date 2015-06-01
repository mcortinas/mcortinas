# Adding jdk8u45 to Centos7 
FROM centos
MAINTAINER Marc Cortinas <marc.cortinas@gmail.com>

RUN yum install -y wget
RUN wget --no-check-certificate --no-cookies --header "Cookie: oraclelicense=accept-securebackup-cookie" http://download.oracle.com/otn-pub/java/jdk/8u45-b14/jdk-8u45-linux-x64.rpm -O /root/jdk-8u45-linux-x64.rpm
RUN rpm -Uvh jdk-8u45-linux-x64.rpm
RUN rm -f /root/jdk-8u45-linux-x64.rpm


