# create class
class Employee():



       #initializing 
    def __init__(self):
        print('Employee Created')

    #CALLING destructor
    def __del__(self):
        print('Destructor called')

def create_obj():
    print('making object...')
    obj = Employee()
    print('function end...')
    return obj

print('calling create_obj() function...')
obj  = create_obj()
print('Program End...')