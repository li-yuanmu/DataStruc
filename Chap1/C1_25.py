#删除标点符号
import re

string = "Let's try, mike"

print(re.sub("[,'.]"," ",string))
