import requests
import json
import os

# Store your webhook URL securely (e.g., as an environment variable)
WEBHOOK_URL = "You Webhook URL" # Replace with the URL you copied

def send_discord_message(content):
    """
    Sends a message to the Discord channel via the webhook.
    """
    data = {
        "content": content,
        "username": "Raspberry Pi Bot", # Custom username for the message
    }
    
    headers = {
        "Content-Type": "application/json"
    }
    
    try:
        response = requests.post(WEBHOOK_URL, data=json.dumps(data), headers=headers)
        response.raise_for_status() # Raise an exception for bad status codes
        print("Message sent successfully!")
    except requests.exceptions.RequestException as e:
        print(f"Error sending message: {e}")

def send_discord_image(webhook_url, image_path, message=""):
    try:
        with open(image_path, "rb") as f:
            # เตรียมไฟล์ภาพไม่เกิน 25 MB และข้อความ
            files = {"file": (image_path, f, "image/jpeg")}
            payload = {"content": message}
            
            # ส่งข้อมูลไปยัง Discord [Requests Documentation](https://requests.readthedocs.io)
            response = requests.post(webhook_url, data=payload, files=files)
            
            # ตรวจสอบสถานะ (Discord คืนค่า 200 หรือ 204 เมื่อสำเร็จ)
            if response.status_code in [200, 204]:
                print(f"✅ Success: ส่งรูป {image_path} เรียบร้อย!")
                return True
            else:
                print(f"❌ Error: {response.status_code} - {response.text}")
                return False
                
    except FileNotFoundError:
        print("⚠️ Error: ไม่พบไฟล์ภาพในตำแหน่งที่ระบุ")
        return False
    except Exception as e:
        print(f"⚠️ Error: เกิดข้อผิดพลาด {str(e)}")
        return False

# Example Send message:
send_discord_message("Hello from the Raspberry Pi! The system is online.")

# Example Send message:
IMG = "camera_shot.jpg"
send_discord_image(WEBHOOK_URL, IMG, "ตรวจพบความเคลื่อนไหว! 📸")

