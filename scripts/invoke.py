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
  

def main():
    store_favorite_number()
    read_favorite_number()