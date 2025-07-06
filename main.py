from instagrapi import Client
import time
import random

# Login to Instagram
cl = Client()
cl.login_by_sessionid("70016257168%3AM6nSnozvM5Bg2H%3A29%3AAYe0gCJZkBuwV_gmYH-5eX8gft7dmvg-5BWGrySBfg")  # 🔐 Replace this with your session ID

# List of GC names to rotate
group_names = [
    "𝐍𝐈𝐂𝐊 𝐓𝐄𝐑𝐈 𝐌𝐀 𝐊𝐈 𝐂𝐇𝐔𝐓❤︎",
    "𝐍𝐈𝐂𝐊 𝐓𝐄𝐑𝐈 𝐌𝐀 𝐊𝐈 𝐂𝐇𝐔𝐓✿︎",
    "𝐍𝐈𝐂𝐊 𝐓𝐄𝐑𝐈 𝐌𝐀 𝐊𝐈 𝐂𝐇𝐔𝐓🝮︎︎︎︎︎︎︎",
    "𝐍𝐈𝐂𝐊 𝐓𝐄𝐑𝐈 𝐌𝐀 𝐊𝐈 𝐂𝐇𝐔𝐓㋛︎",
    "𝐍𝐈𝐂𝐊 𝐓𝐄𝐑𝐈 𝐌𝐀 𝐊𝐈 𝐂𝐇𝐔𝐓❦︎",
    "𝐍𝐈𝐂𝐊 𝐓𝐄𝐑𝐈 𝐌𝐀 𝐊𝐈 𝐂𝐇𝐔𝐓𓆉︎",
    "𝐍𝐈𝐂𝐊 𝐓𝐄𝐑𝐈 𝐌𝐀 𝐊𝐈 𝐂𝐇𝐔𝐓✵",
    "𝐍𝐈𝐂𝐊 𝐓𝐄𝐑𝐈 𝐌𝐀 𝐊𝐈 𝐂𝐇𝐔𝐓𖣘",
    "𝐍𝐈𝐂𝐊 𝐓𝐄𝐑𝐈 𝐌𝐀 𝐊𝐈 𝐂𝐇𝐔𝐓❁",
    "𝐍𝐈𝐂𝐊 𝐓𝐄𝐑𝐈 𝐌𝐀 𝐊𝐈 𝐂𝐇𝐔𝐓𓆈"
]

# Function to get top GC thread ID
def get_gc_thread_id():
    threads = cl.direct_threads(amount=5)
    for thread in threads:
        if thread.is_group:
            return thread.id
    return None

# Auto name changer
def start_auto_gc_rename():
    thread_id = get_gc_thread_id()
    if not thread_id:
        print("❌ No group chat found.")
        return

    print(f"🚀 Changing GC Name of: {thread_id}")

    while True:
        try:
            new_name = random.choice(group_names)
            cl.direct_thread_update_title(thread_id, new_name)
            print(f"✔️ Changed GC name to: {new_name}")
            time.sleep(random.randint(10, 20))  # Delay between changes
        except Exception as e:
            print(f"⚠️ Error: {e}")
            time.sleep(60)

# ▶️ Start bot
start_auto_gc_rename()
