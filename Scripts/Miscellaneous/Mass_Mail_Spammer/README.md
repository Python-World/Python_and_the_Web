# Mass Mail Spammer
A python + expect script to send any number of trash emails from your google account, with custom/random trash messages (can also be taken from a file) to any target.<br>
The connection is made via secure openssl to GSMTP. Google accepts the credentials in base64 and TLS connection<br>
<b>Make sure that use have enabled less secure app access in your google account</b><br>
There are 3 options to send the messages :<br>
1. Random Messages<br>
2. Custom user defined<br>
3. From a files<br>
Basic error handling has also been done<br>

## Prerequisites
Expect<br>
// On Debian based systems<br>
`sudo apt install expect`<br>

// On Redhat based systems<br>
`sudo yum install expect`<br>

## Usage
`python3 main.py`<br>
<b>Also, the passwd field will remain empty when you type your gmail passwd</b><br>
(as a matter of privacy)


## Screenshots
The screenshots are blurred to hide the sensitive info<br>
  
![image not found](img1.png)<br>
![image not found](img2.png)<br>

## Author name
#### Ritik Malik

