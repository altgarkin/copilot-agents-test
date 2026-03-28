import os
from dotenv import load_dotenv

# .env dosyasını yükle (varsa)
load_dotenv()

AWS_SECRET_KEY = os.getenv("AWS_SECRET_KEY")

def connect():
  if not AWS_SECRET_KEY:
    print("Error: AWS_SECRET_KEY is not set!")
    return
  print(f"Connecting with: {AWS_SECRET_KEY}")

connect()
