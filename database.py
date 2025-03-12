import csv
class Database:

    def __init__(self,filename,field_list):
        self.filename = filename
        self.field_list= field_list

    #function to create new csv files
    def create_csv(self):
        with open(self.filename,'x',newline='\n') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(self.field_list)
        print("Database Created")

    def check_database_already_created(self):
        try:
            self.create_csv()
        except FileExistsError as e:
            print(f"File already existed {self.filename}")     

        
    