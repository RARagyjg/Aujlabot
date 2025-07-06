from keep_alive import keep_alive
keep_alive()  # ✅ Keeps the bot alive on platforms like Render or Replit

from instagrapi import Client
import time
import random

# 🔐 Login to Instagram
cl = Client()
cl.login_by_sessionid("70016257168%3AM6nSnozvM5Bg2H%3A29%3AAYe0gCJZkBuwV_gmYH-5eX8gft7dmvg-5BWGrySBfg")  # ← Yaha apna session ID daalo

# 🔁 List of names to rotate
group_names = [
    "NICK TERI TMKC ♥️",
    "NICK TERI TMKC 🖤",
    "NICK TERI TMKC 🤍",
    "NICK TERI TMKC ❤️",
    "NICK TERI TMKC 🧡",
    "NICK TERI TMKC 💛",
    "NICK TERI TMKC 💚",
    "NICK TERI TMKC 🤎",
    "NICK TERI TMKC 💜",
    "NICK TERI TMKC 💙"
]

# 🔎 Sabse top wale GC ka thread ID lao
def get_gc_thread_id():
    threads = cl.direct_threads(amount=10)
    for thread in threads:
        if thread.is_group:
            return thread.id
    return None

# 🔄 Auto GC Name Changer
def start_auto_gc_rename():
    thread_id = get_gc_thread_id()
    if not thread_id:
        print("❌ Koi GC nahi mila.")
        return

    print(f"🚀 Changing GC name in thread: {thread_id}")

    while True:
        try:
            new_name = random.choice(group_names)
            cl.private_request(
                "direct_v2/threads/update_title/",
                {
                    "thread_id": thread_id,
                    "title": new_name
                }
            )
            print(f"✔️ GC name changed to: {new_name}")
            time.sleep(random.randint(10, 20))  # Safe delay
        except Exception as e:
            print(f"⚠️ Error while changing GC name: {e}")
            time.sleep(60)

# 🚀 Start
start_auto_gc_rename()
