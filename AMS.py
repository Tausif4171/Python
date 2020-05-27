from tkinter import *
import tkinter.messagebox
import time


get=None
def record(event):
    global get
    a=student_username_entry.get()+'.txt'
    fw=open(a,'a+')
    fwt=open("admin.txt",'a+')
    fw.write("                  ")
    fwt.write("                 ")
    fw.write(student_username_entry.get())
    fwt.write(student_username_entry.get())
    fw.write("                  ")
    fwt.write("                 ")
    fw.write('Present')
    fwt.write('Present')
    fw.write("                  ")
    fwt.write("                 ")
    fw.write(var2.get())
    fwt.write(var2.get())
    fw.write("                  ")
    fwt.write("                 ")
    fw.write(time.strftime("%H:%M:%S"))
    fwt.write(time.strftime("%H:%M:%S"))
    fw.write("              ")
    fwt.write("             ")
    fw.write(time.strftime("%Y-%m-%d"))
    fwt.write(time.strftime("%Y-%m-%d"))
    fw.write('\n')
    fwt.write('\n')
    get.destroy()
    dashboard_button_1.destroy()
    fw.close()


student_login_frame=None
student_password_entry=None
student_username_entry=None

def student_login():
    global student_login_frame
    student_login_frame = Frame(student_admin_frame, width=900, height=500, bg='black')
    student_login_frame.place(x=0, y=0)
    student_login_frame.tkraise()
    student_icon = Label(student_login_frame, image=img15, bd=0, bg='#EBF2F8')
    student_icon.place(x=370, y=10)
    username_label = Label(student_login_frame, text='Username', font=('Berlin Sans FB', 16), bg='#EBF2F8')
    username_label.place(x=405, y=200)
    global student_username_entry
    student_username_entry = Entry(student_login_frame, bg='white', relief='sunken', highlightcolor='#D2E0F1',highlightthickness=1, highlightbackground='#D8D6D7', font=('Tw Cen MT', 14))
    student_username_entry.place(x=350, y=240)
    password_label = Label(student_login_frame, text='Password', font=('Berlin Sans FB', 16), bg='#EBF2F8')
    password_label.place(x=405, y=280)
    global student_password_entry
    student_password_entry = Entry(student_login_frame, bg='white', show='*', relief='sunken', highlightcolor='#D2E0F1',highlightthickness=1, highlightbackground='#D8D6D7', font=('Tw Cen MT', 14))
    student_password_entry.place(x=350, y=320)
    student_password_entry.bind('<Return>', authorize)
    login_button = Button(student_login_frame, image=img24, bd=0, bg='#EBF2F8')
    login_button.bind('<Button-1>',authorize)
    login_button.place(x=357, y=380)
    cancel_button = Button(student_login_frame, image=img14, bd=0, bg='#EBF2F8', command=student_exit)
    cancel_button.place(x=357, y=430)


def authorize(event):
    fr = open('database.txt', 'r')
    flag = 0
    for line in fr:
        if student_username_entry.get() in line and student_password_entry.get()=='12345':
            flag = 1
            break
    if flag == 1 and len(student_username_entry.get())==5:
        student_portal()
    fr.close()




def show_admin_record():
    show_admin_record_frame = Frame(admin_display_frame, width=650, height=500, bd=0, bg='white')
    show_admin_record_frame.place(x=0, y=0)
    show_admin_record_frame.tkraise()
    headings = Label(show_admin_record_frame, bg='white',text="ROLL NO                  STATUS                   SUBJECT                     TIME                    DATE")
    headings.place(x=50, y=0)
    heading_seperator = Label(show_admin_record_frame, image=img10, bg='white')
    heading_seperator.place(x=-50, y=20)
    p = Listbox(show_admin_record_frame, width=100, height=327, bd=0, bg='black', fg='white',font="Candara 12 bold")
    p.place(x=0, y=50)
    global L
    for x in range(len(L)):
        p.insert(END, L[x])
    L=[]
    back = Button(show_admin_record_frame, image=img20, command=admin_portal, highlightthickness=0)
    back.place(x=560, y=-10)

L=[]
def authorize_admin_record():
    global var3
    global L
    if enter_date_entry.get() != '':
        fr=open("admin.txt",'r')
        for line in fr:
            flag=0
            if enter_date_entry.get() in line and var3.get() in line:
                flag=1
                if flag==1:
                    L.append(line)

        fr.close()
    show_admin_record()


var3=None
enter_data_entry=None

def admin_record():
    admin_record_frame=Frame(admin_display_frame, width=650, height=500,bg='#EBF2F8')
    admin_record_frame.place(x=0,y=0)
    enter_date_label=Label(admin_record_frame,text="Enter Today's date in yyyy-mm-dd ",font=('Berlin Sans FB',16),bg='#EBF2F8')
    enter_date_label.place(x=150,y=50)
    global var3
    global enter_date_entry
    var3 = StringVar()
    enter_date_entry=Entry(admin_record_frame,bg='#EBF2F8',relief='flat',highlightcolor='#D2E0F1',highlightthickness=1,highlightbackground='#D8D6D7',font=('Tw Cen MT',14))
    enter_date_entry.place(x=210,y=110)
    optionList = ('Python', 'AOA', 'OS','CG','M4','COA')
    var3.set(optionList[0])
    d_menu = OptionMenu(admin_record_frame, var3, *optionList)
    d_menu.config(font=('calibri', (20)), width=320, fg='blue', image=img16, indicatoron=0, bd=0,bg='#EBF2F8')
    d_menu.place(x=150, y=200)
    get_admin_record=Button(admin_record_frame,image=img21,command=authorize_admin_record,bd=0,bg='#EBF2F8')
    get_admin_record.place(x=240,y=340)

def home():
    global display_frame
    display_frame = Frame(student_login_frame, width=650, height=500, bg='#EBF2F8')
    display_frame.place(x=250, y=0)
    display_frame.tkraise()
    ned_logo = Label(display_frame, image=img3, bg='#EBF2F8')
    ned_logo.place(x=-180, y=-200)
    sp_logo = Label(display_frame, image=img4, bg='#EBF2F8')
    sp_logo.place(x=150, y=175)


var2=None
attendance_frame=None
def takeattendance():
    global attendance_frame
    attendance_frame = Frame(display_frame, width=650, height=500, bg='#EBF2F8')
    attendance_frame.tkraise()
    attendance_frame.pack()
    instruction_label=Label(attendance_frame,text="SELECT THE SUBJECT AND PRESS THE 'ATTENDANCE' LOGO",font=('Felix Titling',14,'bold'),bg='#EBF2F8')
    instruction_label.place(x=20,y=100)
    global var2
    var2 = StringVar()
    optionList = ('Python', 'AOA', 'OS','CG','M4','COA')
    var2.set(optionList[0])
    d_menu = OptionMenu(attendance_frame, var2, *optionList)
    d_menu.config(font=('calibri', (20)), fg='blue', image=img16, indicatoron=0,bd=0)
    d_menu.place(x=150,y=200)
    global get
    get=Button(attendance_frame,image=img17,bd=0,bg='#EBF2F8')
    get.place(x=200,y=310)
    get.bind("<Button-1>",record)
    back = Button(attendance_frame, image=img18,command=home,bd=0,bg='#EBF2F8')
    back.place(x=360, y=300)

display_frame=None
dashboard_button_1=None
def student_portal():
    dashboard_frame=Frame(student_login_frame,width=250,height=500,bg='#1C2739')
    dashboard_frame.place(x=0,y=0)
    dashboard_frame.tkraise()
    dashboard_label=Label(dashboard_frame,image=img5,bg='#1C2739')
    dashboard_label.place(x=5,y=5)
    divider_logo=Label(dashboard_frame,image=img9,bg='#1C2739')
    divider_logo.place(x=0,y=60)
    global dashboard_button_1
    dashboard_button_1 = Button(dashboard_frame,image=img6,command=takeattendance,bg='#1C2739',bd=0)
    dashboard_button_1.place(x=5, y=120)
    dashboard_button_2 = Button(dashboard_frame, image=img7,bd=0,bg='#1C2739', command=show_student_record)
    dashboard_button_2.place(x=-30, y=200)
    dashboard_button_3 = Button(dashboard_frame, image=img8,bd=0,bg='#1C2739', command=student_login)
    dashboard_button_3.place(x=10, y=270)
    global display_frame
    display_frame=Frame(student_login_frame,width=650,height=500,bg='#EBF2F8')
    display_frame.place(x=250,y=0)
    display_frame.tkraise()
    ned_logo=Label(display_frame,image=img3,bg='#EBF2F8')
    ned_logo.place(x=-180,y=-200)
    instruction_label=Label(display_frame,text="Welcome To Student Portal",font=('Felix Titling',14,'bold'),bg='#EBF2F8')
    instruction_label.place(x=165,y=100)
    sp_logo=Label(display_frame,image=img4,bg='#EBF2F8')
    sp_logo.place(x=150,y=175)
    

def show_student_record():
    showrecord_frame=Frame(display_frame, width=650, height=500,bg='#FFFFFF')
    showrecord_frame.place(x=0,y=0)
    showrecord_frame.tkraise()
    headings=Label(showrecord_frame,bg='white',text="ROLL NO                  STATUS                   SUBJECT                     TIME                    DATE")
    headings.place(x=50,y=0)
    heading_seperator=Label(showrecord_frame,image=img10,bg='white')
    heading_seperator.place(x=-50,y=20)
    t=student_username_entry.get()+'.txt'
    try:
        p = Listbox(showrecord_frame, width=100, height=327, bd=0, bg='black', fg='white', font="Candara 12 bold")
        fr=open(t,'r')
        line=fr.readline()
        while line:
            p.insert(END,line)
            line=fr.readline()
        p.place(x=0, y=50)
        fr.close()
        back = Button(showrecord_frame, image=img20, command=home,highlightthickness=0)
        back.place(x=560, y=-10)
    except:
        tkinter.messagebox.showerror("ERROR","File is Empty")


admin_display_frame=None

def admin_portal():
    admin_dashboard_frame = Frame(admin_login_frame, width=250, height=500, bg='#1C2739')
    admin_dashboard_frame.place(x=0, y=0)
    admin_dashboard_frame.tkraise()
    dashboard_label = Label(admin_dashboard_frame, image=img5, bg='#1C2739')
    dashboard_label.place(x=5, y=5)
    divider_logo = Label(admin_dashboard_frame, image=img9, bg='#1C2739')
    divider_logo.place(x=0, y=60)
    dashboard_button_1 = Button(admin_dashboard_frame, image=img7, bd=0, bg='#1C2739', command=admin_record)
    dashboard_button_1.place(x=-30, y=120)
    dashboard_button_2 = Button(admin_dashboard_frame, image=img8, bd=0, bg='#1C2739', command=admin_login)
    dashboard_button_2.place(x=10, y=200)
    global admin_display_frame
    admin_display_frame = Frame(admin_login_frame, width=650, height=500,bg='#EBF2F8')
    admin_display_frame.place(x=250, y=0)
    admin_display_frame.tkraise()
    ned_logo = Label(admin_display_frame, image=img3,bg='#EBF2F8')
    ned_logo.place(x=200, y=10)
    admin_logo = Label(admin_display_frame, image=img19,bg='#EBF2F8')
    admin_logo.place(x=200, y=200)


def admin_authorize(event):
    if admin_username_entry.get()=='admin' and admin_password_entry.get()=='admin123':
        admin_portal()


def student_exit():
    main_window()


def admin_exit():
    main_window()

admin_username_entry=None
admin_password_entry=None
admin_login_frame=None

def admin_login():
    global admin_login_frame
    admin_login_frame=Frame(student_admin_frame,width=900,height=500,bg='black')
    admin_login_frame.place(x=0,y=0)
    admin_login_frame.tkraise()
    admin_icon=Label(admin_login_frame,image=img13,bd=0,bg='#EBF2F8')
    admin_icon.place(x=370,y=10)
    username_label=Label(admin_login_frame,text='Username',font=('Berlin Sans FB',16),bg='#EBF2F8')
    username_label.place(x=405,y=200)
    global admin_username_entry
    admin_username_entry=Entry(admin_login_frame,bg='white',relief='sunken',highlightcolor='#D2E0F1',highlightthickness=1,highlightbackground='#D8D6D7',font=('Tw Cen MT',14))
    admin_username_entry.place(x=350,y=240)
    password_label = Label(admin_login_frame, text='Password', font=('Berlin Sans FB', 16), bg='#EBF2F8')
    password_label.place(x=405, y=280)
    global admin_password_entry
    admin_password_entry = Entry(admin_login_frame, bg='white',show='*', relief='sunken', highlightcolor='#D2E0F1',highlightthickness=1,highlightbackground='#D8D6D7', font=('Tw Cen MT', 14))
    admin_password_entry.place(x=350, y=320)
    admin_password_entry.bind('<Return>',admin_authorize)
    login_button=Button(admin_login_frame,image=img24,bd=0,bg='#EBF2F8')
    login_button.bind('<Button-1>',admin_authorize)
    login_button.place(x=357,y=380)
    cancel_button=Button(admin_login_frame,image=img14,bd=0,bg='#EBF2F8',command=admin_exit)
    cancel_button.place(x=357,y=430)


student_admin_frame=None

def main_window():
    global student_admin_frame
    student_admin_frame = Frame(root, width=900, height=500,bg="#EBF2F8")
    student_admin_frame.place(x=0, y=0)
    instruction_label=Label(student_admin_frame,text="Welcome To The Attendance System",font=('Felix Titling',25,'bold'),bg='Green')
    instruction_label.place(x=230,y=200)
    main_logo_image=Label(student_admin_frame,image=img23,bg='#EBF2F8')
    main_logo_image.place(x=200,y=50)
    black_button_student = Button(student_admin_frame,image=img11, bd=0, command=student_login,bg="#EBF2F8")
    black_button_student.place(x=100, y=300)
    black_button_teacher = Button(student_admin_frame,image=img12, bd=0, command=admin_login,bg="#EBF2F8")
    black_button_teacher.place(x=500, y=300)


root=Tk()
root.geometry("900x500")
root.title("Attendance System")
img3=PhotoImage(file='ned-student-portal-logo.gif')
img4=PhotoImage(file='student_portal-logo.png')
img5=PhotoImage(file='dashboard-logo.png')
img6=PhotoImage(file='attendance-logo.png')
img7=PhotoImage(file='view-records-logo.png')
img8=PhotoImage(file='logout-logo.png')
img9=PhotoImage(file='divider-logo.png')
img10=PhotoImage(file='heading-seperator.png')
img11=PhotoImage(file='student-login1.gif')
img12=PhotoImage(file='admin-login1.gif')
img20=PhotoImage(file='back-button2.png')
img21=PhotoImage(file='show-record-button.png')
img23=PhotoImage(file='main.png')
img24=PhotoImage(file='login-button.png')
img13=PhotoImage(file='admin-icon.png')
img14=PhotoImage(file='cancel-button.png')
img15=PhotoImage(file='student-icon.png')
img16=PhotoImage(file='dropdown.png')
img17=PhotoImage(file='take-attendance.png')
img18=PhotoImage(file='back-button.png')
img19=PhotoImage(file='admin-portal-logo.png')


main_window()

root.mainloop()
