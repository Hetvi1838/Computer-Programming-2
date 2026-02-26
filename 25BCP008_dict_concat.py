def dict_concat():
    dict1={"Diya":48, "Hetvi":8}
    dict2={"Kavya":27, "Veli":31}
    dict3={"Vraj":1, "Kush":277}
    #dict4={**dict1, **dict2, **dict3}
    dict4=dict1|dict2|dict3
    print(dict4)
dict_concat()
