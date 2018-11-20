FROM mysql:latest

ENV MYSQL_ROOT_PASSWORD=testing
ENV MYSQL_DATABASE=django
ENV MYSQL_USER=user1
ENV MYSQL_PASSWORD=testing

#add startMysql.sh .
#ENTRYPOINT mysql -u root -ptesting -e 'ALTER USER root IDENTIFIED WITH mysql_native_password BY 'testing';'
CMD [ "/bin/bash" ]

