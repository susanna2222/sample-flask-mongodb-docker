FROM python:3.7

RUN mkdir /app
WORKDIR /app

ADD entrypoints.sh /app/entrypoints.sh
ADD app/ /app

RUN chmod +x /app/entrypoints.sh
RUN export -p

RUN pip install --upgrade pip --no-cache-dir
RUN pip install -r requirements.txt --no-cache-dir

EXPOSE 8000
ENV PYTHONPATH "${PYTHONPATH}:/app/"
ENV FLASK_APP "/run.py"
CMD ["/app/entrypoints.sh"]