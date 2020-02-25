def function_elements_in_lists(L1,L2):
    L3=[]
    for i in L1:
        if i in L2:
            L3.append(i)
    print(L3)

List1=[1,2,3,4]
List2=[1,5,3,7]
function_elements_in_lists(List1,List2)