# Use the official Golang image to build the application
FROM golang:1.21 AS builder

# Set the working directory inside the container
WORKDIR /app

# Copy Go module files first for efficient caching
COPY go.mod go.sum ./
RUN go mod download

# Copy the rest of the application files
COPY . .

# Build the Go application
RUN go build -o server .

# Use a lightweight image for running the built binary
FROM alpine:latest

# Set the working directory
WORKDIR /root/

# Copy the compiled binary from the builder stage
COPY --from=builder /app/server .

# Expose the port the app runs on
EXPOSE 8080

# Run the application
CMD ["./server"]
