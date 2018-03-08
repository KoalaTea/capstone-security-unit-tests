FROM maven:3.5-jdk-8-alpine
WORKDIR /app
COPY /demo/ /app
RUN ["mvn", "package"]
ENTRYPOINT ["/usr/bin/java"]
CMD ["-jar", "/app/target/javademo-0.1.0.jar"]
EXPOSE 8080
