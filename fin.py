import phonenumbers
from phonenumbers import carrier, geocoder, timezone

mobileNo = input("Enter Mobile Number with Country Code: ")
mobileNo = phonenumbers.parse(mobileNo)

# get timezone a phone number 
print(timezone.time_zones_for_number(mobileNo))

# getting carrier of a phone number
print(carrier.name_for_number(mobileNo, "en"))

# getting region information 
print(geocoder.description_for_number(mobileNo,"en"))

# Validating a phone number 
print("Valid Mobile Number :", phonenumbers.is_valid_number(mobileNo))

# checking possibility of a number
print("Checking possibility of Number :", phonenumbers.is_possible_number(mobileNo))
