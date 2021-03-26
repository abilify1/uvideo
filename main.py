#-*-coding:utf-8-*-
try:
 import os,requests, inquirer
 import sys
 import time
 from bs4 import BeautifulSoup as bs
except: os.system("pip2 install requests inquirer bs4")
qu = '\033[0;36m'
hi = '\033[0;32m'
pu = '\033[0;37m'
me = '\033[0;31m'
ku = '\033[0;33m'

def downloadFile(url, directory,dir2) :
 ws = bs(requests.get(url).text,'html.parser')
 judul = ws.find("h1",{'itemprop':'title'}).getText().rstrip()
 link = ws.find("div","download-placement").a["href"]
 user = ws.find_all('a', href=True)[9].getText().rstrip()
 view = ws.find("span",{'id':'video-views-count'}).getText()
 print "%s[%s!%s] %sJudul : %s%s %s| %sDiunggah oleh %s%s %s| %s%s %sviews"%(pu,me,pu,qu,ku,judul,pu,qu,ku,user,pu,ku,view,qu)
 desc = ws.find("p",{'itemprop':'description'}).getText()
 print ("%s[%s!%s] %sDescription : %s%s"%(pu,me,pu,qu,ku,desc))
 with open(directory+"/"+dir2, 'wb') as f:
  start = time.clock()
  we = time.time()
  while True:
   try:
    r = requests.get(link, headers={'user-agent':'Mozilla/5.0 (Linux; Android 9; vivo 1902) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.181 Mobile Safari/537.36'},stream=True)
    total_length = r.headers.get('content-length')
    print "%s[%s!%s] %sUkuran file : %s%s MB"%(pu,me,pu,qu,ku,str(int(total_length) / 1024 / 1024))
    print "%s[%s!%s] %sSedang mendownload file sebagai %s%s %sdi folder %s%s"%(pu,me,pu,qu,ku,dir2,qu,ku,directory)
    dl = 0
    if total_length is None:
      f.write(r.content)
    else:
      for chunk in r.iter_content(1024):
        dl += len(chunk)
        f.write(chunk)
        done = int(20 * dl / int(total_length))
        sys.stdout.write("\r%s[%s%s%s%s] %s%s %skbps" % (pu,hi,'▭' * done, ' ' * (20-done),pu,ku, dl//(time.clock() - start) / 1024,qu))
        sys.stdout.flush()
   except: print ("%s[%s!%s] %sTerjadi kesalahan, mengulangi..."%(pu,me,pu,me));continue
   else: break
 return (time.time() - we)

def searchmode():
 
 key = raw_input("%s[%s?%s] %sMasukkan keyword : %s"%(pu,me,pu,qu,hi))
 ry = bs(requests.get("https://www.uvideo.xyz/search?keyword=%s"%key).text,'html.parser')
 o = ry.findAll("div",{'class':'video-title'})
 ppl = len(o)
 pap = 0
 w = 0
 for oo in range(len(o)):
  woi = o[pap].a["href"]
  if "@" in woi:ppl -= 1;continue
  pap += 1
 if len(o) < 1: exit("%s[%s!%s] %sTidak ditemukan!!"%(pu,me,pu,me))
 print ("%s[%s!%s] %sDitemukan %s%s %svideo"%(pu,me,pu,qu,ku,str(ppl),qu))
 lin = []
 for x in range(len(o)):
  woy = o[w].a["href"]
  if "@" in woy: continue
  lin.append(woy)
  print "%s• %s(%s%s%s). %s%s"%(hi,pu,me,str(w),pu,ku,o[w].find("h4").getText().encode('utf-8'))
  w += 1
 waw = raw_input("%s[%s?%s] %sSilahkan pilih berdasarkan nomor : %s"%(pu,me,pu,qu,hi))
 url = lin[int(waw)]
 try:
  time_elapsed = downloadFile(url, "/sdcard/Download/",o[int(waw)].find("h4").getText().encode('utf-8')+".mp4")
 except:exit("%s[%s!%s] %sTerjadi error, ini adalah channel bukan video!!"%(pu,me,pu,me))
 print "\n%s[%s!%s] %sDownload selesai..."%(pu,me,pu,hi)
 print "%s[%s!%s] %sWaktu Terpakai: %s%s %sdetik"%(pu,me,pu,qu,ku,str(time_elapsed),qu)

def main() :
 tyn = inquirer.prompt([inquirer.List('tanya',message=qu+'Pilih mode',choices=["Input by url","Search by keyword"],),])["tanya"]
 if tyn == "Input by url":
  while True:
   url = raw_input("%s[%s!%s] %sMasukkan URL : %s"%(pu,me,pu,qu,hi))
   if not url.startswith(tuple(["https://uvideo.xyz","https://www.uvideo.xyz"])): print ("%s[%s!%s] %sURL salah\n%s[%s!%s] %sContoh url yg benar : %shttps://www.uvideo.xyz/watch/21-bridges-2019-dubbing-indonesia_iBhWhkHmeD4bBxm.html"%(pu,me,pu,me,pu,me,pu,qu,ku))
   else: break
  while True:
   global directory
   global dir2
   directory = raw_input("%s[%s?%s] %sSimpan file ke folder ? %s"%(pu,me,pu,qu,hi))
   dir2 = raw_input("%s[%s?%s] %sSimpan file sebagai ? %s"%(pu,me,pu,qu,hi))
   try:
    open(directory+"/"+dir2,"wb+").write(" ")
   except: exit("%s[%s!%s] %sFile tidak dapat ditemukan"%(pu,me,pu,me))
   break
  time_elapsed = downloadFile(url, directory,dir2)
  print "\n%s[%s!%s] %sDownload selesai..."%(pu,me,pu,hi)
  print "%s[%s!%s] %sWaktu Terpakai: %s%s %sdetik"%(pu,me,pu,qu,ku,str(time_elapsed),qu)
 elif tyn == "Search by keyword":
   searchmode()
  #if (directory == "DF") or (directory == "df") or (directory == "Df") or (directory == "dF"): directory = "/sdcard/Download"


if __name__ == "__main__" :
  os.system("clear")
  print """%s
 __    __  ____    ____  __   _______   _______   ______   
|  |  |  | \   \  /   / |  | |       \ |   ____| /  __  \  
|  |  |  |  \   \/   /  |  | |  .--.  ||  |__   |  |  |  | %sAuthor by %sabilseno11%s
|  |  |  |   \      /   |  | |  |  |  ||   __|  |  |  |  | %sGithub %sgithub.com/AbilSeno%s
|  `--'  |    \    /    |  | |  '--'  ||  |____ |  `--'  | %sTools downloader uvideo.xyz%s
 \______/      \__/     |__| |_______/ |_______| \______/  
                                                           """%(hi,pu,ku,hi,pu,ku,hi,pu,hi)
  main()
