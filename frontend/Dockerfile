# Build stage
FROM node:18-alpine as build

# Set working directory
WORKDIR /app

# Install dependencies first (for better caching)
COPY package*.json ./
RUN npm install

# Copy tsconfig and other config files
COPY tsconfig.json .
COPY tailwind.config.js .
COPY postcss.config.js .
COPY craco.config.js .

# Copy source code
COPY . .

# Install additional type definitions
RUN npm install --save-dev \
    @types/node@20.10.4 \
    @types/react@18.2.42 \
    @types/react-dom@18.2.17

# Build the app
RUN npm run build

# Production stage
FROM nginx:alpine

# Copy nginx configuration
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Copy built assets from build stage
COPY --from=build /app/build /usr/share/nginx/html

# Expose port
EXPOSE 3000

# Start nginx
CMD ["nginx", "-g", "daemon off;"]