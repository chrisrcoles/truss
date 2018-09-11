FROM python:3.6
ENV PYTHONUNBUFFERED 1

RUN mkdir -p /src/lib
COPY requirements.txt /src/lib
RUN pip install --no-cache-dir -r /src/lib/requirements.txt

COPY . /src/lib
WORKDIR /src/lib

CMD ["python", "./main.py", "sample.csv"]