def format_name(f_name1, l_name1):
    f_name = f_name1.title()
    l_name = l_name1.title()
    full_name = str(f_name+" "+l_name)
    return full_name

f_name1 = str(input("Enter your first name"))
l_name1 = str(input("Enter your Last name"))

full_name = format_name(f_name1, l_name1)
print(full_name)