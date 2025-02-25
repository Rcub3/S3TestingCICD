# Use the official Golang image as a builder
FROM golang:1.21 as builder

# Set the working directory
WORKDIR /app

# Copy go.mod and go.sum first (for better caching)
COPY go.mod go.sum ./

# Download dependencies
RUN go mod tidy

# Copy the rest of the source code
COPY . .

# Build the Go binary with optimizations
RUN CGO_ENABLED=0 GOOS=linux GOARCH=amd64 go build -o server .

# Use a minimal base image
FROM alpine:latest

# Install CA certificates
RUN apk --no-cache add ca-certificates

# Set a non-root user for security
RUN addgroup -S app && adduser -S app -G app
USER app

# Set the working directory
WORKDIR /home/app

# Copy the compiled Go binary from builder stage
COPY --from=builder /app/server .

# Expose the port
EXPOSE 8080

# Run the binary
CMD ["./server"]
