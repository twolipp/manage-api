FROM node:18-alpine

WORKDIR /manage-api/frontend

COPY package*.json .

RUN yarn install

COPY . .

RUN yarn build

EXPOSE 3000

# DEV MODE
CMD ["yarn", "dev"]

# PROD MODE
# CMD [ "yarn", "start" ]