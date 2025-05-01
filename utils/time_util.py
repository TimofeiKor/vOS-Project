import time

def cTime():
    try:
        return time.ctime()
    except Exception as e:
        print(f"Ошибка получения времени: {e}")
        return None