from tkinter import *
from tkinter import messagebox,END
import random,os,tempfile,smtplib

#functionality part
def clear():

    bathSoapEntry.delete(0,END)
    faceCreamEntry.delete(0,END)
    faceWashEntry.delete(0,END)
    hairSprayEntry.delete(0,END)
    hairGelEntry.delete(0,END)
    bodyLotionEntry.delete(0,END)

    bathSoapEntry.insert(0,0)
    faceCreamEntry.insert(0,0)
    faceWashEntry.insert(0,0)
    hairSprayEntry.insert(0,0)
    hairGelEntry.insert(0,0)
    bodyLotionEntry.insert(0,0)

    riceEntry.delete(0,END)
    oilEntry.delete(0,END)
    daalEntry.delete(0,END)
    wheatEntry.delete(0,END)
    sugarEntry.delete(0,END)
    teaEntry.delete(0,END)

    riceEntry.insert(0,0)
    oilEntry.insert(0,0)
    daalEntry.insert(0,0)
    wheatEntry.insert(0,0)
    sugarEntry.insert(0,0)
    teaEntry.insert(0,0)

    maazaEntry.delete(0,END)
    pepsiEntry.delete(0,END)
    spriteEntry.delete(0,END)
    dewEntry.delete(0,END)
    frootiEntry.delete(0,END)
    cocaColaEntry.delete(0,END)

    maazaEntry.insert(0,0)
    pepsiEntry.insert(0,0)
    spriteEntry.insert(0,0)
    dewEntry.insert(0,0)
    frootiEntry.insert(0,0)
    cocaColaEntry.insert(0,0)

    cosmeticsPriceEntry.delete(0,END)
    groceryPriceEntry.delete(0,END)
    drinksPriceEntry.delete(0,END)

    cosmeticsTaxEntry.delete(0,END)
    groceryTaxEntry.delete(0,END)
    drinksTaxEntry.delete(0,END)

    nameEntry.delete(0,END)
    phoneEntry.delete(0,END)
    billNoEntry.delete(0,END)

    textArea.delete(1.0,END)
    

def send_email():
    def send_gmail():
        try:
            ob=smtplib.SMTP('smtp.gmail.com',587)
            ob.starttls()
            ob.login(senderEntry.get(),passwordEntry.get())
            message = email_TextArea.get(1.0,END)
            recieveraddress = recieverEntry.get()
            ob.sendmail(senderEntry.get(),recieveraddress,message)
            ob.quit()
            messagebox.showinfo('Success','Bill is successfully sent',parent=root1)
            root1.destroy()
        except:
            messagebox.showerror('Error','Something went wrong, Please try again',parent=root1)
    if textArea.get(1.0,END) == '\n':
        messagebox.showerror('Error','Bill is empty')
    else:
        root1=Toplevel()
        root1.grab_set()
        root1.title('Send E-mail')
        root1.config(bg='gray20')
        root1.resizable(0,0)

        senderFrame = LabelFrame(
            root1,
            text='SENDER',
            font=('montserrat', 16, 'bold'),
            bg='gray20',  
            fg='gold',  
            bd=6,
            relief=GROOVE
        )
        senderFrame.grid(row=0,column=0,padx=40,pady=20)

        senderLabel = Label(
            senderFrame,
            text="Sender's Email",
            font=('montserrat', 14, 'bold'),
            bg='gray20',
            fg='white'
        )
        senderLabel.grid(row=0, column=0,padx=10,pady=8,sticky='w')

        senderEntry = Entry(
            senderFrame,
            font=('montserrat', 14),
            bd=2,
            width=23,
            relief=RIDGE 
        )
        senderEntry.grid(row=0,column=1,padx=10,pady=8)

        passwordLabel = Label(
            senderFrame,
            text="Sender's Password",
            font=('montserrat', 14,'bold'),
            bg='gray20',
            fg='white'
        )
        passwordLabel.grid(row=1, column=0,padx=10,pady=8,sticky='w')

        passwordEntry = Entry(
            senderFrame,
            font=('montserrat', 14,),
            bd=2,
            width=23,
            relief=RIDGE,
            show='*'
        )
        passwordEntry.grid(row=1,column=1,padx=10,pady=8)


        recipientFrame = LabelFrame(
            root1,
            text='RECIPIENT',
            font=('montserrat', 16, 'bold'),
            bg='gray20',  
            fg='gold',  
            bd=6,
            relief=GROOVE
        )
        recipientFrame.grid(row=1,column=0,padx=40,pady=20)


        recieverLabel = Label(
            recipientFrame,
            text="Reciever's Email",
            font=('montserrat', 14,'bold'),
            bg='gray20',
            fg='white'
        )
        recieverLabel.grid(row=0,column=0,padx=10,pady=8,sticky='w')

        recieverEntry = Entry(
            recipientFrame,
            font=('montserrat', 14,),
            bd=2,
            width=23,
            relief=RIDGE 
        )
        recieverEntry.grid(row=0,column=1,padx=10,pady=8)


        messageLabel = Label(
            recipientFrame,
            text="Message",
            font=('montserrat', 14,'bold'),
            bg='gray20',
            fg='white'
        )
        messageLabel.grid(row=1,column=0,padx=10,pady=8,sticky='w')

        email_TextArea = Text(
            recipientFrame,
            font=('montserrat', 14),
            bd=2,
            relief=SUNKEN,
            height=11,
            width=42

        )
        email_TextArea.grid(row=2,column=0,columnspan=2)
        email_TextArea.delete(1.0,END)
        email_TextArea.insert(END,textArea.get(1.0,END).replace('=','').replace('-','').replace('\t\t\t','\t\t'))

        sendbutton = Button(
            root1,
            text='SEND',
            font=('montserrat', 16,'bold'),
            width=15,
            bd=7,
            command=send_gmail
            
        )
        sendbutton.grid(row=2,column=0,pady=20)


        root1.mainloop()
def print_bill():
    if textArea.get(1.0,END) == '\n':
        messagebox.showerror('Error','Bill is empty')
    else:
        file=tempfile.mktemp('.txt')
        open(file,'w').write(textArea.get(1.0,END))
        os.startfile(file,'print')


def search_bill():
    bill_number = billNoEntry.get().strip()  # Remove leading/trailing spaces
    found = False  

    try:
        for filename in os.listdir('bills/'):
            print(f"Checking file: {filename}")  # Debugging line
            if filename.split('.')[0] == bill_number:  # Compare without extension
                # Open and display the content of the matched file
                with open(f'bills/{filename}', 'r') as fread:
                    textArea.delete(1.0, END)  # Clear the text area
                    textArea.insert(END, fread.read())  # Insert the file's content
                found = True
                break

        if not found:
            raise FileNotFoundError  # Raise an error if no match is found

    except FileNotFoundError:
        messagebox.showerror('Error', 'Invalid Bill Number')
    except Exception as e:
        messagebox.showerror('Error', f"An unexpected error occurred: {e}")

def total():
    global soapprice,facecreamprice,facewashprice,hairgelprice,hairsparayprice,bodylotionprice,cosmeticstax
    #cosmetics calculation
    soapprice=int(bathSoapEntry.get())*20
    facecreamprice=int(faceCreamEntry.get())*50
    facewashprice=int(faceWashEntry.get())*60
    hairsparayprice=int(hairSprayEntry.get())*100
    hairgelprice=int(hairGelEntry.get())*55
    bodylotionprice=int(bodyLotionEntry.get())*75

    totalcosmeticprice = soapprice+facecreamprice+facewashprice+hairgelprice+hairsparayprice+bodylotionprice

    cosmeticsPriceEntry.delete(0,END)
    cosmeticsPriceEntry.insert(0,f'{totalcosmeticprice} Rs') 
    cosmeticstax=totalcosmeticprice*0.12

    cosmeticsTaxEntry.delete(0,END)
    cosmeticsTaxEntry.insert(0,f'{cosmeticstax} Rs')

    #grocery calculation
    global riceprice,oilprice,daalprice,wheatprice,sugarprice,teaprice,grocerytax
    riceprice=int(riceEntry.get())*120
    oilprice=int(oilEntry.get())*350
    daalprice=int(daalEntry.get())*80
    wheatprice=int(wheatEntry.get())*655
    sugarprice=int(sugarEntry.get())*90
    teaprice=int(teaEntry.get())*32

    totalgroceryprice=riceprice+oilprice+daalprice+wheatprice+sugarprice+teaprice

    groceryPriceEntry.delete(0,END)
    groceryPriceEntry.insert(0,f'{totalgroceryprice} Rs')

    grocerytax=totalgroceryprice*0.05

    groceryTaxEntry.delete(0,END)
    groceryTaxEntry.insert(0,f'{grocerytax} Rs')

    #cold drinks calculation 
    global maazaprice,pepsiprice,spriteprice,dewprice,frootiprice,cocacolaprice,drinkstax,totalbill
    maazaprice=int(maazaEntry.get())*25
    pepsiprice=int(pepsiEntry.get())*50
    spriteprice=int(spriteEntry.get())*55
    dewprice=int(dewEntry.get())*70
    frootiprice=int(frootiEntry.get())*45
    cocacolaprice=int(cocaColaEntry.get())*70

    totaldrinksprice=maazaprice+pepsiprice+spriteprice+dewprice+frootiprice+cocacolaprice

    drinksPriceEntry.delete(0,END)
    drinksPriceEntry.insert(0,f'{totaldrinksprice} Rs')

    drinkstax=totaldrinksprice*0.08

    drinksTaxEntry.delete(0,END)
    drinksTaxEntry.insert(0,f'{drinkstax} Rs')

    totalbill=0
    totalbill=totalcosmeticprice+totaldrinksprice+totalgroceryprice

if not os.path.exists('bills'):
    os.mkdir('bills')

def save_bill():
    global billNumber
    result=messagebox.askyesno('Confirm','Do you want to save the bill?')
    if result:
        bill_content=textArea.get(1.0,END)
        file=open(f'bills/{billNumber}.txt','w')
        file.write(bill_content)
        file.close()
        messagebox.showinfo('Success',f'Bill Number {billNumber} saved successfully')
        billNumber = random.randint(100,10000)

billNumber = random.randint(100,10000)

def bill_area():
    if nameEntry.get()=='' or phoneEntry.get()=='':
        messagebox.showerror('Error','Customers Details Area is Required')
    elif cosmeticsPriceEntry.get()=='' and groceryPriceEntry.get()=='' and drinksPriceEntry.get() == '':
        messagebox.showerror('Error','No Products are selected')
    elif cosmeticsPriceEntry.get()=='0 Rs' and groceryPriceEntry.get()=='0 Rs' and drinksPriceEntry.get()=='0 Rs':
        messagebox.showerror('Error','No Products are selectd')
    else:
        textArea.delete(1.0,END)
        textArea.insert(END,'\t\t     ** Welcome Customer **\n')
        textArea.insert(END,f'\n Bill Number: {billNumber}')
        textArea.insert(END,f'\n Customer Name: {nameEntry.get()}')
        textArea.insert(END,f'\n Phone Number: {phoneEntry.get()}')
        textArea.insert(END,'\n===========================================================')
        textArea.insert(END,'\n  Product\t\t\tQuantity\t\t\tPrice')
        textArea.insert(END,'\n===========================================================')
        if bathSoapEntry.get()!='0':
            textArea.insert(END,f'  Bath Soap\t\t\t {bathSoapEntry.get()}\t\t\t{soapprice} Rs')
        if faceCreamEntry.get()!='0':
            textArea.insert(END,f'\n  Face Cream\t\t\t {faceCreamEntry.get()}\t\t\t{facecreamprice} Rs')
        if faceWashEntry.get()!='0':
            textArea.insert(END,f'\n  Face Wash\t\t\t {faceWashEntry.get()}\t\t\t{facewashprice} Rs')
        if hairSprayEntry.get()!='0':
            textArea.insert(END,f'\n  Hair Spray\t\t\t {hairSprayEntry.get()}\t\t\t{hairsparayprice} Rs')
        if hairGelEntry.get()!='0':
            textArea.insert(END,f'\n  Hair Gel\t\t\t {hairGelEntry.get()}\t\t\t{hairgelprice} Rs')
        if bodyLotionEntry.get()!='0':
            textArea.insert(END,f'\n  Body Lotion\t\t\t {bodyLotionEntry.get()}\t\t\t{bodylotionprice} Rs')
        if riceEntry.get()!='0':
            textArea.insert(END,f'\n  Rice\t\t\t {riceEntry.get()}\t\t\t{riceprice} Rs')
        if oilEntry.get()!='0':
            textArea.insert(END,f'\n  Oil\t\t\t {oilEntry.get()}\t\t\t{oilprice} Rs')
        if daalEntry.get()!='0':
            textArea.insert(END,f'\n  Daal\t\t\t {daalEntry.get()}\t\t\t{daalprice} Rs')
        if wheatEntry.get()!='0':
            textArea.insert(END,f'\n  Wheat\t\t\t {wheatEntry.get()}\t\t\t{wheatprice} Rs')
        if sugarEntry.get()!='0':
            textArea.insert(END,f'\n  Sugar\t\t\t {sugarEntry.get()}\t\t\t{sugarprice} Rs')
        if teaEntry.get()!='0':
            textArea.insert(END,f'\n  Tea\t\t\t {teaEntry.get()}\t\t\t{teaprice} Rs')
        if maazaEntry.get()!='0':
            textArea.insert(END,f'\n  Maaza\t\t\t {maazaEntry.get()}\t\t\t{maazaprice} Rs')
        if pepsiEntry.get()!='0':
            textArea.insert(END,f'\n  Pepsi\t\t\t {pepsiEntry.get()}\t\t\t{pepsiprice} Rs')
        if spriteEntry.get()!='0':
            textArea.insert(END,f'\n  Sprite\t\t\t {spriteEntry.get()}\t\t\t{spriteprice} Rs')
        if dewEntry.get()!='0':
            textArea.insert(END,f'\n  Dew\t\t\t {dewEntry.get()}\t\t\t{dewprice} Rs')
        if frootiEntry.get()!='0':
            textArea.insert(END,f'\n  Frooti\t\t\t {frootiEntry.get()}\t\t\t{frootiprice} Rs')
        if cocaColaEntry.get()!='0':
            textArea.insert(END,f'\n  CocaCola\t\t\t {cocaColaEntry.get()}\t\t\t{cocacolaprice} Rs')
        textArea.insert(END,'\n-----------------------------------------------------------')
        
        if cosmeticsTaxEntry.get()!='0.0 Rs' and cosmeticsTaxEntry.get()!='':
            textArea.insert(END,f'\n Cosmetics Tax: \t\t\t\t\t\t{cosmeticsTaxEntry.get()}')
        if groceryTaxEntry.get()!='0.0 Rs' and groceryTaxEntry.get()!='':
            textArea.insert(END,f'\n Grocery Tax: \t\t\t\t\t\t{groceryTaxEntry.get()}')
        if drinksTaxEntry.get()!='0.0 Rs' and drinksTaxEntry.get()!='':
            textArea.insert(END,f'\n Drinks Tax: \t\t\t\t\t\t{drinksTaxEntry.get()}')

        if totalbill !=0:
            textArea.insert(END,f'\n\n Total Bill: \t\t\t\t\t\t{totalbill} Rs')

        textArea.insert(END,'\n-----------------------------------------------------------')

        save_bill()

#GUI part
root = Tk()
root.title('Khaata Nama')
root.geometry("1920x1080")  # widthxheight
root.iconbitmap('icon.ico')

# Heading Label
headingLabel = Label(
    root,
    text='Khaata Nama',
    font=('montserrat', 30, 'bold'),
    bg='gray20',  
    fg='gold',  
    bd=12,
    relief=GROOVE
)
headingLabel.pack(fill=X)  # Full width with spacing

# Customer Details Frame
customer_Details_Frame = LabelFrame(
    root,
    text='Customer Details',
    font=('montserrat', 15, 'bold'),
    bg='gray20',
    fg='gold',
    bd=8,
    relief=GROOVE
)
customer_Details_Frame.pack(fill=X,pady=10)

nameLabel = Label(
    customer_Details_Frame,
    text='Name',
    font=('montserrat', 15, 'bold'),
    bg='gray20',
    fg='#ffffff'
)

nameLabel.grid(row=0,column=0,padx=20)

nameEntry = Entry(
    customer_Details_Frame,
    font=('montserrat', 15),
    bd=7,
    width=20
    
)

nameEntry.grid(row=0,column=1,padx=25)

phoneLabel = Label(
    customer_Details_Frame,
    text='Phone Number',
    font=('montserrat', 15, 'bold'),
    bg='gray20',
    fg='#ffffff'
)

phoneLabel.grid(row=0,column=2,padx=20)

phoneEntry = Entry(
    customer_Details_Frame,
    font=('montserrat', 15),
    bd=7,
    width=20
    
)

phoneEntry.grid(row=0,column=3,padx=25)



billNoLabel = Label(
    customer_Details_Frame,
    text='Bill Number',
    font=('montserrat', 15, 'bold'),
    bg='gray20',
    fg='#ffffff'
)

billNoLabel.grid(row=0,column=4,padx=20)

billNoEntry = Entry(
    customer_Details_Frame,
    font=('montserrat', 15),
    bd=7,
    width=20
    
)

billNoEntry.grid(row=0,column=5,padx=25)

searchButton = Button(
    customer_Details_Frame,
    text='Search',
    font=('montserrat', 12, 'bold'),
    bd=7,
    width=10,
    command=search_bill
)

searchButton.grid(row=0, column=6,padx=70,pady=8)

productsFrame = Frame(
    root
)

productsFrame.pack(fill=X)

cosmeticsLabelFrame = LabelFrame(
    productsFrame,
    text='Cosmetics',
    font=('montserrat', 15, 'bold'),
    bg='gray20',
    fg='gold',
    bd=8,
    relief=GROOVE,
    padx=25,
    pady=25
)


cosmeticsLabelFrame.grid(row=0,column=0)

bathSoap = Label(
    cosmeticsLabelFrame,
    text='Bath Soap',
    font=('montserrat', 15, 'bold'),
    bg='gray20',
    fg='white',
)

bathSoap.grid(row=0,column=0,pady=11,padx=12,sticky='W')

bathSoapEntry = Entry(
    cosmeticsLabelFrame,
    font=('montserrat', 15),
    width=10,
    bd=5
)

bathSoapEntry.grid(row=0,column=1,pady=11,padx=12)
bathSoapEntry.insert(0,0)


faceCream = Label(
    cosmeticsLabelFrame,
    text='Face Cream',
    font=('montserrat', 15, 'bold'),
    bg='gray20',
    fg='white',
)

faceCream.grid(row=1,column=0,pady=11,padx=12,sticky='W')

faceCreamEntry = Entry(
    cosmeticsLabelFrame,
    font=('montserrat', 15),
    width=10,
    bd=5
)

faceCreamEntry.grid(row=1,column=1,pady=11,padx=12)
faceCreamEntry.insert(0,0)

faceWash = Label(
    cosmeticsLabelFrame,
    text='Face Wash',
    font=('montserrat', 15, 'bold'),
    bg='gray20',
    fg='white',
)

faceWash.grid(row=2,column=0,pady=11,padx=12,sticky='W')

faceWashEntry = Entry(
    cosmeticsLabelFrame,
    font=('montserrat', 15),
    width=10,
    bd=5
)

faceWashEntry.grid(row=2,column=1,pady=11,padx=12)
faceWashEntry.insert(0,0)


hairSpray = Label(
    cosmeticsLabelFrame,
    text='Hair Spray',
    font=('montserrat', 15, 'bold'),
    bg='gray20',
    fg='white',
)

hairSpray.grid(row=3,column=0,pady=11,padx=12,sticky='W')

hairSprayEntry = Entry(
    cosmeticsLabelFrame,
    font=('montserrat', 15),
    width=10,
    bd=5
)

hairSprayEntry.grid(row=3,column=1,pady=11,padx=12)
hairSprayEntry.insert(0,0)


hairGel = Label(
    cosmeticsLabelFrame,
    text='Hair Gel',
    font=('montserrat', 15, 'bold'),
    bg='gray20',
    fg='white',
)

hairGel.grid(row=4,column=0,pady=11,padx=12,sticky='W')

hairGelEntry = Entry(
    cosmeticsLabelFrame,
    font=('montserrat', 15),
    width=10,
    bd=5
)

hairGelEntry.grid(row=4,column=1,pady=11,padx=12)
hairGelEntry.insert(0,0)

bodyLotion = Label(
    cosmeticsLabelFrame,
    text='Body Lotion',
    font=('montserrat', 15, 'bold'),
    bg='gray20',
    fg='white',
)

bodyLotion.grid(row=5,column=0,pady=11,padx=12,sticky='W')

bodyLotionEntry = Entry(
    cosmeticsLabelFrame,
    font=('montserrat', 15),
    width=10,
    bd=5
)

bodyLotionEntry.grid(row=5,column=1,pady=11,padx=12)
bodyLotionEntry.insert(0,0)

groceryFrame = LabelFrame(
    productsFrame,
    text='Grocery',
    font=('montserrat', 15, 'bold'),
    bg='gray20',
    fg='gold',
    bd=8,
    relief=GROOVE,
    padx=25,
    pady=25
)

groceryFrame.grid(row=0,column=1,padx=10)

rice = Label(
    groceryFrame,
    text='Rice',
    font=('montserrat', 15, 'bold'),
    bg='gray20',
    fg='white',
)

rice.grid(row=0,column=0,pady=11,padx=12,sticky='W')

riceEntry = Entry(
    groceryFrame,
    font=('montserrat', 15),
    width=10,
    bd=5
)

riceEntry.grid(row=0,column=1,padx=12,pady=11)
riceEntry.insert(0,0)

oil = Label(
    groceryFrame,
    text='Oil',
    font=('montserrat', 15, 'bold'),
    bg='gray20',
    fg='white',
)

oil.grid(row=1,column=0,pady=11,padx=12,sticky='W')

oilEntry = Entry(
    groceryFrame,
    font=('montserrat', 15),
    width=10,
    bd=5
)

oilEntry.grid(row=1,column=1,padx=12,pady=11)
oilEntry.insert(0,0)

daal = Label(
    groceryFrame,
    text='Daal',
    font=('montserrat', 15, 'bold'),
    bg='gray20',
    fg='white',
)

daal.grid(row=2,column=0,pady=11,padx=12,sticky='W')

daalEntry = Entry(
    groceryFrame,
    font=('montserrat', 15),
    width=10,
    bd=5
)

daalEntry.grid(row=2,column=1,padx=12,pady=11)
daalEntry.insert(0,0)

wheat = Label(
    groceryFrame,
    text='Wheat',
    font=('montserrat', 15, 'bold'),
    bg='gray20',
    fg='white',
)

wheat.grid(row=3,column=0,pady=11,padx=12,sticky='W')

wheatEntry = Entry(
    groceryFrame,
    font=('montserrat', 15),
    width=10,
    bd=5
)

wheatEntry.grid(row=3,column=1,padx=12,pady=11)
wheatEntry.insert(0,0)

sugar = Label(
    groceryFrame,
    text='Sugar',
    font=('montserrat', 15, 'bold'),
    bg='gray20',
    fg='white',
)

sugar.grid(row=4,column=0,pady=11,padx=12,sticky='W')

sugarEntry = Entry(
    groceryFrame,
    font=('montserrat', 15),
    width=10,
    bd=5
)

sugarEntry.grid(row=4,column=1,padx=12,pady=11)
sugarEntry.insert(0,0)

tea = Label(
    groceryFrame,
    text='Tea',
    font=('montserrat', 15, 'bold'),
    bg='gray20',
    fg='white',
)

tea.grid(row=5,column=0,pady=11,padx=12,sticky='W')

teaEntry = Entry(
    groceryFrame,
    font=('montserrat', 15),
    width=10,
    bd=5
)

teaEntry.grid(row=5,column=1,padx=12,pady=11)
teaEntry.insert(0,0)

drinksFrame = LabelFrame(
    productsFrame,
    text='Cold Drinks',
    font=('montderrat',15,'bold'),
    bg='gray20',
    fg='gold',
    bd=8,
    relief=GROOVE,
    padx=25,
    pady=25
)
drinksFrame.grid(row=0,column=2)

maaza = Label(
    drinksFrame,
    text='Maaza',
    font=('montserrat', 15, 'bold'),
    bg='gray20',
    fg='white',
)

maaza.grid(row=0,column=0,pady=11,padx=12,sticky='W')

maazaEntry = Entry(
    drinksFrame,
    font=('montserrat', 15),
    width=10,
    bd=5
)

maazaEntry.grid(row=0,column=1,padx=12,pady=11)
maazaEntry.insert(0,0)

pepsi = Label(
    drinksFrame,
    text='Pepsi',
    font=('montserrat', 15, 'bold'),
    bg='gray20',
    fg='white',
)

pepsi.grid(row=1,column=0,pady=11,padx=12,sticky='W')

pepsiEntry = Entry(
    drinksFrame,
    font=('montserrat', 15),
    width=10,
    bd=5
)

pepsiEntry.grid(row=1,column=1,padx=12,pady=11)
pepsiEntry.insert(0,0)


sprite = Label(
    drinksFrame,
    text='Sprite',
    font=('montserrat', 15, 'bold'),
    bg='gray20',
    fg='white',
)

sprite.grid(row=2,column=0,pady=11,padx=12,sticky='W')

spriteEntry = Entry(
    drinksFrame,
    font=('montserrat', 15),
    width=10,
    bd=5
)

spriteEntry.grid(row=2,column=1,padx=12,pady=11)
spriteEntry.insert(0,0)


dew = Label(
    drinksFrame,
    text='Dew',
    font=('montserrat', 15, 'bold'),
    bg='gray20',
    fg='white',
)

dew.grid(row=3,column=0,pady=11,padx=12,sticky='W')

dewEntry = Entry(
    drinksFrame,
    font=('montserrat', 15),
    width=10,
    bd=5
)

dewEntry.grid(row=3,column=1,padx=12,pady=11)
dewEntry.insert(0,0)

frooti = Label(
    drinksFrame,
    text='Frooti',
    font=('montserrat', 15, 'bold'),
    bg='gray20',
    fg='white',
)

frooti.grid(row=4,column=0,pady=11,padx=12,sticky='W')

frootiEntry = Entry(
    drinksFrame,
    font=('montserrat', 15),
    width=10,
    bd=5
)

frootiEntry.grid(row=4,column=1,padx=12,pady=11)
frootiEntry.insert(0,0)


cocaCola = Label(
    drinksFrame,
    text='Coca Cola',
    font=('montserrat', 15, 'bold'),
    bg='gray20',
    fg='white',
)

cocaCola.grid(row=5,column=0,pady=11,padx=12,sticky='W')

cocaColaEntry = Entry(
    drinksFrame,
    font=('montserrat', 15),
    width=10,
    bd=5
)

cocaColaEntry.grid(row=5,column=1,padx=12,pady=11)
cocaColaEntry.insert(0,0)

billFrame = Frame(
    productsFrame,
    bd=8,
    relief=GROOVE
)

billFrame.grid(row=0,column=3,padx=10)


billAreaLabel =Label(
    billFrame,
    text='Bill Area',
    font=('montserrat', 15, 'bold'),
    bd=7,
    relief=GROOVE

)

billAreaLabel.pack(fill=X)

scrollbar = Scrollbar(
    billFrame,
    orient=VERTICAL
)

scrollbar.pack(side=RIGHT,fill=Y)

textArea = Text(
    billFrame,
    height=23,
    width=59,
    yscrollcommand=scrollbar.set
)
textArea.pack()
scrollbar.config(command=textArea.yview)


billMenuFrame = LabelFrame(
    root,
    text='Bill Menu',
    font=('montserrat', 15, 'bold'),
    bd=8,
    relief=GROOVE,
    bg='gray20',
    fg='gold'
)

billMenuFrame.pack(fill=X,pady=10)


cosmeticsPrice = Label(
    billMenuFrame,
    text='Cosmetic Price',
    font=('montserrat', 15, 'bold'),
    bg='gray20',
    fg='white',
)

cosmeticsPrice.grid(row=0,column=0,pady=11,padx=12,sticky='W')

cosmeticsPriceEntry = Entry(
    billMenuFrame,
    font=('montserrat', 15),
    width=10,
    bd=5
)

cosmeticsPriceEntry.grid(row=0,column=1,padx=12,pady=11)


groceryPrice = Label(
    billMenuFrame,
    text='Grocery Price',
    font=('montserrat', 15, 'bold'),
    bg='gray20',
    fg='white',
)

groceryPrice.grid(row=1,column=0,pady=11,padx=12,sticky='W')

groceryPriceEntry = Entry(
    billMenuFrame,
    font=('montserrat', 15),
    width=10,
    bd=5
)

groceryPriceEntry.grid(row=1,column=1,padx=12,pady=11)


drinksPrice = Label(
    billMenuFrame,
    text='Drinks Price',
    font=('montserrat', 15, 'bold'),
    bg='gray20',
    fg='white',
)

drinksPrice.grid(row=2,column=0,pady=11,padx=12,sticky='W')

drinksPriceEntry = Entry(
    billMenuFrame,
    font=('montserrat', 15),
    width=10,
    bd=5
)

drinksPriceEntry.grid(row=2,column=1,padx=12,pady=11)

#tax section
cosmeticsTax = Label(
    billMenuFrame,
    text='Cosmetic Tax',
    font=('montserrat', 15, 'bold'),
    bg='gray20',
    fg='white',
)

cosmeticsTax.grid(row=0,column=2,pady=11,padx=12,sticky='W')

cosmeticsTaxEntry = Entry(
    billMenuFrame,
    font=('montserrat', 15),
    width=10,
    bd=5
)

cosmeticsTaxEntry.grid(row=0,column=3,padx=12,pady=11)


groceryTax = Label(
    billMenuFrame,
    text='Grocery Tax',
    font=('montserrat', 15, 'bold'),
    bg='gray20',
    fg='white',
)

groceryTax.grid(row=1,column=2,pady=11,padx=12,sticky='W')

groceryTaxEntry = Entry(
    billMenuFrame,
    font=('montserrat', 15),
    width=10,
    bd=5
)

groceryTaxEntry.grid(row=1,column=3,padx=12,pady=11)


drinksTax = Label(
    billMenuFrame,
    text='Drinks Tax',
    font=('montserrat', 15, 'bold'),
    bg='gray20',
    fg='white',
)

drinksTax.grid(row=2,column=2,pady=11,padx=12,sticky='W')

drinksTaxEntry = Entry(
    billMenuFrame,
    font=('montserrat', 15),
    width=10,
    bd=5
)

drinksTaxEntry.grid(row=2,column=3,padx=12,pady=11)

buttonFrame = Frame(
    billMenuFrame,
    bd=8,
    relief=GROOVE,
)
buttonFrame.grid(row=0,column=4,rowspan=3)

totalButton = Button(
    buttonFrame,
    text='Total',
    font=('montserrat', 15, 'bold'),
    bg='gray20',
    fg='white',
    bd=5,
    width=11,
    pady=19,
    command=total

)
totalButton.grid(row=0,column=0,pady=25,padx=10)


billButton = Button(
    buttonFrame,
    text='Bill',
    font=('montserrat', 15, 'bold'),
    bg='gray20',
    fg='white',
    bd=5,
    width=11,
    pady=19,
    command=bill_area

)
billButton.grid(row=0,column=1,pady=25,padx=10)

emailButton = Button(
    buttonFrame,
    text='Email',
    font=('montserrat', 15, 'bold'),
    bg='gray20',
    fg='white',
    bd=5,
    width=11,
    pady=19,
    command=send_email

)
emailButton.grid(row=0,column=2,pady=25,padx=10)

printButton = Button(
    buttonFrame,
    text='Print',
    font=('montserrat', 15, 'bold'),
    bg='gray20',
    fg='white',
    bd=5,
    width=11,
    pady=19,
    command=print_bill 

)
printButton.grid(row=0,column=3,pady=25,padx=10)

clearButton = Button(
    buttonFrame,
    text='Clear',
    font=('montserrat', 15, 'bold'),
    bg='gray20',
    fg='white',
    bd=5,
    width=11,
    pady=19,
    command=clear

)
clearButton.grid(row=0,column=4,pady=25,padx=10)
root.mainloop()