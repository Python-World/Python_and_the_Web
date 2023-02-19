def mail():
  #import all required package
  import smtplib
  import random
  from email.mime.multipart import MIMEMultipart
  from email.mime.text import MIMEText
  from email.mime.image import MIMEImage
  otp=random.randint(1000,10000)

#content of mail
  content1 = '''<p><u><h3>The verification code OTP -<mark> {} </mark> </h3></u></p>\n<b>*Note</b> :<br>&nbsp;&nbsp;&nbsp; Do not share your one-time password (OTP)]\n<br>&nbsp;&nbsp;&nbsp; with anyone over phone or e-mail \n<br>&nbsp;&nbsp;&nbsp; as this could lead to fraud.'''.format(otp)
  content2 = "*Please read: \n            If you did not initiate the request, you do not \n            need to take any further action and can \n            safely disregard this email.\n\n"
  content3 =" <b>Thanks<br>HelpYourself</b><br>  <b>***No reply mail.</b>.<br> &ensp;&ensp;&ensp;This is system generated mail do not reply to it."
 
  sender= 'xyz@gmail.com'#replace with the mail of sender
  passward = 'hzvwm'#replace with your sthird party permission passward of sender email
  receiver = 'abc@gmail.com'#replace with receivers email
  
  message = MIMEMultipart()
  message['Subject'] = 'Please verify your email.'# replace with the subject of your mail
  message.attach(MIMEText(content1, 'html'))

  msgAlt = MIMEMultipart('alternative')
  message.attach(msgAlt)

  msgText = MIMEText('Something went wrong.\nImage cannot be displayed')
  msgAlt.attach(msgText)

  msgText = MIMEText('<b> <i></i> <br><br><img src="cid:image1"></b><br>', 'html')
  msgAlt.attach(msgText)

# place image in current directory
  fp = open('logo baymax_.jpg', 'rb')# add image name you want to attach in mail
  msgImage = MIMEImage(fp.read())
  fp.close()

  msgImage.add_header('Content-ID', '<image1>')
  message.attach(msgImage)

  message.attach(MIMEText(content2, 'plain'))
  message.attach(MIMEText(content3, 'html'))
  session = smtplib.SMTP('smtp.gmail.com', 587)
  session.starttls()
  session.login(sender, passward)
  text = message.as_string()
  session.sendmail(sender, receiver, text)
  session.quit()
  print('Mail Sent')
  
  
mail()
