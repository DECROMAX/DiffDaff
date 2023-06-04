from datetime import datetime

file_timestamp = f"{str(datetime.now().date())}_{str(datetime.now().time()).replace(':', '.')[:8]}"
