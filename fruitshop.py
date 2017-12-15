from tkinter import *
d = {'mango': '100', 'cherry': '50', 'apple': '200', 'guava': '60', 'orange': '100'}
pricelist=list(d.values())
def calc_bill():
    v1=float(var1.get())
    v2=float(var2.get())
    v3=float(var3.get())
    v4=float(var4.get())
    v5=float(var5.get())
    new_list = []
    for item in pricelist:
        new_list.append(float(item))
    calc_bill.amt=0
    if v1!=0:
        en1 = float(qen1.get())
        calc_bill.amt+=float(v1*new_list[0]*en1)
    if v2!=0:
        en2 = float(qen2.get())
        calc_bill.amt += float(v2 * new_list[1] * en2)
    if v3!=0:
        en3 = float(qen3.get())
        calc_bill.amt += float(v3 * new_list[2] * en3)
    if v4!=0:
        en4 = float(qen4.get())
        calc_bill.amt += float(v4*new_list[3]*en4)
    if v5!=0:
        en5 = float(qen5.get())
        calc_bill.amt += float(v5*new_list[4]*en5)

    calc_bill.service_tax=10/100*calc_bill.amt
    calc_bill.amt+=calc_bill.service_tax
    billamt.config(text="bill amount is %s" % calc_bill.amt)


def calc_change():
    bill=calc_bill.amt
    st=calc_bill.service_tax
    paidamt=float(paiden.get())
    change = float(paidamt-bill)
    changeamt.config(text="change due %s" % change)



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

mainloop()