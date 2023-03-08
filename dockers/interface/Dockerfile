FROM node:latest

WORKDIR /app

COPY interface/package.json /app/

RUN npm install

EXPOSE 3000

COPY interface/. /app/

CMD ["npm", "start"]