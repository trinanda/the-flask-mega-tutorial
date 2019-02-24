# Flask-Microblog

#### Instalation process
```bash
$ git https://github.com/trinanda/Flask-Microblog.git
$ cd Flask-Microblog
```
#### Export credential
Create **.env** file in the root directory, then export the credential that needed for this app.
The **.env** file contains few credential and configuration like this:
```.env
SECRET_KEY=Learn-with-1%-everyday-in-one-years-your-skill-will-be-upgraded-365%.
MAIL_SERVER=smtp.googlemail.com
MAIL_PORT=587
MAIL_USE_TLS=1
MAIL_USERNAME='example@gmail.com'
MAIL_PASSWORD='your_mail_password'
MS_TRANSLATOR_KEY='YOUR_MS_TRANSLATOR_KEY'
```
- You can get the **MS_TRANSLATOR_KEY** in your Azure account, you can find it here: https://azure.microsoft.com/en-us/
- **Note**: If you don't have the account and try to create one, you will need to provide your credit card, 
but Microsoft offering has an entry level option for low volume of translations that is free. 
Don't worry if you don't have the credit card, this is not too important for this app in mean you can skip this option without **MS_TRANSLATOR_KEY**. 
You will only lose one feature in this app which is instans translate for each users posts and without it you still can running your app perfectly.
#### Run the app
```bash
$ flask run
```

#### Feature
1. Follow/Unfollow Users
2. Database migrations
3. Unit testing
4. Profile page with avatars using Gravatar
5. Error handling
   - Sending error by email if error occurred on the app
   - Maintain a log file for the application using stacktrace
6. Password reset
   - Requesting a reset password
   - Password reset tokens using JWT
   - Sending a password reset email
7. Asynchronous emails
8. Last seen users online
9. I18n and L10n
10. Translate users posts using Microsoft Translator Text API and using Ajax to get instants translate

#### Next Feature
1. Deployment on Linux, Heroku and Docker Containers
2. User Notifications
3. Background Jobs

##### The other things
If you want to make some changes in your models don't forget to test your app before.

```bash
$ python3 test.py
```
and then running the db migrate and upgrade command
```bash
$ flask db migrate
$ flask db upgrade
```

##### Big thanks to Miguel Grinberg for this great tutorial 
The Flask Mega-Tutorial https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world
