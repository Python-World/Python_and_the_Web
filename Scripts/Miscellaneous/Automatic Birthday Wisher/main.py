# import required packages
import datetime
import smtplib

import pandas as pd

# your gmail credentials here
GMAIL_ID = "Your-Gmail-Id"
GMAIL_PWD = "Your-Gmail-Password"


# function for sending email
def sendEmail(to, sub, msg):
    # conncection to gmail
    gmail_obj = smtplib.SMTP("smtp.gmail.com", 587)
    # starting the session
    gmail_obj.starttls()
    # login using credentials
    gmail_obj.login(GMAIL_ID, GMAIL_PWD)
    # sending email
    gmail_obj.sendmail(GMAIL_ID, to, f"Subject : {sub}\n\n{msg}")
    # quit the session
    gmail_obj.quit()
    # printing to check whether email is sent or not
    print(
        "Email sent to "
        + str(to)
        + " with subject "
        + str(sub)
        + " and message :"
        + str(msg)
    )


# driver code
if __name__ == "__main__":
    # read the excel sheet having all the details
    dataframe = pd.read_excel("Path-of-your-excel-sheet")
    # fetching  todays date in format : DD-MM
    today = datetime.datetime.now().strftime("%d-%m")
    # fetching current year in format : YY
    yearNow = datetime.datetime.now().strftime("%Y")
    # writeindex list to avoid spamming of mails
    writeInd = []
    for index, item in dataframe.iterrows():
        msg = "Many Many Happy Returns of the day dear " + str(item["Name"])
        # stripping the birthday in excel sheet as : DD-MM
        bday = item["Birthday"].strftime("%d-%m")
        # condition checking for today birthday
        if (today == bday) and yearNow not in str(item["Year"]):
            # calling the sendEmail function
            sendEmail(item["Email"], "Happy Birthday", msg)
            writeInd.append(index)
    for i in writeInd:
        yr = dataframe.loc[i, "Year"]
        # this will record the years in which email has been sent
        dataframe.loc[i, "Year"] = str(yr) + "," + str(yearNow)

    dataframe.to_excel("Path-of-your-excel-sheet", index=False)
