import time
import datetime


def say_time():
    time.ctime()
    time_ = time.strftime('%H:%M%p')
    return time_


def say_date():
    cur_date = datetime.date.today().strftime("%d %B %Y")
    spec_dates = {"17:03", }
    spec_dates_prompts = {"17:03": f"It's my birthday."}
    if not spec_dates.issuperset(cur_date[:-5]):
        return f"Today's {cur_date}. It's just a regular day"
    else:
        return f"Today's {cur_date}. {spec_dates_prompts[cur_date[:-5]]}"