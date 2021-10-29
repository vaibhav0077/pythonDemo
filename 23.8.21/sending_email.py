import smtplib
# smtpObj = smtplib.SMTP(host, port, local_hostname)  

sender_mail = "jadugarklal777@gmail.com"
receiver_mail = "jadugarklal777@gmail.com"

message = """From: From Person %s  
To: To Person %s  
Subject: Sending SMTP e-mail   
This is a test e-mail message.  
"""%(sender_mail,receiver_mail)

try:    
   smtpObj = smtplib.SMTP('gamil.com', 587)    
   smtpObj.sendmail(sender_mail, receiver_mail, message)    
   print("Successfully sent email")    
except Exception as e:    
   print("Error: unable to send email")
   print("\n\n" + e)    