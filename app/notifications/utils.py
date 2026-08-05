from datetime import datetime


def time_ago(dt):

    if dt is None:
        return ""

    now = datetime.utcnow()

    diff = now - dt

    seconds = int(diff.total_seconds())

    if seconds < 60:
        return "Just now"

    minutes = seconds // 60

    if minutes < 60:
        return f"{minutes} minute{'s' if minutes != 1 else ''} ago"

    hours = minutes // 60

    if hours < 24:
        return f"{hours} hour{'s' if hours != 1 else ''} ago"

    days = hours // 24

    if days == 1:
        return "Yesterday"

    if days < 30:
        return f"{days} days ago"

    months = days // 30

    if months < 12:
        return f"{months} month{'s' if months != 1 else ''} ago"

    years = months // 12

<<<<<<< HEAD
    return f"{years} year{'s' if years != 1 else ''} ago"
=======
    return f"{years} year{'s' if years != 1 else ''} ago"
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
