""""This is the "nester.py" module ,and it provides one function called print_lol() 
which prints Lists that may on may not include nested lists"""
def print_mov(the_list,indent=False, level=0):
    """"This function takes a positional argument called the "thelist",which is any python lisy (of,possibly,nested
    lists).Each data item in the provided list is (recursively) printed to the screen on itw own
    line"""
    for each_item in the_list:
        if isinstance (each_item, list):
            print_mov(each_item,indent, level+1)
        else:
            if indent:
              for tab_stop in range(level):
                print("\t",end='')
            print (each_item)



