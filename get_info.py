import csv
f = csv.reader(open('template.csv', 'r'))
x = open('test.txt', 'w+')
next(f)
for i in f:
    name = i[1]
    num = i[0]
    strings =f"""adb shell am start -a android.intent.action.SENDTO -d sms:{num} --es sms_body 【xxx】{name}同学你好，这里是xxxxx。
adb shell input keyevent 22
adb shell input keyevent 66"""
    x.write(strings)
    x.write("\n")
