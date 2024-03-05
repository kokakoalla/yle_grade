FROM python:3.12-rc-alpine

WORKDIR /app

COPY requirements.txt . 
#COPY requirements.txt . OR . . 
#WTF is requiremnents.txt?

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "main.py"]
