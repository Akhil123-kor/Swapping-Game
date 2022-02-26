def swap():
    file1=input("Enter the file name")
    file2=input("Enter the second file's name")

    with open(file1, 'r') as a:
        data_a=a.read()

    
    with open(file2, 'r') as b:
        data_b=b.read()

    with open(file1, 'w') as c:
        c.write(data_b)

    with open(file2, 'w') as d:
        d.write(data_a)

swap()