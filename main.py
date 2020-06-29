from bin.rufengso import rufen
from bin.pansou import pansou
from bin.pantx import pantx
from bin.pan51 import pan51
from bin.fastsoso import fastsoso
from bin.yunpz import yunpz
from bin.qzhou import qzhou
from bin.verypan import verypan
from static import All_ret
from tkinter import *
from copy import copy
from static.pro import copy_type

n_s_dic = {
    '51网盘':pan51,
}

s_dic = {
    # 'yunpz(不占后台)': yunpz,
    'rufen(不占后台)': rufen,
    'pantx(不占后台)': pantx,
    'qzhou(不占后台)': qzhou,
    'pansou(不占后天)':pansou,
    'verypan(不占后台)': verypan,
    'fastsoso(不占后台)': fastsoso,
}

dic = {}

# for key in n_s_dic:
#     dic[key] = n_s_dic[key]
# for key in s_dic:
#     dic[key] = s_dic[key]


# th_dic = {} if copy_type == 1 else copy(s_dic)

def tk_run(title,num=None):
    for pro in th_dic:
        All_ret.run(th_dic[pro],title,num=num)

def tk_main():
    def global_dic():
        global th_dic
        th_dic = _dic
        root.destroy()
    def add_Checkbutton():
        def insert(title):
            if 'del' in title:
                if _dic.get(title[3:]):
                    del _dic[title[3:]]
            elif title.strip():
                if not _dic.get(title):
                    _dic[title] = dic[title]
        def inner(t):
            var = StringVar(root)
            r = Checkbutton(root, text=t, variable=var, onvalue=t, offvalue='del' + t,command=lambda: insert(var.get()))
            r.pack()
        for text in dic.keys():
            inner(text)
    _dic = copy(th_dic)
    root = Tk()
    root.minsize(500,300)
    root.title('选择添加搜索引擎')
    Label(root,text='请选择').pack()
    add_Checkbutton()
    Button(root,text='保存',command=global_dic).pack()
    root.mainloop()
