
## Deploy

### Easy Method
[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/new/template/Y1pXr6?referralCode=GishanKrishka) [![Deploy on Heroku](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/Gishankrishka/Movie_Finder/)

### Hard Method
```sh
# Install Git First (apt-instll git)
$ git clone https://github.com/Gishankrishka/Movie_Finder/
$ cd Movie_Finder
# Install All Requirements 
$ pip3 install -r requirements.txt
# Add Your Details to ./Movie_Finder/vars.py
# Start Bot 
$ python3 -m alpha
```
##### Mandatory Vars
```
[+] Make Sure You Add All These Mandatory Vars. 
    [-] API_ID:   You can get this value from my.telegram.org
    [-] API_HASH :   You can get this value from my.telegram.org
    [-] FDBURL : Your Firebase DataBase Url. (You can get this value from console.firebase.google.com)
    [-] BOT_TOKEN: Get from @BotFather
    [-] LOG_CHNL: Your Log Channel ID. (Make sure bot is admin in channel)
    [-] BOT_USERNAME: Bot Username.
[+] The bot won't run without setting the mandatory vars.
```

## Important ⚠

[+] Go to console.firebase.google.com & Go to Your Project & Go to Project Settings & Go to Service Accounts & Click on <b>Generate New Private Key</b> & It will Download your Database Credentials File & Then rename it to Database.json & Put it on main directory on MissRaya. MissRaya won't work if you don't put it correctly.

[+] You Must Need To Create Some Keys on Firebase Realtime Database. It's on down below pitcure👇
<p align="center">
  <img src="https://user-images.githubusercontent.com/90763454/169789605-70b386ca-ebe6-4aa2-a2b2-d01b5120f1e5.png"> 
</p>

[+] And then you need to Admins in database as like this👇. You must need at least one admin on bot. You can add new admins through bot after you deployed.
<p align="center">
  <img src="https://user-images.githubusercontent.com/90763454/169789380-d229f6d1-f52c-4033-a930-0dc4d99e0cb5.png"> 
</p>


##### Should any be missing kindly let us know at [Developers](https://t.me/Gishankrishka) or simply submit a pull request on the readme.

# Contributors
![GitHub Contributors Image](https://contrib.rocks/image?repo=Gishankrishka/Movie_Finder/))

