FROM golang:1.18 as builder

# Set the Current Working Directory inside the container
WORKDIR /app

# Copy go mod file
COPY go.mod ./

# Download all dependencies
RUN go mod download

# Copy the source from the current directory to the Working Directory inside the container
COPY . /app/

# Build the Go app
RUN CGO_ENABLED=0 GOOS=linux GOARCH=amd64 go build -o main .

######## Start a new stage from scratch #######
FROM alpine:latest

RUN apk --no-cache add ca-certificates

WORKDIR /root/

# Copy the Pre-built binary file from the previous stage
COPY --from=builder /app/main .

# Expose port 8090 to the outside world
EXPOSE 8090

# Command to run the executable
CMD ["./main"]
