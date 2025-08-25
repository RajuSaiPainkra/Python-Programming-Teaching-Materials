country_name = str(input("Enter Your Country Name : \n"))

print("Ok, Country Name is : ", country_name)

if country_name == "India" or country_name == "INDIA" or country_name == "india":
    print("Welcome Citizen of India")
elif country_name == "USA" or country_name == "usa" or country_name == "Usa":
    print("Welcome Citizen of USA")
elif country_name == "UK" or country_name == "uk" or country_name == "Uk":
    print("Welcome Citizen of UK")
elif country_name == "Nepal" or country_name == "NEPAL" or country_name == "nepal":
    print("Welcome Citizen of Nepal")
elif country_name == "":
    print("Please enter the valid country name ", country_name, end ="")
else:
    print("Welcome Citizen of the World, India Welcomes You!")