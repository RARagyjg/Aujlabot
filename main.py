from instagrapi import Client
import time
import random

# Login
cl = Client()
cl.login_by_sessionid("70016257168%3AM6nSnozvM5Bg2H%3A29%3AAYe0gCJZkBuwV_gmYH-5eX8gft7dmvg-5BWGrySBfg")  # Replace with real session ID

# GC Names
group_names = [
    "𝐒𝐇𝐔𝐁𝐇𝐀𝐍𝐒𝐇 𝐓𝐄𝐑𝐈 𝐓𝐌𝐊𝐂🟣",
    "𝐒𝐇𝐔𝐁𝐇𝐀𝐍𝐒𝐇 𝐓𝐄𝐑𝐈 𝐓𝐌𝐊𝐂🔵",
    "𝐒𝐇𝐔𝐁𝐇𝐀𝐍𝐒𝐇 𝐓𝐄𝐑𝐈 𝐓𝐌𝐊𝐂🟢",
    "𝐒𝐇𝐔𝐁𝐇𝐀𝐍𝐒𝐇 𝐓𝐄𝐑𝐈 𝐓𝐌𝐊𝐂🟡",
    "𝐒𝐇𝐔𝐁𝐇𝐀𝐍𝐒𝐇 𝐓𝐄𝐑𝐈 𝐓𝐌𝐊𝐂🟠"
]

# Get GC thread ID
def get_gc_thread_id():
    threads = cl.direct_threads(amount=10)
    for thread in threads:
        if thread.is_group:
            return thread.id
    return None

# Start GC renamer
def start_auto_gc_rename():
    thread_id = get_gc_thread_id()
    if not thread_id:
        print("❌ No GC found.")
        return

    print(f"🚀 Trying GC name change in: {thread_id}")

    while True:
        try:
            new_name = random.choice(group_names)
            # Using thread_update instead of thread_update_title (try this workaround)
            cl.private_request(
                "direct_v2/threads/update_title/",
                {
                    "thread_id": thread_id,
                    "title": new_name
                }
            )
            print(f"✔️ Changed GC name to: {new_name}")
            time.sleep(random.randint(25, 40))
        except Exception as e:
            print(f"⚠️ Error while changing GC name: {e}")
            time.sleep(60)

# Run
start_auto_gc_rename()
