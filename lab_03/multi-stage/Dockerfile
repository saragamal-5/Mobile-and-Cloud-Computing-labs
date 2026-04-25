# Stage 1: dummy build
FROM busybox AS builder
RUN echo "Hello Multi-Stage" > /tmp/index.html

# Stage 2: serve with nginx
FROM nginx
COPY --from=builder /tmp/index.html /usr/share/nginx/html/index.html