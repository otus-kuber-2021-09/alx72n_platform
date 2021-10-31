FROM nginx:1.21.3
RUN usermod --uid 1001 nginx
WORKDIR /app
COPY ./nginx.conf /etc/nginx/conf.d/web.conf
EXPOSE 8000
