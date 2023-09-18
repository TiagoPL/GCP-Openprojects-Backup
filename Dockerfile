FROM python:3.10

WORKDIR /app

COPY . /app

RUN apt update && apt install jq -y
RUN pip install --upgrade pip && pip install flask google-cloud-storage

ENV GOOGLE_APPLICATION_CREDENTIALS=/app/serene-courier-198218-d2689a4ce71d.json

EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0"]

# docker build -t nome-da-imagem .
# docker container run -dit -p 5000:5000 --name=nome-do-container -v /db:/db nome-da-imagem
