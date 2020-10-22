# Hacking-Toolbox
This is in heavy work, it is constantly getting updated :)

Tools:

main.py:

1. Discord Spamming Tool(SelfBot):

A selfbot that does five things:

a. Spams a guild chat with `-spamstart` The setting for this are set when the script is launched.

b. Pings all the roles in a guild with `-massroleping`

c. Dms a user with `-spamuser {message} {amount of times} {userid}`

For example:
`-spamuser test 1 768217411643506688`

d. Dms eveyone that sends a message, this Dm message is set when the script is run. If your enter nothing, it will defaut to: `:wave: Why, hello there :wave:`

This can be turned off and on in line 16 of `Mass-Dmer.py` If autodm is set to `'1'` it will Dm, If autodm is set to `'0'` it will not Dm. This is set to `'0'` by defaut.

e. Spams a guild chat with `-spam`. Format is `-spam {message} {amount of times}`

For example:
`-spam hi 2`

2. Discord Alt and token generator:

--THIS IS NOT FULLY AUTOMATIC--
It creates accounts and saves the token to tokens.txt, and the email and password to username_and_passwords.txt
You will need to do two things: 
Complete the catcha, and enter the date. When entering the date, do NOT press the confirm button, the script will.

3. Discord Email Verifier:

Gives you a email, use this email when you sign up, and the email with be automatically verified. 
This relies on 1secmail.com

4. Discord Token Checker:

Checks the tokens in the tokens.txt file

5. Discord Token Grabber:

Gives you the Discord Account Token bassed on a email and password

6. Discord Token Login Tool:

This is one of my favorite, it opens a Chrome borwser and logs in with a Discord Token.
**You Must have chrome installed**


If you think I messuped with somthing, or this Readme in incompleate, please make a Issue. 

Credits:

I didn't make LocalStorage.py and DiscordAccount.py, I cant remember who did. 

# Disclaimer
## I, the creator, am in no way responsible for any actions that you may make using this software. You take full responsibility with any action taken using this software. Please take note that this application was designed for educational purposes and should never be used maliciously. By downloading the software or source to the software, you automatically accept this agreement.
## Most of these tools are against discord's terms of service, the accounts used can and will get banned.
