import smtplib
help(smtplib)
smtp_object = smtplib.SMTP('smtp.gmail.com', 587)
# smtp_object = smtplib.SMTP('localhost')
smtp_object.starttls()
smtp_object.login('katzxa@gmail.com','0505396291')

help(smtp_object.sendmail)
smtp_object.sendmail(from_addr="katzxa@gmail.com",
to_addrs="katzxa@mail.ru",
msg="It's works!")
smtp_object.sendmail(from_addr="katzxa.com",
to_addrs=["katzxa@gmail.com",'dd.petrovskiy@gmail.com'],
msg="I love you!")
smtp_object.quit()
