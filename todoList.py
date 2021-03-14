#  start the list 

#  add to the list
#  determine priority of the list item

#  view the list

#  delete the items on the list

#  stop the list
from itertools import islice


aList = {}

def message():
    print('welcome to the todo list')

message()

def addItem ():
    print('please add your item\n')
    newItem = input(str(''))
    priority = input('please select the level of priority(low, medium, high\n')
    newItemlen = len(newItem)
    
    while newItemlen < 3:
        print('please add a valid number of characters for your item (3)\n')
        priority = input('please select the level of priority(low, medium, high\n')
        newItemlen = len(newItem)
    if newItemlen >= 3:
        aList[newItem] = priority
        print('this whas just added' + newItem + 'and its priority level' + priority + '\n')
        print(aList)
        

        
def viewItem():
    print(aList)
    # print(aList[1])
    # i = aList.index(i)
    # print(i)


def delItem():
    print(aList)
    i = 0
    for list in aList:
        i = i + 1
        print(i, list)
    print('Select (#) to delete from list. Press (b) to return to menu')
    deletedItem = input(str(''))
    if deletedItem == 'b':
        message()
    if deletedItem == '1':
        del aList[next(iter(aList))]
        print(aList)
    if deletedItem == '2':
        del aList[next(islice(aList, 1, None))]
        print(aList)
    if deletedItem == '3':
        del aList[next(islice(aList, 2, None))]
        print(aList)
    if deletedItem == '4':
        del aList[next(islice(aList, 3, None))]
        print(aList)
    if deletedItem == '5':
        del aList[next(islice(aList, 4, None))]
        print(aList)
       







while True:
    choice = input([
         '1: Add item to list',
         
         '2: View items on list',
         
         '3: Delete items from list'
    ])
    if choice == 'q':
        print('exiting')
        break
            
    else:
        message()

    if choice == '1':
        addItem()
   
    if choice == '2':
        viewItem()

    if choice == '3':
        delItem()
   
   