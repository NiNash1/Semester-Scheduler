from tkinter import *
import csv
root=Tk()
root.title("Semester Scheduler")
root.iconbitmap('C:/Users/avina/Desktop/CODES/Python Programs/ScheduleNotiApp/Schedule.ico')

Subjects=["Computer Programming: Python","Basic Electronics","Calculus","Engineering Physics"," Quantitative Skills Practice I"]
TimeslotsTh=["8:00-8:50","9:00-9:50","10:00-10:50","11:00-11:50","12:00-12:50","14:00-14:50","15:00-15:50","16:00-16:50","17:00-17:50",
            "18:00-18:50","19:00-19:50"]
TimeslotsPr=["8:00-8:50","8:51-9:40",]
Days=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]


def submission():
    global entry
    entry=[typeclass.get(),sub.get(),time.get(),day.get()]
    f=open("schedule.csv","r")
    csvr=csv.reader(f)
    if entry in csvr:
        label_submit=Label(root,text=" Already exists goldfish").grid(row=5,column=0)
        f.close()
    else:
        f.close()
        label_submit=Label(root,text="Submitted").grid(row=5,column=0)
        with open("schedule.csv",mode = 'a') as f:
            mywriter = csv.writer(f, delimiter = ',')
            mywriter.writerow(entry)
        f.close()

typeclass=StringVar()
typeclass.set("Theory")

sub=StringVar()
sub.set(Subjects[0])

time=StringVar()
time.set(TimeslotsTh[0])

day=StringVar()
day.set(Days[0])

def update_timeslotandtypedrop(self):
    if typeclass.get()=="Theory":
        timedrop=OptionMenu(root,time,*TimeslotsTh).grid(row=2,column=1)
        
    else:
        timedrop=OptionMenu(root,time,*TimeslotsPr).grid(row=2,column=1)


#Menus
typedrop=OptionMenu(root,typeclass,"Theory","Practical",command= update_timeslotandtypedrop).grid(row=0,column=1)
subdrop=OptionMenu(root,sub,*Subjects).grid(row=1,column=1)
daydrop=OptionMenu(root,day,*Days).grid(row=3,column=1)


label_type=Label(root,text="Type of class:").grid(row=0,column=0)
label_subject=Label(root,text="Subject:").grid(row=1,column=0)
label_time=Label(root,text="Timeslot:").grid(row=2,column=0)
label_day=Label(root,text="Day:").grid(row=3,column=0)


button_quit=Button(root,text="Exit",command=root.quit).grid(row=4,column=0)
button_submit=Button(root,text="Submit",command=submission).grid(row=4,column=1)



root.mainloop()

