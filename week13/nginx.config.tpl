worker_processes $worker_processes;
pid logs/nginx.pid;
events { worker_connections 1024;}
http {
    include mime.types;
    sendfile on;
    gzip on;

server {
    listen $listen;
    server_name localhost;

location / {
    root $root;
    index index.html index.htm;
}
}
}