import select
import socket
import tkinter.scrolledtext as scroll
from tkinter import *
from datetime import datetime
from datetime import date

class user:
    def __init__(self,socket):
        self.user_nickname = ""
        self.client_socket=socket
        self.emoji_dic = {}
        self.Window = Tk()
        self.text_place = scroll.ScrolledText(self.Window, width=50, height=15)

    def add_image(self, pic_code):
        name_user = self.user_nickname
        time_cur = self.Calculate_Time()
        # path pic = r'emoji\emoji2.png'
        my_image = PhotoImage(file=self.emoji_dic[pic_code]).subsample(15, 15)
        self.text_place.images_list.append(my_image)
        # photoimage1 = my_image.subsample(11, 11)
        self.text_place.config(state='normal')
        self.text_place.insert('end', time_cur + " " + name_user + ": " + '\n')
        self.text_place.image_create('end', image=my_image)
        self.text_place.insert('end', '\n')
        self.text_place.config(state='disabled')  # you cant edit the screen after you wrote something
        # Application(Window.Frame)
        self.send_the_emoji_code(pic_code)


    def send_the_emoji_code(self,emoji_code):
        for_message = ("image$").encode()
        length_of_message = len(for_message)
        self.client_socket.send(str(length_of_message).zfill(4).encode())
        self.client_socket.send(for_message)
        length_of_code=len(emoji_code.encode())
        self.client_socket.send(str(length_of_code).zfill(4).encode())
        self.client_socket.send(emoji_code.encode())


    def init_dict(self):
        dic = {'emoji1': r'C:\hifolder\cyber\chat_project\emoji\imagemario.png'}
        self.emoji_dic.update(dic)
        dic = {'emoji2': r'C:\hifolder\cyber\chat_project\emoji\emoji2.png'}
        self.emoji_dic.update(dic)
        dic = {'emoji3': r'C:\hifolder\cyber\chat_project\emoji\emoji3.png'}
        self.emoji_dic.update(dic)
        dic = {'emoji4': r'C:\hifolder\cyber\chat_project\emoji\emoji4.png'}
        self.emoji_dic.update(dic)
        dic = {'emoji5': r'C:\hifolder\cyber\chat_project\emoji\emoji6.png'}
        self.emoji_dic.update(dic)
        dic = {'emoji6': r'C:\hifolder\cyber\chat_project\emoji\emoji7.png'}
        self.emoji_dic.update(dic)
        dic = {'emoji7': r'C:\hifolder\cyber\chat_project\emoji\emoji8.png'}
        self.emoji_dic.update(dic)
        dic = {'emoji8': r'C:\hifolder\cyber\chat_project\emoji\emoji9.png'}
        self.emoji_dic.update(dic)
        dic = {'emoji9': r'C:\hifolder\cyber\chat_project\emoji\emoji10.png'}
        self.emoji_dic.update(dic)

    def Calculate_Date(self):
        today = date.today()
        # Textual month, day and year
        d2 = today.strftime("%B %d, %Y")
        #print("d2 =", d2)
        return d2;

    def Calculate_Time(self):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        #print("Current Time =", current_time)
        time = current_time.split(':')
        time_update=time[0]+':'+time[1]
        return time_update
        #print(time_update)

    def Show_The_Msg_On_Screen(self, textbox):
        time_cur = self.Calculate_Time()
        userMsg = textbox.get('1.0',END)
        textbox.delete("1.0","end")#clear the text box after send the message
        print(userMsg)
        if userMsg != "\n":
            self.text_place.config(state='normal')#if you want to write something on the screen
            self.text_place.insert('end',time_cur+ " " +self.user_nickname+": "+userMsg)
            print(f"time_cur={time_cur}, name_user = {self.user_nickname}, userMsg = {userMsg}")

            self.text_place.config(state='disabled')#you cant edit the screen after you wrote something
            for_message = ("message$" + userMsg).encode()
            length_of_message = len(for_message)
            self.client_socket.send(str(length_of_message).zfill(4).encode())
            self.client_socket.send(for_message)
        elif userMsg=="\n":
            print("empty message")
            pass

    def NameOfUser(self, input_box):
        first_time = True
        ok = True
        cur_date=self.Calculate_Date()
        self.user_nickname = input_box.get()
        print("D"+self.user_nickname+"g")
        if self.user_nickname=="":
            print("serddggf")
        while ok:
            if self.user_nickname =="":
                input_box.delete("1.0","end")
                input_box.config(state="normal")
                self.user_nickname = input_box.get()
            else:
                input_box.config(state="disabled")  # you cant change the name after you wrote it- frizing box
                ok = False
        self.Window.title(self.user_nickname+' Come chat with us! by: Hila Pickholz')
        if first_time:
             self.text_place.config(state="normal")
             print("entering")
             first_time=False
             self.text_place.insert('end',cur_date+ '\n')
             self.text_place.config(state="disabled")
        for_name = "name$" + self.user_nickname
        length_of_nickname = len(for_name)
        self.client_socket.send(str(length_of_nickname).zfill(4).encode())
        self.client_socket.send(for_name.encode())


    def init_gui_emoji_window(self):
        outer_frame=Frame(self.Window, width=100, height=300)
        outer_frame.pack(side=RIGHT)
        emoji_chart_place = Canvas(outer_frame, bg='#FFFFFF', width=102, height=300, scrollregion=(0, 0, 120, 950))
        iner_frame = Frame(emoji_chart_place, width=100, height=950)
        iner_frame.pack(expand=True, fill=BOTH)  # .grid(row=0,column=0)
        vbar = Scrollbar(outer_frame, orient=VERTICAL)
        vbar.config(command=emoji_chart_place.yview)
        vbar.pack(side=RIGHT, fill=Y)

        emoji_chart_place.config(yscrollcommand=vbar)

        # Creating a photoimage object to use image
        photo1 = PhotoImage(file=r'C:\hifolder\cyber\chat_project\emoji\imagemario.png')
        # Resizing image to fit on button
        photoimage1 = photo1.subsample(4, 4)
        photo2 = PhotoImage(file=r'C:\hifolder\cyber\chat_project\emoji\emoji2.png')
        photoimage2 = photo2.subsample(4, 4)
        photo3 = PhotoImage(file=r'C:\hifolder\cyber\chat_project\emoji\emoji3.png')
        photoimage3 = photo3.subsample(4, 4)
        photo4 = PhotoImage(file=r'C:\hifolder\cyber\chat_project\emoji\emoji4.png')
        photoimage4 = photo4.subsample(4, 4)
        photo5 = PhotoImage(file=r'C:\hifolder\cyber\chat_project\emoji\emoji6.png')
        photoimage5 = photo5.subsample(4, 4)
        photo6 = PhotoImage(file=r'C:\hifolder\cyber\chat_project\emoji\emoji7.png')
        photoimage6 = photo6.subsample(4, 4)
        photo7 = PhotoImage(file=r'C:\hifolder\cyber\chat_project\emoji\emoji8.png')
        photoimage7 = photo7.subsample(4, 4)
        photo8 = PhotoImage(file=r'C:\hifolder\cyber\chat_project\emoji\emoji9.png')
        photoimage8 = photo8.subsample(4, 4)
        photo9= PhotoImage(file=r'C:\hifolder\cyber\chat_project\emoji\emoji10.png')
        photoimage9 = photo9.subsample(4, 4)
        self.Window.images = []
        self.Window.images.append(photoimage1)
        self.Window.images.append(photoimage2)
        self.Window.images.append(photoimage3)
        self.Window.images.append(photoimage4)
        self.Window.images.append(photoimage5)
        self.Window.images.append(photoimage6)
        self.Window.images.append(photoimage7)
        self.Window.images.append(photoimage8)
        self.Window.images.append(photoimage9)

        Button(iner_frame, text='', image=photoimage1, command=lambda: self.add_image('emoji1')).pack(side=TOP)
        Button(iner_frame, text='', image=photoimage2, command=lambda: self.add_image('emoji2')).pack(side=TOP)
        Button(iner_frame, text='', image=photoimage3, command=lambda: self.add_image('emoji3')).pack(side=TOP)
        # ---------------------------------------------------------------------------------
        Button(iner_frame, text='', image=photoimage4, command=lambda: self.add_image('emoji4')).pack(side=TOP)
        Button(iner_frame, text='', image=photoimage5, command=lambda: self.add_image('emoji5')).pack(side=TOP)
        Button(iner_frame, text='', image=photoimage6, command=lambda: self.add_image('emoji6')).pack(side=TOP)
        Button(iner_frame, text='', image=photoimage7, command=lambda: self.add_image('emoji7')).pack(side=TOP)
        Button(iner_frame, text='', image=photoimage8, command=lambda: self.add_image('emoji8')).pack(side=TOP)
        Button(iner_frame, text='', image=photoimage9, command=lambda: self.add_image('emoji9')).pack(side=TOP)
        # emoji_chart_place.image_create('end', image=my_image)
        # emoji_chart_place.insert('end', '\n')
        # emoji_chart_place.configure(scrollregion=emoji_chart_place.bbox("all"))
        emoji_chart_place.create_window(0, 0, anchor='nw', window=iner_frame)
        # make sure everything is displayed before configuring the scrollregion
        emoji_chart_place.update_idletasks()
        emoji_chart_place.pack(side=RIGHT)

    def quit_the_window(self):
        for_message = ("quit$").encode()
        length_of_message = len(for_message)
        self.client_socket.send(str(length_of_message).zfill(4).encode())
        self.client_socket.send(for_message)
        print("exit")
        self.Window.destroy()#get out of the screen

    def init_gui_main_window(self):
        #Window = Tk()
        self.Window.configure(bg="lavender")  # lightcyan  azure lavender blush
        # Window.geometry("700x500")
        self.Window.geometry("755x500")
        self.Window.resizable(False, False)  # self.win.resizab'le()

        input_box = Entry(self.Window, width=50, borderwidth=4)
        input_box.place(x=205, y=40)
        # input_box.insert(0, "Enter Your Name: ")
        input_box.insert('end', "")

        # text_place = scroll.ScrolledText(self.Window, width=50, height=15)
        self.text_place.config(state="disabled")
        self.text_place.place(x=140, y=110)

        self.text_place.images_list = []

        # button=Butt on(Window,text="Enter Your Name ",command=myClick,fg="black",bg="turquoise")# if want in the second way(not pixels)-> .grid(row=25,column=124)
        button = Button(self.Window, text="Enter Your Name ", command=lambda: self.NameOfUser(input_box), fg="black", bg="turquoise")
        button.pack()  # the button is on the window
        button.place(x=295, y=70)  # pixels

        myLable = Label(self.Window, text="Welcome to my chat :) ", fg="black", bg="turquoise", padx=50)  # turquoise
        myLable.place(x=250, y=10)

        button_quit = Button(self.Window, text="Exit Program", command=lambda: self.quit_the_window())
        button_quit.place(x=75, y=15)

        text_box = Text(self.Window, width=50, height=3)
        text_box.pack()
        text_box.place(x=140, y=385)

        button_text = Button(self.Window, text="Tap Here To Send ", command=lambda:self.Show_The_Msg_On_Screen(text_box), bg="turquoise", padx=100)
        button_text.place(x=190, y=450)
        # ---------------------------------------------------------------------------
        labelPryProt = Label(self.Window, text="CHAT TIME", bg='white')
        labelPryProt.pack(side=LEFT, fill=BOTH, expand=False)
        labelPryProt = Label(self.Window, text='CHAT TIME', font='Helvetica 18 bold')

        return self.Window, self.text_place



    def MySelect(self):
        # network - input from network
        rlist, wlist, xlist = select.select([self.client_socket], [], [], 0.01)
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
                    self.text_place.config(state='normal')  # if you want to write something on the screen
                    print(rmsg)
                    self.text_place.insert('end',rmsg)
                    #text_place.yview('end')
                    self.text_place.config(state='disabled')  # you cant edit the screen after you wrote something
                elif "image" in rmsg:
                    code_emoji=type_mes[1]
                    name_of_user=type_mes[2]
                    print("hhhh")
                    print(self.emoji_dic.get(code_emoji))
                    print("jjjj")
                    my_image = PhotoImage(file=self.emoji_dic.get(code_emoji)).subsample(15, 15)
                    #my_image = PhotoImage(file=emoji_dic[code_emoji]).subsample(15, 15)
                    self.text_place.images_list.append(my_image)
                    self.text_place.config(state='normal')
                    #name_user = NameOfUser()
                    print(name_of_user+ "kkkkk")
                    time_cur = self.Calculate_Time()
                    self.text_place.insert('end', time_cur + " " + name_of_user + ": "+'\n')
                    self.text_place.image_create('end', image=my_image)
                    self.text_place.insert('end', '\n')
                    self.text_place.config(state='disabled')  # you cant edit the screen after you wrote something
            else:
                print("eror")
        self.Window.after(1000, lambda: self.MySelect())

    def get_Window(self):
        return self.Window

def init_network():
    client_socket = socket.socket()
    client_socket.connect(("127.0.0.1", 5555))
    return client_socket

def main():
    client_socket = init_network()
    user1 = user(client_socket)
    user1.init_dict()
    Window, text_place = user1.init_gui_main_window()

    user1.init_gui_emoji_window()

    Window.after(1000, lambda: user1.MySelect())

    Window.mainloop()

if __name__ == "__main__":
    main()