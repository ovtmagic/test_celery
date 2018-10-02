from add import add


#for i in range(0,5):
#    add.delay(0,i)


#add.delay(0,3)
add.apply_async(args=[0,3])
