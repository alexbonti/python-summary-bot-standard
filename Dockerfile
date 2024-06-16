FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install the dependencies
RUN pip install -r requirements.txt

# Copy the app code
COPY . .

# Set the environment variables
ENV PORT 8080

EXPOSE 8080

# Run the command to start the development server
CMD ["python", "summary-bot.py"]