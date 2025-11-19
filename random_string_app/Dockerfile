
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Make output unbuffered so logs appear immediately
ENV PYTHONUNBUFFERED=1 \
	PYTHONDONTWRITEBYTECODE=1

# Create a system user for running the app (non-root)
RUN groupadd -r app && useradd -r -g app -d /app -s /sbin/nologin app \
	&& mkdir -p /app && chown -R app:app /app

# Copy application code
COPY random_string.py /app/

# Switch to non-root user
USER app

# Default command
CMD ["python", "random_string.py"]
