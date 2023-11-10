def line_file (files):
    line_list1= []
    file = open(files,'r',encoding='utf-8')
    while True:
        line = file.readline()
        if line:
            line_list1.append(line.strip())
        elif not line:
            break
    return line_list1
def dict_files(n):
    line_dict = {}
    len_list =[]
    files_dict = {}
    for i in range(1,n+1):
        len_line = str(len(line_file(f"{i}.txt")))
        line_list = line_file(f"{i}.txt")
        line_dict[len_line]= line_list
        len_list.append(len_line)
        files_dict[len_line] = f"{i}.txt"
    sorted_line_list = sorted(len_list)
    return line_dict, sorted_line_list,files_dict
def write_file(file):
    with open(f'{file}.txt','w',encoding='utf-8' ) as f:
        line_dict,sorted_line_list,files_dict = dict_files(3)
        for len_line in sorted_line_list:
            if len_line in line_dict and len_line in files_dict:
                f.write(files_dict[len_line])
                f.write('\n')
                f.write(len_line)
                f.write('\n')
                for line in line_dict[len_line]:
                    f.write(line)
                    f.write('\n')
    
write_file('resalt')