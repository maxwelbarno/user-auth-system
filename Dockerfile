FROM python:3.13-slim
WORKDIR /app
COPY . .
# install required packages for system
RUN apt update \
    && apt upgrade -y \
    && apt --no-install-recommends install -y default-libmysqlclient-dev gcc pkg-config \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install mysqlclient \
    && pip install --no-cache-dir -r requirements.txt
EXPOSE 5000
ENV FLASK_APP=run.py
CMD ["gunicorn", "run:app"]
