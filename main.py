from test import number
import phonenumbers
from phonenumbers import  geocoder
ch_number=phonenumbers.parse(number,"CCH")
print(geocoder.description_for_number(ch_number,"en"))

#Now we find the Service Provider of the Number
from  phonenumbers import carrier
servicE_provider=phonenumbers.parse(number,"RO")
print(carrier.name_for_number(servicE_provider,"en"))