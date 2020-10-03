import feedparser
from twilio.rest import Client



SID= 'my_SID' #Twilio SID
auth = 'my_auth_token' #Twilio Authentication Token
twilio_number = "your twilio number"
phone_number = "receiving phone number"

news = feedparser.parse('https://www.hltv.org/rss/news')
cl = Client(SID,auth)

print("Number of News: " + str(len(news.entries)))

for i in range(10):
    entry = news.entries[i]
    
    print(entry.keys())
    
    
    
    title = "*"+entry.title+"*"
    body = entry.summary_detail['value']
    link = entry.link
    
    
    msg = title+ "\n\n\n" + body + "\n\n\n" + link
    
    
    
    message = cl.messages.create(from_="whatsapp:"+str(twilio_number),body = msg,to="whatsapp:"+str(phone_number))
    
    print(message.sid)
    

