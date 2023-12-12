# Use the official Gradle image for the build stage
FROM gradle:7.2.0-jdk11 as builder

# Set the working directory in the Docker image
WORKDIR /app

# Copy the Gradle configuration files
COPY build.gradle settings.gradle /app/

# Copy the Gradle wrapper
# Ensure that the Gradle wrapper has execute permissions before copying
COPY gradlew /app/
COPY gradle /app/gradle
RUN chmod +x ./gradlew

# Copy the source code
COPY src /app/src

# Build the application
RUN ./gradlew clean build

# Use the official OpenJDK image for the run stage
FROM openjdk:11-jre-slim

# Set the working directory in the Docker image
WORKDIR /app

# Copy the built jar file from the build stage to the run stage
COPY --from=builder /app/build/libs/*.jar /app/app.jar

# Expose the port the app runs on
EXPOSE 8080

# Run the application
ENTRYPOINT ["java", "-jar", "/app/app.jar"]
