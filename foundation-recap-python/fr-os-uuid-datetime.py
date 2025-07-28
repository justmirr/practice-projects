# os - path handling, file checks, uuid - generate unique request/session IDs, datetime - time-based queries, filtering

import uuid
import os
from datetime import datetime

session_id = uuid.uuid4()
now = datetime.now().strftime("%Y-%m-%d")

print(session_id, now)

folder_name = f"session_{now}_{session_id}"
os.makedirs(folder_name, exist_ok=True)

print(f"directory: {folder_name} created successfully")