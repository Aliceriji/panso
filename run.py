import sys,os
sys.path.append(os.getcwd())
from main import tk_main,tk_run
from static.All_ret import *
from tkinter import *
from threading import Thread
import keyboard
import time
from static.pro import *
import webbrowser

run_time = True
thread_time = True

now_num = 1
All_lis = []

def key(bro,key):
    def inner():
        while 1:
            if keyboard.wait(key) == None:
                bro()
            time.sleep(2)
    t = Thread(target=inner)
    t.setDaemon(True)
    t.start()

def main():
    def get_lis():
        def inner():
            global thread_time,now_num
            T1.delete('0.0', END)
            lis = ret_lis()
            for _lis in lis:
                for li in _lis:
                    if li[-1] not in All_lis:
                        All_lis.append(li[-1])
                        insert_one(li,T1)
            var.set('当前状态:当前第%s页获取完毕'%now_num)
            now_num += 1
            thread_time = True
        global thread_time
        if thread_time:
            var.set('当前状态:正在搜索,请稍后')
            thread_time = False
            if run_time == True:return None
            T = Thread(target=inner)
            T.setDaemon(True)
            T.start()
        else:
            var.set('当前状态:正在搜索,请稍后')
    def insert_one(tup,text):
        def show(url):
            webbrowser.open(url)
        b1 = Button(text, text=tup[0].strip(), fg="blue", bg="white", bd=0, command=lambda: show(tup[-1]))
        text.window_create(INSERT, window=b1)
        text.insert('end', '\n')
    def del_All():
        global run_time
        if run_time == True: return None
        del_driver()
        E1.delete(0,END)
        run_time = True
        var.set('当前状态:已清除')
        global All_lis
        All_lis.clear()
    def find():
        global run_time,now_num
        p = E1.get().strip()
        if p and run_time:
            var.set('当前状态:正在搜索,请稍后')
            run_time = False
            if '|' in p:
                p,n = p.split('|')
                now_num = int(n)
                tk_run(p,now_num)
            else:
                tk_run(p)
            get_lis()
        elif not p:
            var.set('当前状态:请输入内容进行搜索')
        else:
            var.set('当前状态:已存在搜索后台')
    def count_pro():
        tk_main()
    Root = Tk()
    Root.minsize(600,400)
    Root.title('网盘搜索')
    menu = Menu(Root)
    menu.add_command(label='选择引擎',command=count_pro)
    menu.add_command(label='点击清除', command=lambda :T1.delete('0.0',END))
    var = StringVar(Root)
    Label(Root,textvariable=var).pack()
    var.set('当前状态:无')
    T1 = Text(Root,width='60',height='15')
    T1.pack()
    scroll = Scrollbar(Root)
    scroll.place(x=530,y=50)
    scroll.config(command=T1.yview)
    T1.config(yscrollcommand=scroll.set)
    Label(Root,text='请输入搜索内容').pack()
    E1 = Entry(Root)
    E1.pack()
    Button(Root,text='点击搜索',command=find).pack()
    Button(Root,text='点击下一页',command=get_lis).pack()
    Button(Root,text='关闭后台进程',command=del_All).pack()
    key(find,key_find)
    key(get_lis,key_lis)
    key(del_All,key_del)
    Root.config(menu=menu)
    Root.mainloop()

if __name__ == '__main__':
    main()
    # if input('是否完全退出浏览器后台(y/n):') == 'y':
    #     import os
    #     os.system('taskkill -im chromedriver.exe -F')
    #     os.system('taskkill -im chrome.exe -F')