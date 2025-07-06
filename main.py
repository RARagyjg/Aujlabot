from instagrapi import Client
import time
import random
from keep_alive import keep_alive  # Make sure keep_alive.py exists

# 🔌 Start web server for port binding (Render compatible)
keep_alive()

# 🔐 Instagram login
cl = Client()
cl.login_by_sessionid("70016257168%3AM6nSnozvM5Bg2H%3A29%3AAYe0gCJZkBuwV_gmYH-5eX8gft7dmvg-5BWGrySBfg")  # <-- Replace this with your real session ID

# 📛 List of group chat names to rotate
group_names = [
    "SHUBHANSH TMKC--- 💙",
    "SHUBHANSH TMKC--- 💜",
    "SHUBHANSH TMKC--- 🤎",
    "SHUBHANSH TMKC--- 💚",
    "SHUBHANSH TMKC--- 💛",
    "SHUBHANSH TMKC--- 🧡",
    "SHUBHANSH TMKC--- ❤️",
    "SHUBHANSH TMKC--- 🤍",
    "SHUBHANSH TMKC--- ♥️",
    "SHUBHANSH TMKC--- 🖤"
]

# 🔍 Get topmost group chat thread ID where you're admin
def get_top_gc_thread_id():
    threads = cl.direct_threads(amount=10)
    for thread in threads:
        if thread.is_group and thread.is_viewer_admin:
            return thread.id
    return None

# 🔁 Start renaming loop
def start_auto_gc_rename():
    thread_id = get_top_gc_thread_id()
    if not thread_id:
        print("❌ No admin GC found.")
        return

    print(f"🚀 Changing GC name of thread: {thread_id}")

    while True:
        try:
            new_name = random.choice(group_names)
            cl.direct_thread_update_title(thread_id, new_name)
            print(f"✔️ Changed GC name to: {new_name}")
            time.sleep(random.randint(10, 20))  # Delay between renames
        except Exception as e:
            print(f"⚠️ Error while changing name: {e}")
            time.sleep(60)

# ▶️ Start bot
start_auto_gc_rename()
