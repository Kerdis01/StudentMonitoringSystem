# Use the official Gradle image with JDK 17 for the build stage
FROM gradle:8.5.0-jdk21 as builder
WORKDIR /app
COPY build.gradle settings.gradle /app/
COPY gradlew /app/
COPY gradle /app/gradle
RUN chmod +x ./gradlew
COPY src/ /app/src/
RUN ./gradlew clean build --stacktrace

# Use the official OpenJDK image for the run stage
FROM openjdk:21-jdk-slim
WORKDIR /app
COPY --from=builder /app/build/libs/*.jar /app.jar
EXPOSE 8080
ENTRYPOINT ["java", "-jar", "/app.jar"]
