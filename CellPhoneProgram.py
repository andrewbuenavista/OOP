import CellPhoneClass as c

def main():

    phone = c.CellPhone("Apple","iPhone 13", "$500")

    
    phone.set_manufact("Samsung")
    phone.set_model("Note 9")
    phone.set_retail_price("$800")
    
    print(phone.get_manufact())
    print(phone.get_model())
    print(phone.get_retail_price())

main()