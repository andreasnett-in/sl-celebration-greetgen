FROM python:3.10.10-slim

RUN pip3 install --upgrade pip
RUN pip3 install uvicorn

WORKDIR /app  
  
COPY requirements.txt .  
  
RUN pip install --no-cache-dir -r requirements.txt  
  
COPY . .  
  
CMD ["uvicorn", "deploy.app:app", "--host", "0.0.0.0", "--port", "8082"]  
