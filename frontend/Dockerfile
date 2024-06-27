# Create image based on the official Node image from dockerhub
FROM node:lts-buster AS development

# Create app directory
WORKDIR /manage-api/frontend

# Copy dependency definitions
COPY package.json /manage-api/frontend
COPY yarn.lock /manage-api/frontend

# Get all the code needed to run the app
COPY . /manage-api/frontend

# Expose the port the app runs in
EXPOSE 3000

# Serve the app
CMD ["yarn", "start"]