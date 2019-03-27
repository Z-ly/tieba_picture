import requests  
#import lxml.html
from bs4 import BeautifulSoup
import tkinter as tk
global url
window = tk.Tk()
window.title('my window')
window.geometry('400x200')

l = tk.Label(window, text = "输入百度贴吧网址", bg = 'white', font = ('Arial', 12),
             width = 15, heigh = 2)

l.pack()
e = tk.Entry(window)
e.pack()
var = tk.StringVar()

#print("输入百度贴吧网址")
#url = input('>')
#url = 'http://tieba.baidu.com/p/4952824669'
var = e.get()
t = tk.Text(window, height = 3)
t.pack()

def start_download():
    var = e.get()
    
    url = var
    #print(url)
    
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    pn = soup.select(".l_reply_num ")[0].select('.red')[1].text
    #t.insert('insert', 'downloading complete')

    #idx = 0
    for p in range(1,int(pn)+1):                                    #pagecount +1 总页数+1
    
        page = requests.get(url+'?pn='+str(p)).text  
        doc = BeautifulSoup(page,'html.parser')  
        for el in doc.select('img.BDE_Image'):  
            name = el['src'].split('/')[6]
            with open('img\%s' % name, 'wb') as f:  
                f.write(requests.get(el['src']).content)
                #idx += 1
    t.insert('insert', 'downloading complete')

    


b1 = tk.Button(window, text = 'start download', width = 15,
               height = 2,command = start_download)
b1.pack()





window.mainloop()
