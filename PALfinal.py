
import tkinter
from tkinter import *
def float_bin1(my_number, places = 3):  
    my_whole, my_dec = str(my_number).split(".") 
    my_whole = int(my_whole) 
    res = (str(bin(my_whole))+".").replace('0b','') 
  
    for x in range(places): 
        my_dec = str('0.')+str(my_dec) 
        temp = '%1.20f' %(float(my_dec)*2) 
        my_whole, my_dec = temp.split(".") 
        res += my_whole 
    return res 

def flip1(c):
    return '1' if(c == '0') else '0'; 

def xor_c1(a,b):
    return '0' if(a == b) else '1';

def xor_c():
    txt=StringVar()
    txt=entry1.get()
    a=txt.split()
    
    
    #a=int(input("Enter first number"))
    #b=int(input("Enter second number"))
    answer["text"]='0' if(a[0] == a[1]) else '1'

def flip():
    c=IntVar()
    c=entry1.get()
    #c=int(input("Enter number to be flipped"))
    
        
    answer["text"]='1' if(c == '0') else '0'

def binarytoGray():
    binary=StringVar()
    binary=entry1.get()
    #binary=input("Enter number in binary")
    
    gray = ""; 
  
    
    gray += binary[0]; 
  
    
    for i in range(1,len(binary)): 
          
        
        gray += xor_c1(binary[i - 1],  
                      binary[i]); 
  
    answer["text"]= gray 
  



def graytoBinary():
    gray=StringVar()
    gray=entry1.get()
    #gray=input("Enter number in binary")
  
    binary = ""; 
  
    
    binary += gray[0]; 
  
     
    for i in range(1, len(gray)): 
          
        
        if (gray[i] == '0'): 
            binary += binary[i - 1]; 
  
        
        else: 
            binary += flip1(binary[i - 1]); 
  
    answer["text"]= binary; 
  



def bcd_to_int():
    x=StringVar()
    x=entry1.get()
    x=int(x)
    #x=int(input("Enter number to be converted into decimal"))
    
    

    if x < 0:
        raise ValueError("Cannot be a negative integer")

    binstring = ''
    while True:
        q, r = divmod(x, 10)
        nibble = bin(r).replace('0b', "")
        while len(nibble) < 4:
            nibble = '0' + nibble
        binstring = nibble + binstring
        if q == 0:
            break
        else:
            x = q

    answer["text"]=int(binstring, 2)





def int_to_bcd():
    x=StringVar()
    x=entry1.get()
    x=int(x)
    #x=int(input("Enter number to be converted into BCD"))
    
    if x < 0:
        raise ValueError("Cannot be a negative integer")
        
    if x == 0:
        return 0
        
    bcdstring = ''
    while x > 0:
        nibble = x % 16
        bcdstring = str(nibble) + bcdstring
        x >>= 4
    answer["text"]=int(bcdstring)



 
def float_bin():
    my_number=StringVar()
    
    my_number=entry1.get()
    my_number=float(my_number)
    places=3
    #my_number=float(input("Enter number to be converted into binary"))
    my_whole, my_dec = str(my_number).split(".") 
    my_whole = int(my_whole) 
    res = (str(bin(my_whole))+".").replace('0b','') 
  
    for x in range(places): 
        my_dec = str('0.')+str(my_dec) 
        temp = '%1.20f' %(float(my_dec)*2) 
        my_whole, my_dec = temp.split(".") 
        res += my_whole 
    answer["text"]=res 
  
  
  
def IEEE754():
    n=StringVar()
    
    n=entry1.get()
    n=float(n)
    #n=float(input("Enter number to represent it in floating point format"))
    
    sign = 0
    if n < 0 :  
        sign = 1
        n = n * (-1)  
    p = 30
    # convert float to binary 
    dec = float_bin1 (n, places = p) 
  
    dotPlace = dec.find('.') 
    onePlace = dec.find('1') 
    
    if onePlace > dotPlace: 
        dec = dec.replace(".","") 
        onePlace -= 1
        dotPlace -= 1
    elif onePlace < dotPlace: 
        dec = dec.replace(".","") 
        dotPlace -= 1
    mantissa = dec[onePlace+1:] 
  
    
    exponent = dotPlace - onePlace 
    exponent_bits = exponent + 127
  
    
    exponent_bits = bin(exponent_bits).replace("0b",'')  
  
    mantissa = mantissa[0:23] 
  
      
    final = str(sign) + exponent_bits.zfill(8) + mantissa 
  
     
    hstr = '0x%0*X' %((len(final) + 3) // 4, int(final, 2))  
    answer["text"] =(hstr[2:], final)

def hexadecimal():
    n=StringVar()
    n=entry1.get()
    n=int(n)
    #n=int(input("Enter number to represent in hexadecimal format"))
    h=hex(n)
    answer["text"]=h[2:]

def octal():
    n=StringVar()
    n=entry1.get()
    n=int(n)
    #n=int(input("Enter number to represent in octal format"))
    o=oct(n)
    answer["text"]= o[2:]


root=Tk()
root.title("Converter")
canvas1=tkinter.Canvas(root,width=400,height=300)
canvas1.pack()
entry1=tkinter.Entry(root)
canvas1.create_window(200,140,window=entry1)





  

bt1=Button(root,text='XOR',command=xor_c,activeforeground='white',bg='black',activebackground='goldenrod1',fg='white',font=('Airal',12))
bt1.pack()
bt1.place(x=170,y=400)

bt2=Button(root,text='Flip',command=flip,activeforeground='white',bg='black',activebackground='goldenrod1',fg='white',font=('Airal',12))
bt2.pack()
bt2.place(x=370,y=400)

bt3=Button(root,text='Gray',command=binarytoGray,activeforeground='white',bg='black',activebackground='goldenrod1',fg='white',font=('Airal',12))
bt3.pack()
bt3.place(x=570,y=400)

bt4=Button(root,text='Binary',command=graytoBinary,activeforeground='white',bg='black',activebackground='goldenrod1',fg='white',font=('Airal',12))
bt4.pack()
bt4.place(x=770,y=400)

bt5=Button(root,text='Decimal',command=bcd_to_int,activeforeground='white',bg='black',activebackground='goldenrod1',fg='white',font=('Airal',12))
bt5.pack()
bt5.place(x=970,y=400)

bt6=Button(root,text='BCD',command=int_to_bcd,activeforeground='white',bg='black',activebackground='goldenrod1',fg='white',font=('Airal',12))
bt6.pack()
bt6.place(x=170,y=600)

bt7=Button(root,text='Floating Binary',command=float_bin,activeforeground='white',bg='black',activebackground='goldenrod1',fg='white',font=('Airal',12))
bt7.pack()
bt7.place(x=370,y=600)

bt8=Button(root,text='Floating point',command=IEEE754,activeforeground='white',bg='black',activebackground='goldenrod1',fg='white',font=('Airal',12))
bt8.pack()
bt8.place(x=570,y=600)

bt9=Button(root,text='Hexadecimal',command=hexadecimal,activeforeground='white',bg='black',activebackground='goldenrod1',fg='white',font=('Airal',12))
bt9.pack()
bt9.place(x=770,y=600)

bt10=Button(root,text='Octal',command=octal,activeforeground='white',bg='black',activebackground='goldenrod1',fg='white',font=('Airal',12))
bt10.pack()
bt10.place(x=970,y=600)

answer=Message(root,text="Answer")
answer.config(font=('Airal',15),width=400)
answer.place(x=700,y=200)
mainloop()


