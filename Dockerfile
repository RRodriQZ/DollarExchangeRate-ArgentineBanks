FROM alpine:3.10

RUN apk add --no-cache python3-dev && pip3 install --upgrade pip

WORKDIR /dollar_scraping

COPY . /dollar_scraping

RUN pip3 --no-cache-dir install -e .

CMD ["python3", "main.py"]