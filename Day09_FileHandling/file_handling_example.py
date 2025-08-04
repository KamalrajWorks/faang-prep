try:
    with open("data.txt",'r') as f:
        lines = f.readlines()
        for line in lines:
            name, dept = line.strip().split(",")
            print(f"Name : {name}  Department : {dept}")
except FileNotFoundError:
    with open("data.txt",'w') as f:
        f.write("kamal,Cse\n")
        f.write("v,Cse\n")
        f.write("m,Cse\n")
    with open("data.txt",'r') as f:
        for line in f:
            print(line.strip())
