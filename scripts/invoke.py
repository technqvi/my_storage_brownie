from re import X
from brownie import SimpleStorage,accounts,config
import scripts.deploy as xdeploy

def read_favorite_number():
   xcontact=  SimpleStorage[-1]
   print(xcontact.retrieve())

def store_favorite_number():
   xcontact=  SimpleStorage[-1]
   tx=  xcontact.store(1,{"from":xdeploy.get_account()})
   tx.wait(1)
   print("store value successfully")
  
def add_lucky_number_of_person(key_name:str,lucky_numer:int):
   xcontract=SimpleStorage[-1]
   tx=xcontract.addPerson(key_name,lucky_numer,{"from":xdeploy.get_account()})
   tx.wait(1)
   print("add person and his number successfully")

def list_favoriteNumber_of_people():
   xcontract=SimpleStorage[-1]
   list_people=xcontract.people()
   for i in range(len(list_people)):
     print(f"{list_people(i)(0)} of {list_people(i)[1]}")
     #print(xcontract.people(0)[0])

   
def get_favoriteNumber_by_name(key_name):
   xcontract=SimpleStorage[-1]
   my_number=xcontract.nameToFavoriteNumber(key_name)
   print(my_number)


def main():
 xcontract=SimpleStorage[-1]
 print(xcontract.people(0))

   #  store_favorite_number()
   #  read_favorite_number()

  # trong-pongthorn ,noie-phiranun
  # add_lucky_number_of_person("noie-phiranun",50)
  # get_favoriteNumber_by_name("noie-phiranun")
  #list_favoriteNumber_of_people
# list_favoriteNumber_of_people()
# xcontract=SimpleStorage[-1]
 #print(xcontract.people(0))
 #print(xcontract.people(1))
#   print(xcontract.people(0)[0])
#   print(xcontract.people(0)[1])

   # xcontract=SimpleStorage[-1]
   # list_people=xcontract.people()
   # for i in range(len(list_people)):
   #   print(f"{list_people(i)(0)} of {list_people(i)[1]}")