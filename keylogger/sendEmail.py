import smtplib

def sendMail(message):

    # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)

    # start TLS for security
    s.starttls()

    # Authentication
    s.login("Email adress of Gmail", "Pass Of Gmail(Not regular Pass Login")

    # sending the mail
    s.sendmail("From", "TO", message)

    # terminating the session
    s.quit()
