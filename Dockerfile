FROM python:3.8.12-slim

COPY model.joblib /model.joblib
COPY api /api
COPY TaxiFareModel /TaxiFareModel
COPY Makefile /Makefile
COPY MANIFEST.in /MANIFEST.in
COPY setup.py /setup.py
COPY requirements.txt /requirements.txt

RUN pip install --upgrade pip 
RUN pip install -r requirements.txt

CMD uvicorn api.fast:app --host 0.0.0.0 --port $PORT

