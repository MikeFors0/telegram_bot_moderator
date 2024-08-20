import re
from datetime import datetime, timedelta


def parse_time(time: str | None):
    if not time: return None

    re_match = re.match(r"(\d+)([a-z])", time.lower().strip())
    now_datetime = datetime.now()

    if re_match:
        value = int(re_match.group(1))
        unit = re_match.group(2)

        match unit:
            case "h": time_delta = timedelta(hours=value)
            case "d": time_delta = timedelta(days=value)
            case "w": time_delta = timedelta(weeks=value)
            case _: return None
    else:
        return None
    
    new_datetime = now_datetime + time_delta
    return new_datetime



