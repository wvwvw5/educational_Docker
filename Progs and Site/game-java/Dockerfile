FROM openjdk:11-jdk-slim

WORKDIR /app

COPY game.java .

RUN javac game.java

ENTRYPOINT ["java", "game"]
