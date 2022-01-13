import imaplib
import email
from email.header import decode_header

# account credentials
username = "abc@example.com"
password = "Pandaeats@1"

a = imaplib.IMAP4_SSL("imap.gmail.com")
a.login(username,password)
a.select("INBOX")

status,messages = a.search(None, 'BEFORE "13-JAN-2020"')
messages = messages[0].split(b' ')
_, msg = a.fetch(email, "(RFC822)")


for response in msg:
    if isinstance(response, tuple):
        msg = email.message_from_bytes(response[1])
        subject = decode_header(msg["Subject"])[0][0]

        if isinstance(subject, bytes):
            subject = subject.decode()
        print("Deleting", subject)

a.store(mail, "+FLAGS", "\\Deleted")
a.expunge()
a.close()
a.logout()