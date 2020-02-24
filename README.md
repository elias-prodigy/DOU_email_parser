# DOU_email_parser
Small script which parses emails of all agencies registered in Zaporozhye on DOU.ua website.

You can simply adjust it for your city by following these steps:
1) Download the project from my repo
2) Install all requirements into your virtual environment
3) Download and install the Chrome Browser
4) Download the latest version of chromedriver and put it in the root path of your project.
https://chromedriver.chromium.org/downloads
5) In the file parser.py in the line12, change the path to your chromedriver basing on your situation.
6) And finally in the file parser.py in the line13, change the URL basing on your needs.
For example: proceed to this link https://jobs.dou.ua/companies/ and type in the search field any city you want to 'parse emails' and press Enter button. 
Than just copy/paste the link from browser to line13.
7) Now you can execute the parser.py file by running the command 'python3 parser.py'


NOTE
1) The process of the email parsing can take some time, up to 10 minutes, depends on the hardware and the amount of companies you're trying to parse. 
PLEASE don't interrupt the working process until you'll see the new CLI in the terminal.
2) This parser can be used either with any other Browser, but the installation guide in points 3 and 4 should be changed respectively.
