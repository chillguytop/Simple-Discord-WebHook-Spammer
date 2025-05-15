"""
Credits: Webhook spammer made by andy
Discord: !ANDY!#0001
Github: AndyOnTop
"""
print("""
                                                                                            kkkkkkkk                                                
                                                                                            k::::::k                                                
                                                                                            k::::::k                                                
                                                                                            k::::::k                                                
zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz     nnnn  nnnnnnnn    uuuuuu    uuuuuu   k:::::k    kkkkkkk eeeeeeeeeeee    rrrrr   rrrrrrrrr   
z:::::::::::::::zz:::::::::::::::zz:::::::::::::::z     n:::nn::::::::nn  u::::u    u::::u   k:::::k   k:::::kee::::::::::::ee  r::::rrr:::::::::r  
z::::::::::::::z z::::::::::::::z z::::::::::::::z      n::::::::::::::nn u::::u    u::::u   k:::::k  k:::::ke::::::eeeee:::::eer:::::::::::::::::r 
zzzzzzzz::::::z  zzzzzzzz::::::z  zzzzzzzz::::::z       nn:::::::::::::::nu::::u    u::::u   k:::::k k:::::ke::::::e     e:::::err::::::rrrrr::::::r
      z::::::z         z::::::z         z::::::z          n:::::nnnn:::::nu::::u    u::::u   k::::::k:::::k e:::::::eeeee::::::e r:::::r     r:::::r
     z::::::z         z::::::z         z::::::z           n::::n    n::::nu::::u    u::::u   k:::::::::::k  e:::::::::::::::::e  r:::::r     rrrrrrr
    z::::::z         z::::::z         z::::::z            n::::n    n::::nu::::u    u::::u   k:::::::::::k  e::::::eeeeeeeeeee   r:::::r            
   z::::::z         z::::::z         z::::::z             n::::n    n::::nu:::::uuuu:::::u   k::::::k:::::k e:::::::e            r:::::r            
  z::::::zzzzzzzz  z::::::zzzzzzzz  z::::::zzzzzzzz       n::::n    n::::nu:::::::::::::::uuk::::::k k:::::ke::::::::e           r:::::r            
 z::::::::::::::z z::::::::::::::z z::::::::::::::z       n::::n    n::::n u:::::::::::::::uk::::::k  k:::::ke::::::::eeeeeeee   r:::::r            
z:::::::::::::::zz:::::::::::::::zz:::::::::::::::z       n::::n    n::::n  uu::::::::uu:::uk::::::k   k:::::kee:::::::::::::e   r:::::r            
zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz       nnnnnn    nnnnnn    uuuuuuuu  uuuukkkkkkkk    kkkkkkk eeeeeeeeeeeeee   rrrrrrr            

""")

#imports
from dhooks import Webhook
import time

#prompts
message = input("What do you want to spam?: ")
webhookurl = Webhook(input("Enter webhook: "))
delay = int(input("Enter a delay: "))

#webhook spamming time
while True:
    time.sleep(delay)
    webhookurl.send(message)
    print("Sent.")
