FROM node:16-alpine
RUN apk update && \
    apk upgrade && \
    apk add git
RUN git clone https://github.com/noxlock/my-anime-openings-list.git
WORKDIR my-anime-openings-list/MAOL/vue/
RUN npm i --legacy-peer-deps
RUN npm run build


FROM python:3.9-buster
COPY --from=0 my-anime-openings-list/ ./my-anime-openings-list/
WORKDIR ./my-anime-openings-list/
COPY ./server.csr ./server.csr
COPY ./server.key ./server.key
RUN pip install -r requirements.txt
EXPOSE 443
WORKDIR ./MAOL/
ENTRYPOINT gunicorn --certfile=server.crt --keyfile=server.key -b 0.0.0.0:443 MAOL.wsgi