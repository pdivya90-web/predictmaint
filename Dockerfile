FROM python:3.10-slim
WORKDIR /app
RUN apt-get update && apt-get install -y --no-install-recommends gcc python3-dev && rm -rf /var/lib/apt/lists/*
COPY requirements.txt .
RUN pip install --no-cache-dir -U pip && pip install --no-cache-dir -r requirements.txt
COPY app.py .
COPY best_xgboost_model.joblib .
EXPOSE 7860 
ENV STREAMLIT_SERVER_PORT=7860 STREAMLIT_SERVER_ADDRESS=0.0.0.0 STREAMLIT_SERVER_HEADLESS=true STREAMLIT_BROWSER_GATHER_USAGE_STATS=false
CMD ["streamlit", "run", "app.py", "--server.port=7860", "--server.address=0.0.0.0"]