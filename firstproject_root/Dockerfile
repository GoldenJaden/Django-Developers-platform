FROM python:3.11-alpine

WORKDIR /app

COPY ./requirements.txt ./

# Dependencies for PILLOW
RUN apk add -u zlib-dev jpeg-dev gcc musl-dev
# PIP requirements
RUN pip install -r requirements.txt --no-cache-dir

COPY . .

EXPOSE 8000
