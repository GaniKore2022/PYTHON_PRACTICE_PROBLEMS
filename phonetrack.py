import phonenumbers
from phonenumbers import geocoder
p1=phonenumbers.parse("+917995266314")
print(geocoder.description_for_number(p1,"en"))
