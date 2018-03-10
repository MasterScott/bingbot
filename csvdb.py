import csv
"""def list_maker(file_path):
    with open(file_path, 'r') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        i=-1
        for row in spamreader:
            i=i+1
        with open (file_path,'r') as f:
            reader = csv.reader(f)
            your_list = list(reader)
            total_rows=len(your_list)-1
            data_row=len(your_list)
#your_list[row][column]
"""
def csv_query(file_path,what,columnname,value):
    with open(file_path, 'r') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        i=-1
        for row in spamreader:
            i=i+1
        with open (file_path,'r') as f:
            reader = csv.reader(f)
            your_list = list(reader)
            total_rows=len(your_list)-1
            data_row=len(your_list)
    try:
        columnnumber=your_list[0].index(columnname)
        whatcolumnnumber=your_list[0].index(what)
        row=0
        while row<=i:
           ifs=your_list[row][columnnumber]
           if ifs==value:
               return(your_list[row][whatcolumnnumber])
               break
           row =row+1
    except:
        print("Query error. Result returns None")
        return False
def csv_update(file_path,what,to,columnname,value):
    with open(file_path, 'r') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        i=-1
        for row in spamreader:
            i=i+1
        with open (file_path,'r') as f:
            reader = csv.reader(f)
            your_list = list(reader)
            total_rows=len(your_list)-1
            data_row=len(your_list)
    try:
        columnnumber=your_list[0].index(columnname)
        whatcolumnnumber=your_list[0].index(what)
        row=0
        while row<=total_rows:
            ifs=your_list[row][columnnumber]
            if ifs==value:
                your_list[row][whatcolumnnumber]=to
                break
            row =row+1
        if your_list[row][whatcolumnnumber]=='':
            return error
        counter=0
        datacolumn=len(your_list[0])-1
        while counter<=total_rows:
            counter2=0
            line=""
            while counter2<=datacolumn:
                if counter2==0:
                    line=your_list[counter][counter2]
                else:
                    line=line+","+your_list[counter][counter2]
                counter2=counter2+1
            if counter==0:
                myfile=open(file_path,"w")
                line=line+'\n'
                myfile.write(line)
                myfile.close()
            else:
                myfile=open(file_path,"a")
                line=line+'\n'
                myfile.write(line)
                myfile.close()
            counter=counter+1
        return True
    except:
        print("Unable to update. Result returns None")
        return False
def csv_insert(file_path,lists):
    with open(file_path, 'r') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        i=-1
        for row in spamreader:
            i=i+1
        with open (file_path,'r') as f:
            reader = csv.reader(f)
            your_list = list(reader)
            total_rows=len(your_list)-1
            data_row=len(your_list)
    try:
        datacolumn=len(your_list[0])
        if len(lists)!=datacolumn:
            print("check no of items in list")
            return False
        else:
            line=''
            counter=0
            for i in lists:
                line=line+lists[counter]+","
                counter=counter=1
            myfile=open(file_path,"a")
            myfile.write(line)
            myfile.close()
            return True
    except:
        Print("Unable to insert")
        return False
def csv_drop(file_path):
    with open(file_path, 'r') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        i=-1
        for row in spamreader:
            i=i+1
        with open (file_path,'r') as f:
            reader = csv.reader(f)
            your_list = list(reader)
            total_rows=len(your_list)-1
            data_row=len(your_list)
    try:
        myfile=open(file_path,"w")
        line=''
        myfile.write(line)
        myfile.close()
        return True
    except:
        return False
def csv_row_number(file_path):
    with open(file_path, 'r') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        i=-1
        for row in spamreader:
            i=i+1
        with open (file_path,'r') as f:
            reader = csv.reader(f)
            your_list = list(reader)
            total_rows=len(your_list)-1
            data_row=len(your_list)
    return len(your_list)-1
def csv_column_number(file_path):
    with open(file_path, 'r') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        i=-1
        for row in spamreader:
            i=i+1
        with open (file_path,'r') as f:
            reader = csv.reader(f)
            your_list = list(reader)
            total_rows=len(your_list)-1
            data_row=len(your_list)
    return len(your_list[0])

def csv_total_rows(file_path):
    with open(file_path, 'r') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        i=-1
        for row in spamreader:
            i=i+1
        with open (file_path,'r') as f:
            reader = csv.reader(f)
            your_list = list(reader)
            total_rows=len(your_list)-1
            return total_rows
