import pyjokes
import time

a = pyjokes.get_joke()
for i in list(a):
    print(i, end="", flush=True)
    time.sleep(.1)
    
print()
print ("Made by Ro706")
print ("(★_★)")

