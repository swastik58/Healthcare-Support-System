import smtplib as smt 
from passutil import password,email,destination

# Email Integration
def MailSender(total):
    ob=smt.SMTP("smtp.gmail.com",587)
    ob.starttls()
    ob.login(email,password)
    if(total==1):
        subject="Dietary Assistance for Patient"
        body="Patient XYZ Requires water/medicine"
        message="Subject:{}\n{}\n".format(subject,body)
        ob.sendmail(email,destination,message)
    elif(total==2):
        subject="Basic Assistance for Patient"
        body="Patient XYZ Requires attention/help for going to washroom"
        message="Subject:{}\n{}\n".format(subject,body)
        ob.sendmail(email,destination,message)
        ob.quit()
    elif(total==3):
        subject="Immediate Medical Attention Required"
        body="Patient XYZ is in critical condition and needs medical attention immediately"
        message="Subject:{}\n{}\n".format(subject,body)
        ob.sendmail(email,destination,message)
        ob.quit()
