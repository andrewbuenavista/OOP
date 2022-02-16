import InsectClass as i

def main():

    w = int(input("How many wings does your insect have: "))
    l = int(input("How many legs does your insect have: "))

    my_insect = i.Insect(w,l)

    my_insect.set_flight()

    print("My insect has a flight range of:", my_insect.get_flight(), "mile(s)")
    print("My insect has:", my_insect.get_legs(), "legs" )
    print("My insect has:", my_insect.get_wings(), "wings")

main()
