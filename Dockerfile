# Use the official Golang image as a builder
FROM golang:1.21 as builder

# Set the working directory
WORKDIR /app

# Copy the source code
COPY . .

# Build the Go binary
RUN go mod init app && go mod tidy && go build -o server .

# Use a minimal base image
FROM alpine:latest

# Set the working directory
WORKDIR /root/

# Copy the compiled Go binary from builder stage
COPY --from=builder /app/server .

# Expose the port
EXPOSE 8080

# Run the binary
CMD ["./server"]
