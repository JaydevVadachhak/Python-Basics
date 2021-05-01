def checkmoney(amount):
    if amount<7000  :
        print("Ahem, can you rethink this number please?")
    elif amount>10000:
        print("Wow sis! You are a queen")
    else:
        print("Cool, thanks sis! {} rupees will certainly help.".format(amount))

    return

sis=8500
checkmoney(sis)
