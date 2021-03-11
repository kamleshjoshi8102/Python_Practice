import random     #Importing Random Library to generate Random Integers 

inp='y'

while inp=='y':

     di=random.randint(1,6)         #Generated Random Integers Among Range of (1 - 6) 

     if di==1:
          print("[-----]")
          print("[     ]")
          print("[  0  ]")
          print("[     ]")
          print("[-----]")
     if di==2:
          print("[-----]")
          print("[ 0   ]")
          print("[     ]")
          print("[   0 ]")
          print("[-----]")
     if di==3:
          print("[-----]")
          print("[     ]")
          print("[0 0 0]")
          print("[     ]")
          print("[-----]")

     if di==4:
          print("[-----]")
          print("[0   0]")
          print("[     ]")
          print("[0   0]")
          print("[-----]")
     if di == 5:
          print("[-----]")
          print("[0   0]")
          print("[  0  ]")
          print("[0   0]")
          print("[-----]")
     if di == 6:
          print("[-----]")
          print("[0 0 0]")
          print("[     ]")
          print("[0 0 0]")
          print("[-----]")
     inp=input("Press y to Continue else Press Any Button to EXIT \n")    #Will Exit when Any other Input Is Given Except y
