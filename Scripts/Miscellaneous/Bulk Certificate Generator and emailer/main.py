import email.message as em
import getpass
import re
import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import pandas as pd
from PIL import Image, ImageDraw, ImageFont


def mail(df, from_, password):
    msg = em.Message()
    msg.add_header("Content-Type", "text/html")

    to = df["Email"].to_list()
    name = df["Name"].to_list()

    to_length = len(to)

    try:
        server = smtplib.SMTP(
            "smtp.outlook.com", 587
        )  # Change it to gamil or yahoo as per requirement
        server.starttls()
        server.login(from_, password)
        print("Login Succesfull \n")

        for i, j in zip(to, name):
            print("" + str(to_length) + " left \n")
            print("Sending to {}".format(j))

            data = MIMEMultipart()
            data["To"] = i
            data["From"] = from_
            data["Subject"] = "Certificate"  # Change subject

            body = "Sample Body"  # Change email body
            data.attach(MIMEText(body, "plain"))

            p = "pictures/{}.png".format(j)
            filename = p

            with open(filename) as f:
                attachment = f.read()

            #             attachment = open(filename, "rb")

            p = MIMEBase("application", "octet-stream")

            p.set_payload((attachment).read())

            encoders.encode_base64(p)

            name = re.split("/", filename)[-1]
            p.add_header(
                "Content-Disposition", "attachment; filename= %s" % name
            )

            data.attach(p)

            text = data.as_string()
            server.sendmail(from_, i, text)
            attachment.close()
            print("Sent \n")
            to_length -= 1

        server.quit()

    except:
        print("Make sure have an active internet connection")
        print("Please check your credentials")


def generate_certificate(df):
    font = ImageFont.truetype("Caveat-Bold.ttf", 120)
    for j in df["Name"]:
        img = Image.open("certificate_template.png")
        draw = ImageDraw.Draw(img)
        draw.text(
            xy=(151, 560), text="{}".format(j), fill=(0, 217, 225), font=font
        )
        img.save("pictures/{}.png".format(j))


CSV_PATH = input("Enter the .csv file path: ")

from_ = input("Enter your email address: ")
password = getpass.getpass(prompt="Enter your password: ")

print("\n")

df = pd.read_csv(CSV_PATH)
generate_certificate(df)
mail(df, from_, password)
