# Use an official Node.js runtime as a parent image
FROM node:18.18.0

# Set the working directory inside the container
COPY . /app
WORKDIR ./app

# Install project dependencies
RUN npm install

# Expose the port your app will run on (in this case, 3000)
EXPOSE 3000

# Define the command to start your application
CMD node app.js
