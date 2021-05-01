capitals = {"India":"Delhi","USA":"SAN","France":"Paris"}

for capital in capitals.items():
    print("The capital and country is {}".format(capital))

print("\n")

for country,capital in capitals.items():
    print("The capital of {} is {}".format(country,capital))
