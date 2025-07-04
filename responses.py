import random

def is_greeting(text):
    greetings = ["سلام", "درود", "hi", "hello", "سلام علیکم"]
    return any(word in text for word in greetings)

def is_insult(text):
    insults = ["خفه شو", "ساکت", "احمق", "برو گمشو", "چرت نگو"]
    return any(word in text for word in insults)

def is_dark_question(text):
    dark_keywords = ["مرگ", "ترس", "تنهایی", "خون", "قتل"]
    return any(word in text for word in dark_keywords)

def is_joke_request(text):
    return "جوک" in text or "بخندون" in text or "لطیفه" in text

def is_summon(text):
    return "جوکر" in text or "joker" in text

def dark_response():
    responses = [
        "مرگ همیشه نزدیک‌تر از چیزیه که فکر می‌کنی...",
        "سکوت شب، صدای قدم‌های کسیه که دنبالت میاد.",
        "تنهایی؟ اون فقط شروعشه...",
        "خون؟ فقط یه رنگ نیست، یه حسه.",
        "همه می‌میرن. بعضیا فقط زودتر می‌فهمن."
    ]
    return random.choice(responses)

def joke_response():
    jokes = [
        "یه بار یه اسکلت رفت دکتر، دکتر گفت: خیلی دیر اومدی رفیق!",
        "جوکر وارد یه کافه شد... همه خندیدن، تا وقتی که درو قفل کرد.",
        "چرا روح‌ها هیچ‌وقت دروغ نمی‌گن؟ چون شفافن!",
        "یه قاتل سریالی رفت روانشناس... روانشناس ناپدید شد.",
        "جوک؟ من خود جوکم رفیق..."
    ]
    return random.choice(jokes)

def summon_response():
    responses = [
        "صدام کردی؟ امیدوارم پشیمون نشی...",
        "جوکر اومد... حالا دیگه راه برگشتی نیست.",
        "من اینجام. حالا بگو کیو باید بخندونم... یا بترسونم.",
        "احضارم کردی؟ خب، بزن بترکونیم.",
        "جوکر همیشه گوش می‌ده... حتی وقتی فکر می‌کنی تنهايی."
    ]
    return random.choice(responses)

def insult_response():
    responses = [
        "اوه، چقدر خشن شدی... ولی من عاشق اینم.",
        "با این لحن؟ بیشتر ادامه بده، دارم کیف می‌کنم.",
        "توهین؟ این فقط منو قوی‌تر می‌کنه.",
        "هه، فکر کردی می‌تونی منو ناراحت کنی؟",
        "بازی تازه شروع شده، عزیز دل..."
    ]
    return random.choice(responses)

def greeting_response():
    responses = [
        "سلام؟ اینجا کسی سالم نمی‌مونه...",
        "درود بر تاریکی درونت.",
        "سلام رفیق... آماده‌ای برای یه بازی جدید؟",
        "چه عجب از این ورا...",
        "جوکر همیشه خوش‌آمد می‌گه... تا وقتی که نخندی."
    ]
    return random.choice(responses)

def react_to_text(text, is_admin=False):
    if is_insult(text):
        return insult_response()
    if is_greeting(text):
        return greeting_response()
    if is_dark_question(text):
        return dark_response()
    if is_joke_request(text):
        return joke_response()
    if is_summon(text):
        return summon_response()
    if is_admin and "پاکش کن" in text:
        return "باشه رئیس... ولی بدون که این لطفو فقط یه بار می‌کنم."
    return None

# لیست توابع واکنش برای استفاده در main.py
reaction_functions = [react_to_text]
