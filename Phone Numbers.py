import phonenumbers
from phonenumbers import carrier , geocoder ,timezone
mobileNo=input("Mobile number with country code:")
mobileNo=phonenumbers.parse(mobileNo)
print(timezone.time_zone_for_number(mobileNo))
print(geocoder.description_for_number(mobileNo,"en"))
print("Valid Mobile Number:",phonenumbers.is_valid_number(mobileNo))
print("Checking possibility if Number:",phonenumbers.is_possible_number(mobileNo))
