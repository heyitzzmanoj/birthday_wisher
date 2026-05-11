import smtplib
import datetime as dt 
import random 
import pandas
def send_mail(a,g_mail,message):
    my_email = "sutharm965.com@gmail.com"
    password = "hcccpzomltmwxqfq"
    
    connection = smtplib.SMTP("smtp.gmail.com",587)
    connection.starttls()
    connection.login(user=my_email,password=password)
    connection.sendmail(from_addr=my_email,to_addrs=g_mail,msg=message) 
    connection.close() 

date= dt.datetime.now() 
day= date.day
year= date.year
month= date.month
weekday = date.weekday()
print(year,month,day) 
bd = pandas.read_csv("birthday_data.csv")

with open("quotes.txt") as file:
    data = file.readlines() 
a=random.randint(0,101) 
dates = str(month)+"-"+str(day) 
bd_list = bd.date.to_list()
if dates in bd_list:
    d = bd[bd.date==dates] 
    email=d.email
    name = d.name.item()
    with open("massage.txt") as f:
        d= f.read()
        data=d.replace("name",name)
        
    
    send_mail(a,email,data)
    print(data)
 