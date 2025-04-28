# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3-alpine

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Install gcc and musl-dev for building the cryptography package
WORKDIR /app
COPY . /app

# Create a directory for output files
RUN mkdir -p /output
# Set up volume for persisting output
VOLUME /output

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
CMD ["sh", "-c", "python -v /output:/output challenge_b.py > /output/output.csv"]
