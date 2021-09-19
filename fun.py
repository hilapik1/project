import select
import socket
import tkinter.scrolledtext as scroll
from tkinter import *
from datetime import datetime
from datetime import date


def add_image(client_socket, emoji_dic, pic_code, text_place):
    global user_nickname
    name_user = user_nickname
    time_cur = Calculate_Time()
    # path pic = r'emoji\emoji2.png'
    my_image = PhotoImage(file=emoji_dic[pic_code]).subsample(15, 15)
    text_place.images_list.append(my_image)
    # photoimage1 = my_image.subsample(11, 11)
    text_place.config(state='normal')
    text_place.insert('end', time_cur + " " + name_user + ": " + '\n')
    text_place.image_create('end', image=my_image)
    text_place.insert('end', '\n')
    text_place.config(state='disabled')  # you cant edit the screen after you wrote something
    # Application(Window.Frame)
    send_the_emoji_code(client_socket, pic_code)


def send_the_emoji_code(client_socket,emoji_code):
    for_message = ("image$").encode()
    length_of_message = len(for_message)
    client_socket.send(str(length_of_message).zfill(4).encode())
    client_socket.send(for_message)
    length_of_code=len(emoji_code.encode())
    client_socket.send(str(length_of_code).zfill(4).encode())
    client_socket.send(emoji_code.encode())


def init_dict(emoji_dic):
    dic = {'emoji1': r'emoji\imagemario.png'}
    emoji_dic.update(dic)
    dic = {'emoji2': r'emoji\emoji2.png'}
    emoji_dic.update(dic)
    dic = {'emoji3': r'emoji\emoji3.png'}
    emoji_dic.update(dic)
    dic = {'emoji4': r'emoji\emoji4.png'}
    emoji_dic.update(dic)
    dic = {'emoji5': r'emoji\emoji6.png'}
    emoji_dic.update(dic)
    dic = {'emoji6': r'emoji\emoji7.png'}
    emoji_dic.update(dic)
    dic = {'emoji7': r'emoji\emoji8.png'}
    emoji_dic.update(dic)
    dic = {'emoji8': r'emoji\emoji9.png'}
    emoji_dic.update(dic)
    dic = {'emoji9': r'emoji\emoji10.png'}
    emoji_dic.update(dic)

def Calculate_Date():
    today = date.today()
    # Textual month, day and year
    d2 = today.strftime("%B %d, %Y")
    #print("d2 =", d2)
    return d2;

def Calculate_Time():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    #print("Current Time =", current_time)
    time = current_time.split(':')
    time_update=time[0]+':'+time[1]
    return time_update
    #print(time_update)

def Show_The_Msg_On_Screen(client_socket, text_place, textbox):
    global user_nickname
    time_cur = Calculate_Time()

    userMsg = textbox.get('1.0',END)
    textbox.delete("1.0","end")#clear the text box after send the message
    print(userMsg)
    if userMsg != "\n":
        text_place.config(state='normal')#if you want to write something on the screen
        text_place.insert('end',time_cur+ " " +user_nickname+": "+userMsg)
        print(f"time_cur={time_cur}, name_user = {user_nickname}, userMsg = {userMsg}")

        text_place.config(state='disabled')#you cant edit the screen after you wrote something
        for_message = ("message$" + userMsg).encode()
        length_of_message = len(for_message)
        client_socket.send(str(length_of_message).zfill(4).encode())
        client_socket.send(for_message)
    elif userMsg=="\n":
        print("empty message")
        pass

def NameOfUser(client_socket, Window, input_box, text_place):
    global user_nickname

    first_time = True
    ok = True

    cur_date=Calculate_Date()
    user_nickname = input_box.get()
    print("D"+user_nickname+"g")
    if user_nickname=="":
        print("serddggf")
    while ok:
        if user_nickname =="":
            input_box.delete("1.0","end")
            input_box.config(state="normal")
            user_nickname = input_box.get()
        else:
            input_box.config(state="disabled")  # you cant change the name after you wrote it- frizing box
            ok = False
    Window.title(user_nickname+' Come chat with us! by: Hila Pickholz')
    if first_time:
         text_place.config(state="normal")
         print("entering")
         first_time=False
         text_place.insert('end',cur_date+ '\n')
         text_place.config(state="disabled")
    for_name = "name$" + user_nickname
    length_of_nickname = len(for_name)
    client_socket.send(str(length_of_nickname).zfill(4).encode())
    client_socket.send(for_name.encode())


def init_gui_emoji_window(client_socket, Window, emoji_dic, text_place):
    outer_frame=Frame(Window, width=100, height=300)
    outer_frame.pack(side=RIGHT)
    emoji_chart_place = Canvas(outer_frame, bg='#FFFFFF', width=102, height=300, scrollregion=(0, 0, 120, 950))
    iner_frame = Frame(emoji_chart_place, width=100, height=950)
    iner_frame.pack(expand=True, fill=BOTH)  # .grid(row=0,column=0)
    vbar = Scrollbar(outer_frame, orient=VERTICAL)
    vbar.config(command=emoji_chart_place.yview)
    vbar.pack(side=RIGHT, fill=Y)

    emoji_chart_place.config(yscrollcommand=vbar)

    # Creating a photoimage object to use image
    photo1 = PhotoImage(file=r'emoji\imagemario.png')
    # Resizing image to fit on button
    photoimage1 = photo1.subsample(4, 4)
    photo2 = PhotoImage(file=r'emoji\emoji2.png')
    photoimage2 = photo2.subsample(4, 4)
    photo3 = PhotoImage(file=r'emoji\emoji3.png')
    photoimage3 = photo3.subsample(4, 4)
    photo4 = PhotoImage(file=r'emoji\emoji4.png')
    photoimage4 = photo4.subsample(4, 4)
    photo5 = PhotoImage(file=r'emoji\emoji6.png')
    photoimage5 = photo5.subsample(4, 4)
    photo6 = PhotoImage(file=r'emoji\emoji7.png')
    photoimage6 = photo6.subsample(4, 4)
    photo7 = PhotoImage(file=r'emoji\emoji8.png')
    photoimage7 = photo7.subsample(4, 4)
    photo8 = PhotoImage(file=r'emoji\emoji9.png')
    photoimage8 = photo8.subsample(4, 4)
    photo9= PhotoImage(file=r'emoji\emoji10.png')
    photoimage9 = photo9.subsample(4, 4)
    Window.images = []
    Window.images.append(photoimage1)
    Window.images.append(photoimage2)
    Window.images.append(photoimage3)
    Window.images.append(photoimage4)
    Window.images.append(photoimage5)
    Window.images.append(photoimage6)
    Window.images.append(photoimage7)
    Window.images.append(photoimage8)
    Window.images.append(photoimage9)

    Button(iner_frame, text='', image=photoimage1, command=lambda: add_image(client_socket, emoji_dic, 'emoji1', text_place)).pack(side=TOP)
    Button(iner_frame, text='', image=photoimage2, command=lambda: add_image(client_socket, emoji_dic, 'emoji2', text_place)).pack(side=TOP)
    Button(iner_frame, text='', image=photoimage3, command=lambda: add_image(client_socket, emoji_dic, 'emoji3', text_place)).pack(side=TOP)
    # ---------------------------------------------------------------------------------
    Button(iner_frame, text='', image=photoimage4, command=lambda: add_image(client_socket, emoji_dic, 'emoji4', text_place)).pack(side=TOP)
    Button(iner_frame, text='', image=photoimage5, command=lambda: add_image(client_socket, emoji_dic, 'emoji5', text_place)).pack(side=TOP)
    Button(iner_frame, text='', image=photoimage6, command=lambda: add_image(client_socket, emoji_dic, 'emoji6', text_place)).pack(side=TOP)
    Button(iner_frame, text='', image=photoimage7, command=lambda: add_image(client_socket, emoji_dic, 'emoji7', text_place)).pack(side=TOP)
    Button(iner_frame, text='', image=photoimage8, command=lambda: add_image(client_socket, emoji_dic, 'emoji8', text_place)).pack(side=TOP)
    Button(iner_frame, text='', image=photoimage9, command=lambda: add_image(client_socket, emoji_dic, 'emoji9', text_place)).pack(side=TOP)
    # emoji_chart_place.image_create('end', image=my_image)
    # emoji_chart_place.insert('end', '\n')
    # emoji_chart_place.configure(scrollregion=emoji_chart_place.bbox("all"))
    emoji_chart_place.create_window(0, 0, anchor='nw', window=iner_frame)
    # make sure everything is displayed before configuring the scrollregion
    emoji_chart_place.update_idletasks()
    emoji_chart_place.pack(side=RIGHT)

def quit_the_window(client_socket,Window):
    for_message = ("quit$").encode()
    length_of_message = len(for_message)
    client_socket.send(str(length_of_message).zfill(4).encode())
    client_socket.send(for_message)
    print("exit")
    Window.destroy()#get out of the screen

def init_gui_main_window(client_socket):
    Window = Tk()
    Window.configure(bg="lavender")  # lightcyan  azure lavender blush
    # Window.geometry("700x500")
    Window.geometry("755x500")
    Window.resizable(False, False)  # self.win.resizab'le()

    input_box = Entry(Window, width=50, borderwidth=4)
    input_box.place(x=205, y=40)
    # input_box.insert(0, "Enter Your Name: ")
    input_box.insert('end', "")

    text_place = scroll.ScrolledText(Window, width=50, height=15)
    text_place.config(state="disabled")
    text_place.place(x=140, y=110)

    text_place.images_list = []

    # button=Butt on(Window,text="Enter Your Name ",command=myClick,fg="black",bg="turquoise")# if want in the second way(not pixels)-> .grid(row=25,column=124)
    button = Button(Window, text="Enter Your Name ", command=lambda: NameOfUser(client_socket, Window, input_box, text_place), fg="black", bg="turquoise")
    button.pack()  # the button is on the window
    button.place(x=295, y=70)  # pixels

    myLable = Label(Window, text="Welcome to my chat :) ", fg="black", bg="turquoise", padx=50)  # turquoise
    myLable.place(x=250, y=10)

    button_quit = Button(Window, text="Exit Program", command=lambda: quit_the_window(client_socket,Window))
    button_quit.place(x=75, y=15)

    text_box = Text(Window, width=50, height=3)
    text_box.pack()
    text_box.place(x=140, y=385)

    button_text = Button(Window, text="Tap Here To Send ", command=lambda:Show_The_Msg_On_Screen(client_socket, text_place, text_box), bg="turquoise", padx=100)
    button_text.place(x=190, y=450)
    # ---------------------------------------------------------------------------
    labelPryProt = Label(Window, text="CHAT TIME", bg='white')
    labelPryProt.pack(side=LEFT, fill=BOTH, expand=False)
    labelPryProt = Label(Window, text='CHAT TIME', font='Helvetica 18 bold')

    return Window, text_place

def init_network():
    client_socket = socket.socket()
    client_socket.connect(("127.0.0.1", 5555))
    return client_socket

def MySelect(client_socket, emoji_dic, Window, text_place):
    # network - input from network
    rlist, wlist, xlist = select.select([client_socket], [], [], 0.01)
    for sock in rlist:
        rmsg = sock.recv(1024).decode()
        print("ddd")
        print(rmsg)
        if (rmsg != ""):
            type_mes=rmsg.split('$')
            if  "message" in rmsg:
                print('h')
                rmsg=type_mes[1]
                #rmsg = sock.recv(1024).decode()
                print(rmsg)
                text_place.config(state='normal')  # if you want to write something on the screen
                print(rmsg)
                text_place.insert('end',rmsg)
                #text_place.yview('end')
                text_place.config(state='disabled')  # you cant edit the screen after you wrote something
            elif "image" in rmsg:
                code_emoji=type_mes[1]
                name_of_user=type_mes[2]
                print("hhhh")
                print(emoji_dic.get(code_emoji))
                print("jjjj")
                my_image = PhotoImage(file=emoji_dic.get(code_emoji)).subsample(15, 15)
                #my_image = PhotoImage(file=emoji_dic[code_emoji]).subsample(15, 15)
                text_place.images_list.append(my_image)
                text_place.config(state='normal')
                #name_user = NameOfUser()
                print(name_of_user+ "kkkkk")
                time_cur = Calculate_Time()
                text_place.insert('end', time_cur + " " + name_of_user + ": "+'\n')
                text_place.image_create('end', image=my_image)
                text_place.insert('end', '\n')
                text_place.config(state='disabled')  # you cant edit the screen after you wrote something
        else:
            print("eror")
    Window.after(1000, lambda: MySelect(client_socket, emoji_dic, Window, text_place))


global user_nickname
user_nickname=""

def main():
    client_socket = init_network()

    emoji_dic = {}
    init_dict(emoji_dic)

    Window, text_place = init_gui_main_window(client_socket)

    init_gui_emoji_window(client_socket, Window, emoji_dic, text_place)

    Window.after(1000, lambda: MySelect(client_socket, emoji_dic, Window, text_place))

    Window.mainloop()

if __name__ == "__main__":
    main()