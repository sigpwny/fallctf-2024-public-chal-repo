FROM python:3.12.6
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY app.py .
COPY static/ static/
COPY flag.png /
EXPOSE 1337
CMD ["hypercorn", "app:app", "--bind", "0.0.0.0:1337"]