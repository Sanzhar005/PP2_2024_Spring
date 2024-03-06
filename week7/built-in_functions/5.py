def all_elements_true(tup):
    return all(tup)

tuple1 = (True, True, True)
tuple2 = (True, False, True)
tuple3 = (False, False, False)

print(all_elements_true(tuple1))  
print(all_elements_true(tuple2))  
print(all_elements_true(tuple3))  