FROM node:latest 

WORKDIR /usr/app
ADD ./interface/package.json .
ADD ./interface/package-lock.json .
RUN npm install

COPY ./interface .

USER node

EXPOSE 3000

CMD ["npm", "run", "start"]