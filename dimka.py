import time

def a(user_time):
    while user_time >= 0:
        min, sec = divmod(user_time, 60)
        timer = '{:02d}:{:02d}'.format(min,sec)
        print(timer, end = '\r')
        time.sleep(1)
        user_time -= 1
    print('Timer end!')

if __name__ == '__main__':
    user_time = int(input('Введите время в секундах:'))
    a(user_time)
