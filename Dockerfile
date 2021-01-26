FROM python:3.6.6-alpine
# copy data to app from src folder 
COPY src /app
# Now working directory is app
WORKDIR /app
#RUN apk update && apk add libressl-dev postgresql-dev libffi-dev gcc musl-dev python3-dev 
#RUN apk update && apk add libressl-dev postgresql-dev libffi-dev gcc musl-dev
# This is for fixing the missing gcc library in alpine image. On mac it is present as part of x-code.
# Try removing libressl-dev and/or libffi-dev
RUN apk update && apk add libressl-dev libffi-dev gcc musl-dev
RUN pip install -r requirements.txt
# It will create local host at port 5000
EXPOSE 5000
# entrypoint means special executed command 
ENTRYPOINT ["python"]
# CMD can be apply in dockerfile only last one
CMD ["analyse.py"]