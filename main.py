from instagrapi import Client
import time
import random
from keep_alive import keep_alive  # Render hosting ke liye keep_alive

# 🔌 Keep Render port alive
keep_alive()

# 🔐 Instagram login
cl = Client()
cl.login_by_sessionid("70016257168%3AM6nSnozvM5Bg2H%3A29%3AAYe0gCJZkBuwV_gmYH-5eX8gft7dmvg-5BWGrySBfg")  # Replace this with your session ID

# 💖 Colorful hearts
heart_colors = ["❤️", "🧡", "💛", "💚", "💙", "💜", "🖤", "🤍", "🤎"]

# 📛 Group names template
base_group_names = [
    "🔥 Tu pagal hai 🤣 | SHUBHANSH TMKC {heart}",
    "📛 Tu sudhar jaa 💀 | SHUBHANSH TMKC {heart}",
    "💘 Tujhe bahut marunga 💘 | SHUBHANSH TMKC {heart}",
    "🤣 BKL gang online | SHUBHANSH TMKC {heart}",
    "👻 Ghost Mode Activated | SHUBHANSH TMKC {heart}",
    "⚠️ Beta aaj toh maar padegi | SHUBHANSH TMKC {heart}",
    "🛐 Chal beta maafi maang | SHUBHANSH TMKC {heart}",
    "🤖 Spam Bot Activated | SHUBHANSH TMKC {heart}",
    "💥 Full Bakchodi Mode | SHUBHANSH TMKC {heart}",
    "🧠 IQ = Room Temp | SHUBHANSH TMKC {heart}"
]

# 🔍 Get first group chat where you're admin (manual check)
def get_top_gc_thread_id():
    my_id = cl.user_id
    threads = cl.direct_threads(amount=10)
    for thread in threads:
        if thread.is_group:
            # admin_ids is a list of admin user IDs
            if hasattr(thread, "admin_user_ids") and my_id in thread.admin_user_ids:
                return thread.id
    return None

# 🔁 GC Rename Loop
def start_auto_gc_rename():
    thread_id = get_top_gc_thread_id()
    if not thread_id:
        print("❌ No admin GC found.")
        return

    print(f"🚀 Changing GC name of thread: {thread_id}")

    while True:
        try:
            heart = random.choice(heart_colors)
            base_name = random.choice(base_group_names)
            new_name = base_name.format(heart=heart)
            cl.direct_thread_update_title(thread_id, new_name)
            print(f"✔️ Changed GC name to: {new_name}")
            time.sleep(random.randint(10, 20))  # Safe delay
        except Exception as e:
            print(f"⚠️ Error: {e}")
            time.sleep(60)

# ▶️ Run
start_auto_gc_rename()
