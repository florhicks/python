import smtplib
email = ""
password =""
class Email():
    def __init__(self,name,email_address,phone_number, message):
        self.name = name
        self.email_address = email_address
        self.phone_number = phone_number
        self.message = message
        self.send_email()

    def send_email(self):
        email_message = (f"Subject:New Message\n\nName: {self.name}\nEmail: {self.email_address}"
                         f"\nPhone: {self.phone_number}\nMessage:{self.message}")
        print (email_message)
        # with smtplib.SMTP("smtp.gmail.com") as connection:
        #     connection.starttls()
        #     connection.login(email, password)
        #     connection.sendmail(email, password, email_message)