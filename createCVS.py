import csv 
# field names 
fields = ['BGelectroniks',  'bgel_price','maxshop_price','maxshop_dif'] 
    

# name of csv file 
filename = "doc.csv"
    
# writing to csv file 
with open(filename, 'w') as csvfile: 
    # creating a csv writer object 
    csvwriter = csv.writer(csvfile) 
        
    # writing the fields 
    csvwriter.writerow(fields) 
        

