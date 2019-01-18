def print_lol(the_list):
    for each_item in the_list:
        if isinstance(each_item,list):
            print_lol(each_item)
        else:
            print(each_item)
movies=["the holy grail",1975,"the jones",91,["graham chapman",["michael palin","john cleese","terry gilliam","eric idle","terry jones"]]]
print_lol(movies)
