# Use the official Golang image to build the application
FROM golang:1.20 AS builder

# Set the working directory inside the container
WORKDIR /app

# Copy the randnumb.go script into the container
COPY randnumb.go .

# Download necessary Go modules (if any)
RUN go mod init random-server && go mod tidy

# Build the Go application
RUN go build -o server .

# Use a lightweight image to run the built application
FROM alpine:latest

# Set the working directory
WORKDIR /root/

# Copy the compiled binary from the builder stage
COPY --from=builder /app/server /root/

# Expose port 8080 for the web server
EXPOSE 8080

# Run the server binary
CMD ["./server"]
