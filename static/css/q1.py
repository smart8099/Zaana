#value = 'ghanatashs8099@ai'
#value2 ='freebuf78andjeep9'

# program to select integers from a string




def select_int(value):
    result = ''.join(filter(str.isdigit,value))
    if result:
        print( result)
    else:
        print(f'there are no integers in the string {value}')    

value_input = input('enter the string to you want to pick integer values from:  ')
select_int(value_input)   