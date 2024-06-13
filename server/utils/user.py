import hashlib
import random
import string
import smtplib

from email.mime.text import MIMEText

def hash_password(password):
    input_bytes = password.encode('utf-8')
    sha256_object = hashlib.sha256()
    sha256_object.update(input_bytes)
    hashed_output = sha256_object.hexdigest()

    return hashed_output


def generate_random_string():
    characters = string.ascii_letters + string.digits + string.punctuation
    random_string = ''.join(random.choice(characters) for _ in range(10))
    
    return random_string


def send_email(subject, body, sender, receiver, key):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = receiver

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender, key)
    server.sendmail(sender, receiver, msg.as_string())

    return True
