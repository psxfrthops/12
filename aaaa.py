import time

def greet_based_on_time(hour):
    if 0 <= hour < 6:
        return "نیمه شب بخیر"
    elif 6 <= hour < 12:
        return "صبح بخیر"
    elif 12 <= hour < 18:
        return "بعد از ظهر بخیر"
    elif 18 <= hour < 24:
        return "شب بخیر"
    else:
        return "سارا خانم، لطفا عددی در بازه ی ۰ تا ۲۴ وارد کن"

def get_hour_from_user():
    while True:
        try:
            hour = int(input("لطفا ساعت را وارد کنید (0 تا 24): "))
            if 0 <= hour <= 24:
                return hour
            else:
                print("سارا خانم، لطفا عددی در بازه ی ۰ تا ۲۴ وارد کن")
        except ValueError:
            print("لطفا یک عدد صحیح وارد کنید.")

def main():
    print("سلام سارا! لطفا یکی از گزینه‌های زیر را انتخاب کن:")
    print("الف) وارد نمودن دستی ساعت")
    print("ب) خود کامیپیوتر ساعت رو اتوماتیک در برنامه درج کن")
    choice = input("لطفا 'الف' یا 'ب' را وارد کن: ")

    if choice == 'الف':
        hour = get_hour_from_user()
        print(greet_based_on_time(hour))
    elif choice == 'ب':
        current_hour = time.localtime().tm_hour  # گرفتن ساعت فعلی از سیستم
        print(f"ساعت فعلی: {current_hour}")
        print(greet_based_on_time(current_hour))
    else:
        print("لطفا فقط 'الف' یا 'ب' را وارد کنید.")
