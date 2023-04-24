import smtplib
import time
import imaplib

M=imaplib.IMAP4_SSL('imap.gmail.com')
mail_id='lokie2301@gmail.com'
password=''

'''#creating an boject for the smtp
smtp_obj = smtplib.SMTP('smtp.gmail.com',587)
smtp_obj.starttls()
smtp_obj.login(mail_id,password)
smtp_obj.select('inbox')'''
M.login(mail_id,password)
M.select('inbox')
type,data=M.search(None,'UNSEEN')

print(type)
email_ids=data
for email_id in email_ids[0]:
    print(email_id)
    datas=M.fetch(email_id,'(RFC822)')
    msg=email.message_from_string(datas)
    re,email_data=M.store(email_id,'-FLAGS','\\Seen')

    print(email_data,re)
