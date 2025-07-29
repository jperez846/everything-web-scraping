FROM node:13.12.0-alpine

LABEL "lesson.number"=1

ENV PATH /app/node_modules/.bin:$PATH

COPY package.json ./
COPY package-lock.json ./
RUN npm install --silent

COPY . ./

ENV HOST 0.0.0.0
ENV PORT 3000

CMD ["npm", "start"]