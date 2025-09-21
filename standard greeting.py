import time
t=time.strftime('%H:%M:%S')
print(t)
if time.strftime('%H:%M:%S') < time.strftime('12:00:00'):
    print("Good Morning")
elif time.strftime('%H:%M:%S') >= time.strftime('12:00:00'):
    print("Good Afternoon")
else:
    print("Good Evening")            