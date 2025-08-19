import os, time, requests

TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT  = os.getenv("TELEGRAM_CHAT_ID")
API   = f"https://api.telegram.org/bot{TOKEN}"

def send(msg: str):
    if TOKEN and CHAT:
        try:
            requests.post(f"{API}/sendMessage", data={"chat_id": CHAT, "text": msg[:4000]}, timeout=10)
        except Exception as e:
            print("send error:", e)

if __name__ == "__main__":
    send("agent_hello: démarrage")
    i = 0
    while True:
        i += 1
        send(f"agent_hello: ping {i}")
        time.sleep(10)
