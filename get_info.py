import csv
f = csv.reader(open('template.csv', 'r'))
x = open('test.txt', 'w+')
next(f)
for i in f:
    name = i[1]
    num = i[0]
    strings =f"""adb shell am start -a android.intent.action.SENDTO -d sms:{num} --es sms_body 【现教计协】{name}同学你好，这里是现教中心计算机协会。我们将于10月14日星期三中午12:00～14:00在主教306进行面试（主教304为面试等候区），面试前请根据群内引导在校园网完成线上纳新注册。如有特殊情况无法前往，请联系QQ2446085188。
adb shell input keyevent 22
adb shell input keyevent 66"""
    x.write(strings)
    x.write("\n")