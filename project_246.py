from tkinter import *
from web3 import Web3#task1
root = Tk()

root.title("My Ethereum App")
root.geometry("600x200")
root.configure(background="white")

# Setting labels
block_name_label = Label(root, text="Ethereum gas fee in other currencies", font=("Helvetica", 18, 'bold'), bg="white")
block_name_label.place(relx=0.5, rely=0.15, anchor=CENTER)
block_entry = Entry(root, text="This is Entry Widget", bd=2)

block_entry.place(relx=0.5, rely=0.35, anchor=CENTER)
value_in_ether = Label(root, bg="white", font=("bold", 14))
value_in_ether.place(relx=0.5, rely=0.28, anchor=CENTER)
value_in_dollar = Label(root, bg="white", font=("bold", 10))
value_in_dollar.place(relx=0.5, rely=0.48, anchor=CENTER)
value_in_rupees = Label(root, bg="white", font=("bold", 10))
value_in_rupees.place(relx=0.5, rely=0.58, anchor=CENTER)
value_in_pounds = Label(root, bg="white", font=("bold", 10))
value_in_pounds.place(relx=0.5, rely=0.68, anchor=CENTER)


url = 'https://mainnet.infura.io/v3/cded6e6690d04259b05137dd10b170c3'
web3 = Web3(Web3.HTTPProvider(url))
# main function
# Start code for Task 1 below
def ethereum_block():
    wei_price = web3.eth.gas_price()
    gwei_price = wei_price/(10**9)
    gasPriceInEther = (gwei_price/10**9)




    # Start code for Task 2 below
    gasPriceInDollar = gasPriceInEther*3103.69
    gasPriceInRupees = gasPriceInEther*231756.67
    gasPriceInPound = gasPriceInEther*2268.81
    



    # Start code for Task 3 below
   
    value_in_ether['text']= 'Value of gas in ether: eth'+ str(gasPriceInEther)
    value_in_dollar['text']= 'Value of gas in dollar: $'+ str(gasPriceInDollar)
    value_in_rupees['text']= 'Value of gas in rupees: Rs.'+ str(gasPriceInRupees)
    value_in_pounds['text']= 'Value of gas in pound: P'+ str(gasPriceInPound)


   
    search_btn.destroy()


search_btn = Button(root, text="Search currency fee", command=ethereum_block, relief=FLAT)
search_btn.place(relx=0.5, rely=0.48, anchor=CENTER)
root.mainloop()