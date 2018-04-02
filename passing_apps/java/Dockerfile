FROM maven:3.5-jdk-8-alpine
WORKDIR /app
COPY /demo/pom.xml /app/pom.xml
RUN ["mvn", "dependency:resolve"]
COPY /demo/ /app
RUN ["mvn", "package"]
ENTRYPOINT ["/usr/bin/java"]
CMD ["-jar", "/app/target/javademo-0.1.0.jar"]
EXPOSE 8081
