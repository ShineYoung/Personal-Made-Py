import datetime
import time

def days(date):
    date=date.split(' ')  # 输入到期日时，请用空格隔开年 月 日
    if len(date)!=3:
        return False
    else:
        year=int(date[0])
        month=int(date[1])
        day=int(date[2])
        return year,month,day

def be_days(date0):
    days1=datetime.date(days(date0)[0],days(date0)[1],days(date0)[2])
    days2=datetime.date.today()
    return abs(days2-days1)

def counter(principal, rate):
	sum_rate = principal * ( 1 + rate * d / 360 )
	return sum_rate 
    
    
date0=input('please input a date:\n>')
principal = float(input('please input the principal:\n>'))
rate = float(input('please input the rate:\n>'))
d = int(str(be_days(date0))[0:2])
print(counter(principal, rate))




