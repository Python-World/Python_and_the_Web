
# Instagram Bot <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e7/Instagram_logo_2016.svg/1200px-Instagram_logo_2016.svg.png" alt="Instagram_icon" width="45"  height="45">
	
#### It can perform the followng task:

1. **Give list of people** :
	- Who don't follow you back 
		- _Optional-> Unfollow them all_
	- Whom you don't follow back 
		- _Optional-> Follow back them all_

2. **Spamming bot** :
	- It can spam multiple people in a single input with the custom message you provide

It saves your user id and password in the same location as your `.py`/`.exe` as `Users.txt`, and don't worry, your user id might be readable to you but password is in the encrypted form

It also saves both of the list of above mentioned people in the form of simple text file.

For your convinience I added another file named `Pyinstaller_python.py` which on running converts the app into an `.exe` file which functions the same and it doesn't even have any prerequisites except for the web driver

It waits for 50 seconds if you have second authorization enabled

## Prerequisites

**To run the `Instagram_bot.py` file you need following stuff in your system:**

1. **[Python 3]**(https://www.python.org/downloads)

2. **Following python pakages**
    1. Selenium *{$ pip install selenium}*
    2. Cryptography *{$ pip install cryptography}*
    3. Pyinstaller (To convert it into `.exe` file) *{$ pip install pyinstaller}*
    
    Or, simply run `pip install -r requirements.txt` in your command prompt in the same directory as your `Instagram_bot.py` file

3. **Web driver of your respective browser**
    - If you have Chrome installed in your system then download the [Chrome webdriver](https://chromedriver.chromium.org/downloads).
	- Place web driver and the bot in the same directory or else bot will fail.

**After conversion by running `Pyinstaller_python.py`, yo run the `Instagram_bot.exe` file you need following stuff in your system:**

1. **You should have the `x64` bit OS.**

2. **Web driver of your respective browser**
    - If you have Chrome installed in your system then download the [Chrome webdriver](https://chromedriver.chromium.org/downloads).
	- Place web driver and the bot in the same directory or else bot will fail.

## How to run the script

1. It'll ask you to select/add/remove instagram user id.
2. With your chosen id, now you can 
	- Keep a track on your followers/following
	- Spam multiple person
- To create a `.exe` file, just run `Pyinstaller_python.py` file, but make sure you have all the pakages installed as mentioned above.
		
_Note:_
- Please make sure you opt the command/choice in form of numbers(1,2,3,4...), as the numbers will be mentioned in-front of the option_
- It is possible that in the 1st time use, your user id isn't shown even after adding it. In that case, just go for the option "Refresh(re)" or close and re-run the code/file.


### Screenshot/GIF showing the sample use of the script

#### When you open the app 1st time

<img src="MainPage.PNG" alt="MainPage">

#### After adding your username and password

<img src="LoginPage.png" alt="LoginPage">

#### Bot Commands available

<img src="MenuPage.png" alt="MenuPage">

#### Passwords stays safe(encrypted), even in your own computer

<img src="Users.png" alt="Users">

---------------------------------------

## *Author Name*

**Yash Joglekar**

GitHub username :- [YASHBRO](https://github.com/YASHBRO) 

<br/>

<img width="150px" src="https://sdk.bitmoji.com/render/panel/b6dbf504-c36d-498c-acf9-c7350b749221-23c927d9-4799-4bc6-9129-0d51a8a995de-v1.png?transparent=1&palette=1">
