from add import add
from add import add_noretry


#for i in range(0,5):
#    add.delay(0,i)


#add.delay(0,3)
add_noretry.delay(1,3)
#add.apply_async(args=[0,3])
