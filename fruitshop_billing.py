'''
project name:Fruit Shop Billing System
author:Ramya Sreedhar

This is a simple program to Calculate the bill amount and change for the quantities in kg  of the selected fruits ...
'''
#importing the GUI tkinter
from tkinter import *

'''----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

LIST OF CONFIGURABLE ITEMS/GLOBAL VARIABLES

'''
d = {'mango': '100', 'cherry': '50', 'apple': '200', 'guava': '60', 'orange': '100'}#listing the price fr the specific fruits per kg
pricelist=list(d.values())#takes the dictionary price values
ERROR=False
SERVICETAX=0.10 #can be configured as per your region
AMOUNT = 0.0
'''--------------------------------------------------------------------------------------------------------''''''---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

FUNCTION DESCRIPTIONS STARTS  HERE

----------------------------------------------------------------------------------------''''''----------------------------------------------------------------------------------------------------------------'''
'''
Name  : calc_bill
Desc  : calc_bill  function calculates the total amount of the bill using the 3 lists for the checkboxes,
quantity entries and the list of prices and the global variables d,pricelist,SERVICCETAX and AMOUNT

type  : calc_b]ill ( [list of Bool] , [List of Float numbers] , [List of float )
arguments: none
dependencies:calls the calc_price function ,global variables d,pricelist,SERVICCETAX and AMOUNT
return type: none
''''''---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
def calc_bill( ):
    global SERVICETAX
    global AMOUNT

    list_chkbox=[]#checkbox variables converted to float added to this list

    list_chkbox.append(float(var1.get()))
    list_chkbox.append(float(var2.get()))
    list_chkbox.append(float(var3.get()))
    list_chkbox.append(float(var4.get()))
    list_chkbox.append(float(var5.get()))


    try:
        list_qtyentry=[] #list of entries for quantity
        list_qtyentry.append(qen1.get())
        list_qtyentry.append(qen2.get())
        list_qtyentry.append(qen3.get())
        list_qtyentry.append(qen4.get())
        list_qtyentry.append(qen5.get())
    except:

        ERROR = True
        print('Conversion failure while passing entries. Please check again')
        sys.exit(1)

    price_list = []
    for item in pricelist:
        price_list.append(float(item))
    calc_bill.amt=0
    qty_list=[]
    prc_list=[]
    for i in range(0,len(list_chkbox),1):
        if list_chkbox[i]!= 0:
            try:
                qty_list.append(float(list_qtyentry[i]))
                prc_list.append(price_list[i])
            except:
                error=True
                print('Invalid characters found in the qty entry %s' %i)
                billamt.config(text='Quantiy entry %s is invalid' % i)
                sys.exit(1)
    AMOUNT = calc_price(qty_list,prc_list)
    AMOUNT = AMOUNT + (AMOUNT * SERVICETAX)
    billamt.config(text="Your Bill Amount is %s" % AMOUNT)

'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
'''
Name:calc_price()
desc:this function calculates the total price of the purchased fruits using the two lists quantity list and price list
arguments:Quantity_list,price_List. It returns the price
return type:float 

'''
'''-------------------------------------------------------------------------------------------------------------------'''
def calc_price(Quantity_list,price_List):
    price = 0.0
    if(len(Quantity_list) != len(price_List) ):
        #error
        return 0
    else:
        for index in range( 0 , len(Quantity_list), 1):
            price = price + ( Quantity_list[index] * price_List[index])
        return price

'''----------------------------------------------------------------------------------------------------------------------------------'''
'''
Name:calc_change

Desc:calculates the change to be returned by subtracting the amount paid entry value from the bill amount
and returns the change amount and prints the same

dependencies:calls the global variable AMOUNT

return type: float

'''
'''--------------------------------------------------------------------------------------------------------------------------------'''



def calc_change():
    global AMOUNT
    paidamt=float(paiden.get())
    change = float(paidamt-AMOUNT)
    changeamt.config(text="change due %s" % change)
    return change
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''
The Program execution starts here
--------------------------------------------------------------------'''


root=Tk()
root.title("Fruit Shop Billing System")
root.geometry("300x400")
Label(root, text="Available Fruits list:").grid(row=0)
Label(root,text='Fruit').grid(row=1,column=0,padx=20,sticky=W)
Label(root,text='Price').grid(row=1,column=1,sticky=W)
Label(root,text='Quantity').grid(row=1,column=3,sticky=W)

var1 = IntVar()
Checkbutton(root,text="mango",variable=var1).grid(row=2,column=0, sticky=W)
lbl1=Label(root,text=str(pricelist[0])).grid(row=2,column=1)
qen1=Entry(root)
qen1.grid(row=2,column=3)
var2 = IntVar()
Checkbutton(root, text="cherry",variable=var2).grid(row=3,column=0, sticky=W)
lbl2=Label(root,text=str(pricelist[1])).grid(row=3,column=1)
qen2=Entry(root)
qen2.grid(row=3,column=3)
var3 = IntVar()
Checkbutton(root, text="apple",variable=var3).grid(row=4,column=0, sticky=W)
lbl3=Label(root,text=str(pricelist[2])).grid(row=4,column=1)
qen3=Entry(root)
qen3.grid(row=4,column=3)
var4 = IntVar()
Checkbutton(root, text="guava",variable=var4).grid(row=5,column=0, sticky=W)
lbl4=Label(root,text=str(pricelist[3])).grid(row=5,column=1)
qen4=Entry(root)
qen4.grid(row=5,column=3)
var5 = IntVar()
Checkbutton(root, text="orange",variable=var5).grid(row=6,column=0, sticky=W)
lbl5=Label(root,text=str(pricelist[4])).grid(row=6,column=1)
qen5=Entry(root)
qen5.grid(row=6,column=3)
Button(root, text='Bill',command=calc_bill).grid(row=7, sticky=W, pady=4)
billamt=Label(root,text="")
billamt.grid(row=8)
amtlbl=Label(root,text="enter the amount paid").grid(row=9)
paiden=Entry(root)
paiden.grid(row=10)
lbldummy=Label(root,text='').grid(row=11)
Button(root, text='Change',command=calc_change).grid(row=12, sticky=W)
changeamt=Label(root,text="")
changeamt.grid(row=13)
lblvalen=Label(root,text="")
lblvalen.grid(row=14)
mainloop()
'''--------------------------------------END OF FILE-----------------------------------------------------------------------'''