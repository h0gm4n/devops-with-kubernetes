FROM python:3.11-slim
WORKDIR /app
COPY . .
RUN pip install flask

# Ensure shared dir exists and is owned by app user
RUN groupadd -r app && useradd -r -g app -d /app -s /sbin/nologin app \
	&& mkdir -p /app /shared && chown -R app:app /app /shared

# Copy application files
COPY generator.py reader.py /app/

# Expose HTTP port for the reader
EXPOSE 3000

# Run as non-root by default
USER app

# Default command (overridden in the pod spec where needed)
CMD ["python", "-u", "reader.py"]
