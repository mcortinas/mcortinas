# Adding Centos7 javasdk
FROM centos
MAINTAINER Marc Cortinas <marc.cortinas@gmail.com>

RUN yum install -y wget
RUN wget --no-check-certificate --no-cookies --header "Cookie: oraclelicense=accept-securebackup-cookie" http://download.oracle.com/otn-pub/java/jdk/7u45-b18/jdk-7u45-linux-x64.rpm -c -O jdk-7u45-linux-x64.rpm
RUN rpm -Uvh jdk-7u45-linux-x64.rpm
RUN rm -f /root/jdk-7u45-linux-x64.rpm



