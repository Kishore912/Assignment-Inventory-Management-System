glob = {
    
"product_id_list" : [1,2,3,4],
"product_name_list" : [5,6,7,8],
"category_list" : [9,10,11,12],
"price_list" : [13,14,15,16],
"quantity_list" : [17,18,19,20],
}

for i in glob.values():
    for j in i:
        print(j)