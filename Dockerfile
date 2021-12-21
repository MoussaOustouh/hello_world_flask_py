FROM python:3.6.1-alpine
RUN pip install --upgrade pip && pip install flask
CMD ["python","main.py"]
COPY main.py /main.py