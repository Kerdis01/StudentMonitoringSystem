# Install node
# Use package.json to install express and body-parser
# Copy engagementScore.js 
# Open port 4000
FROM node:14
WORKDIR /app
COPY package*.json ./
RUN npm install
RUN npm install body-parser
RUN npm install cors
RUN npm install --save-dev jest supertest
COPY src/ ./
EXPOSE 4000
ENV NODE_ENV=production
CMD ["node", "engagementScore.js"]
