
def menu():
    print('menu')
    print('1:add')
    print('2:delete')
    print('3:view')
    print('4:close')

enter_number='random'
data=[]
while enter_number!='4':
    menu()
    enter_number=input('enter number')
    print('you entered',enter_number)
    if enter_number=='1':
        item=input('enter thing in list')
        data.append(item)
        print('u added ',item,'in list')
    elif enter_number=='2':
        item=input('delete thing in list')
        if item in data:
            data.remove(item)
            print(item,'has deleted')
        else:
            print('its not in list to be deletde')
    elif enter_number=='3':
        for item in data:
            print('all your list:',item)
    elif enter_number=='4':
        print('good bye')  
    else:
        print('chose only 1,2,3,4')     
    

 
