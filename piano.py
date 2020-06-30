#==============================Credentials=============================
#                     Progrme by  Harsh Yadav
#========================================================================


#importing necessary libraries

from tkinter import *
import time
import datetime
import pygame
#coding will start from here

#-----intialising frames of application---------
program.init()
root = TK()
root.title("Virtual Piano")
root.geometery('1352 x 1700 + 0 + 0')
root.configure(background = "#fff")

cdr = frame(root, bg="#5bd", bd=20, relief=RIDGE)
cdr.grid()

cdr1 = frame(root, bg="#5bd", bd=20, relief=RIDGE)
cdr1.grid()

cdr2 = frame(root, bg="#5bd", relief=RIDGE)
cdr2.grid()

cdr3 = frame(root, bg="#5bd", relief=RIDGE)
cdr3.grid()

#-------diffrent string variables for displaying necessary info------

str1 = StringVar()
str1.set("Piano is awesome!")

date1 = StringVar()
time1 = StringVar()

date1.set(time.strtime("%d/%m/%Y"))
time1.set(time.strtime("%H:%M:%S"))

#--------------main label tuple -------------
Label(cdr1, text="Virtual PIANO", font=('arial',25, 'bold'), padx = 8, pady = 8, bd = 4, bg ="#5bd",
fg = "#ffbfa1", width=28, justify=CENTER).grid(row = 0 , column = 0, columnspan = 11 )

#---------defining commandlines for piano keys-------
def value_CS():
    str1.set("C#")
    sound = pygame.mixer.Sound("C:\Users\rc\SkyDrive\Documents\PIANO PROJECT\Music_Notes\C_s.wav")
    sound.play
    return

def value_DS():
    str1.set("D#")
    sound = pygame.mixer.Sound("C:\Users\rc\SkyDrive\Documents\PIANO PROJECT\Music_Notes\D_s.wav")
    sound.play
    return

def value_FS():
    str1.set("F#")
    sound = pygame.mixer.Sound("C:\Users\rc\SkyDrive\Documents\PIANO PROJECT\Music_Notes\F_s.wav")
    sound.play
    return


def value_GS():
    str1.set("G#")
    sound = pygame.mixer.Sound("C:\Users\rc\SkyDrive\Documents\PIANO PROJECT\Music_Notes\G_s.wav")
    sound.play
    return

def value_Bb():
    str1.set("Bb")
    sound = pygame.mixer.Sound("C:\Users\rc\SkyDrive\Documents\PIANO PROJECT\Music_Notes\Bb.wav")
    sound.play
    return

def value_CS1():
    str1.set("C#1")
    sound = pygame.mixer.Sound("C:\Users\rc\SkyDrive\Documents\PIANO PROJECT\Music_Notes\C_s1.wav")
    sound.play
    return

def value_DS1():
    str1.set("D#1")
    sound = pygame.mixer.Sound("C:\Users\rc\SkyDrive\Documents\PIANO PROJECT\Music_Notes\D_s1.wav")
    sound.play
    return

def value_C():
    str1.set("C")
    sound = pygame.mixer.Sound("C:\Users\rc\SkyDrive\Documents\PIANO PROJECT\Music_Notes\C.wav")
    sound.play
    return

def value_D():
    str1.set("D")
    sound = pygame.mixer.Sound("C:\Users\rc\SkyDrive\Documents\PIANO PROJECT\Music_Notes\D.wav")
    sound.play
    return

def value_E():
    str1.set("E")
    sound = pygame.mixer.Sound("C:\Users\rc\SkyDrive\Documents\PIANO PROJECT\Music_Notes\E.wav")
    sound.play
    return


def value_F():
    str1.set("F")
    sound = pygame.mixer.Sound("C:\Users\rc\SkyDrive\Documents\PIANO PROJECT\Music_Notes\F.wav")
    sound.play
    return

def value_G():
    str1.set("G")
    sound = pygame.mixer.Sound("C:\Users\rc\SkyDrive\Documents\PIANO PROJECT\Music_Notes\G.wav")
    sound.play
    return

def value_A():
    str1.set("A")
    sound = pygame.mixer.Sound("C:\Users\rc\SkyDrive\Documents\PIANO PROJECT\Music_Notes\A.wav")
    sound.play
    return

def value_B():
    str1.set("D#1")
    sound = pygame.mixer.Sound("C:\Users\rc\SkyDrive\Documents\PIANO PROJECT\Music_Notes\B.wav")
    sound.play
    return

def value_C1():
    str1.set("C1")
    sound = pygame.mixer.Sound("C:\Users\rc\SkyDrive\Documents\PIANO PROJECT\Music_Notes\C1.wav")
    sound.play
    return

def value_D1():
    str1.set("D1")
    sound = pygame.mixer.Sound("C:\Users\rc\SkyDrive\Documents\PIANO PROJECT\Music_Notes\D1.wav")
    sound.play
    return

def value_E1():
    str1.set("E1")
    sound = pygame.mixer.Sound("C:\Users\rc\SkyDrive\Documents\PIANO PROJECT\Music_Notes\E1.wav")
    sound.play
    return

def value_F1():
    str1.set("F1")
    sound = pygame.mixer.Sound("C:\Users\rc\SkyDrive\Documents\PIANO PROJECT\Music_Notes\F1.wav")
    sound.play
    return





#-----info textlayout tuples-----------------------------------

txtDate(cdr1, textvariable=date1, font=('arial',18, 'bold'), bd = 4, bg ="#5bd",
fg = "#ffbfa1",width=28, justify=CENTER).grid(row = 0 , column = 0, pady=1 )

txtDisplay(cdr1, textvariable=str1, font=('arial',18, 'bold'), bd = 34, bg ="#5bd",
fg = "#ffbfa1",width=28 justify=CENTER).grid(row = 0 , column = 1, pady=1 )


txtTime(cdr1, textvariable=time1, font=('arial',18, 'bold'), bd = 34, bg ="#5bd",
fg = "#ffbfa1",width=28 justify=CENTER).grid(row = 0 , column = 2, pady=1 )

#-------primary keylayout tuples-------------------------------

btnCS = Button(cdr2, height = 6, width = 6, bd =4, text="C#", font=('arial',18, 'bold'), bg ="#000", fg="white", command = value_CS)
btnCS.grid(row = 0 , column = 0, padx = 5, pady = 5)

btnDS = Button(cdr2, height = 6, width = 6, bd =4, text="D#", font=('arial',18, 'bold'), bg ="#000", fg="white",command = value_DS)
btnDS.grid(row = 0 , column = 1, padx = 5, pady = 5)

btnSpace2 = Button(cdr2, state = DISABLED, height = 6, width = 2, bg ="#5BD", relief = FLAT)
btnSpace2.grid(row = 0 , column = 3, padx = 5, pady = 5)

btnFS = Button(cdr2, height = 6, width = 6, bd =4, text="F#", font=('arial',18, 'bold'), bg ="#000", fg = "#FFF",command = value_FS)
btnFS.grid(row = 0 , column = 4, padx = 5, pady = 5)

btnGS = Button(cdr2, height = 6, width = 6, bd =4, text="F#", font=('arial',18, 'bold'), bg ="#000", fg = "#FFF",command = value_GS)
btnGS.grid(row = 0 , column = 4, padx = 5, pady = 5)

btnBb = Button(cdr2, height = 6, width = 6, bd =4, text="G#", font=('arial',18, 'bold'), bg ="#000", fg="white", command = value_Bb)
btnBb.grid(row = 0 , column = 6, padx = 5, pady = 5)


btnSpace5 = Button(cdr2, state = DISABLED, height = 6, width = 2, bg ="#5BD", relief = FLAT)
btnSpace5.grid(row = 0 , column = 9, padx = 5, pady = 5)

btnCS1 = Button(cdr2, height = 6, width = 6, bd =4, text="C#1", font=('arial',18, 'bold'), bg ="#000", fg="white", command = value_CS1)
btnCS1.grid(row = 0 , column = 10, padx = 5, pady = 5)

btnDS1 = Button(cdr2, height = 6, width = 6, bd =4, text="D#1", font=('arial',18, 'bold'), bg ="#000", fg="white", command = value_DS1)
btnDS1.grid(row = 0 , column = 12, padx = 5, pady = 5)

#---------------main keylayout tuples---------------------------------------

btnC = Button(cdr3, height = 8, width = 6, bd =4, text="C", font=('arial',18, 'bold'), bg ="#FFF", fg="#000", command = value_C)
btnC.grid(row = 0 , column = 0, padx = 5, pady = 5)
btnD = Button(cdr3, height = 8, width = 6, bd =4, text="D", font=('arial',18, 'bold'), bg ="#FFF", fg="#000", command = value_D)
btnD.grid(row = 0 , column = 1, padx = 5, pady = 5)
btnE = Button(cdr3, height = 8, width = 6, bd =4, text="E", font=('arial',18, 'bold'), bg ="#FFF", fg="#000",command = value_E)
btnE.grid(row = 0 , column = 2, padx = 5, pady = 5)
btnF = Button(cdr3, height = 8, width = 6, bd =4, text="F", font=('arial',18, 'bold'), bg ="#FFF", fg="#000", command = value_F)
btnF.grid(row = 0 , column = 3, padx = 5, pady = 5)

btnG = Button(cdr3, height = 8, width = 6, bd =4, text="G", font=('arial',18, 'bold'), bg ="#FFF", fg="#000", command = value_G)
btnG.grid(row = 0 , column = 4, padx = 5, pady = 5)
btnA = Button(cdr3, height = 8, width = 6, bd =4, text="A", font=('arial',18, 'bold'), bg ="#FFF", fg="#000", command = value_A)
btnA.grid(row = 0 , column = 5, padx = 5, pady = 5)
btnB = Button(cdr3, height = 8, width = 6, bd =4, text="B", font=('arial',18, 'bold'), bg ="#FFF", fg="#000", command = value_B)
btnB.grid(row = 0 , column = 6, padx = 5, pady = 5)

btnC1 = Button(cdr3, height = 8, width = 6, bd =4, text="C1", font=('arial',18, 'bold'), bg ="#FFF", fg="#000", command = value_C1)
btnC1.grid(row = 0 , column = 7, padx = 5, pady = 5)
btnD1 = Button(cdr3, height = 8, width = 6, bd =4, text="D1", font=('arial',18, 'bold'), bg ="#FFF", fg="#000", command = value_D1)
btnD1.grid(row = 0 , column = 8, padx = 5, pady = 5)
btnE1 = Button(cdr3, height = 8, width = 6, bd =4, text="E1", font=('arial',18, 'bold'), bg ="#FFF", fg="#000", command = value_E1)
btnE1.grid(row = 0 , column = 9, padx = 5, pady = 5)
btnF1 = Button(cdr3, height = 8, width = 6, bd =4, text="F1", font=('arial',18, 'bold'), bg ="#FFF", fg="#000", command = value_F1)
btnF1.grid(row = 0 , column = 10, padx = 5, pady = 5)

#-----------program ends :)---------------------------------------------------------

                                              
