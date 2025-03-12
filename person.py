import csv
#creating person class
class Person:
    
    def __init__(self,name, date_of_birth, mob_no, email_id, gender):
        self._name = name
        self._date_of_birth = date_of_birth
        self._mob_no = mob_no
        self._email_id = email_id
        self._gender = gender

    def __repr__(self):
        return f"Person({self._name},{self._date_of_bith},{self._mob_no},{self._email_id},{self._gender})"
    
class Member(Person):
    
    def __init__(self, name,date_of_birth,mob_no,email_id,gender,filename,member_id=None,permission="Member"):
        self.user_list = []
        self.filename = filename
        #filling _user_list from users.csv files
        if len(self.user_list) == 0:
            self.read_csv_into_user_list()
        
        #making the unique id user logic
        # user_id = 0
        #adding the user_count by +1
        #[-1][0] access the last rows user_id
        # self._user_list[-1][0].isdigit() or 
        if member_id == None:
            if self.user_list[-1][0].isdigit():
                user_id = int(self.user_list[-1][0]) + 1
                # print(user_id)
            else:
                user_id = 0
            
            self._user_id = str(user_id)
        else:
            self._user_id = member_id
        super().__init__(name, date_of_birth, mob_no, email_id, gender)
        self._permission = "Member"
        

    #while initializing read csv_file into user_list
    def read_csv_into_user_list(self):

        with open(self.filename,'r') as csv_file:
            csv_reader =csv.reader(csv_file)
            for line in csv_reader:
                self.user_list.append(line)

    def writing_into_csv_file(self,_row):
        with open(self.filename,'a',newline='\n') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(self._row)
        


    #for members
    def search_movies(self):
        pass


    def add_member(self):
        self._row=[self._user_id, self._name, self._date_of_birth, self._mob_no, self._email_id, self._gender, self._permission]

        self.user_list.append(self._row)
        self.writing_into_csv_file(self._row)
        print(f"user{self._name} Member added with {self._user_id}")
        return self._user_id

    def modify_movies(self):
        pass

    def delete_movies(self):
        pass

    def check_user_exist(self,name,phone,role):


        # #for debuggin
        # if self._user_list[1][1] == name and self._user_list[1][3] == phone and self._user_list[1][6] == role:
        #     print(self._user_list[1][1])
        #     print(type(self._user_list[1][1]),type(name))
        #     print(type(self._user_list[1][3]),type(phone))
        #     print(type(self._user_list[1][6]),type(role))
        #     return True
        # else:
        #     # print(type(self._user_list[1][1]),type(name))
        #     return False
        
        for user in self._user_list:
            if user[1] == name and user[3] == phone and user[6] == role:
                return user[0]# returns the user_id
            
                # return user[0] #returns the match user_id
        # if not found it returns False
        print("Invalid Input or No such {role} user")
        return None


# u100 = User("Hari","2000",98131112222,"ram@gmail.com","M","Admin")
# u100.add_movies()

class Admin(Person):

    def __init__(self, name, date_of_birth, mob_no, email_id, gender,filename,admin_id=None,permission="Admin"):
        super().__init__(name, date_of_birth, mob_no, email_id, gender)
        self.user_list = []
        
        self.filename = filename

        #filling for user_list for all
        if len(self.user_list) == 0:
            self.read_csv_into_user_list()
        #making the unique id user logic
        # user_id = 0
        #adding the user_count by +1
        #[-1][0] access the last rows user_id
        # self._user_list[-1][0].isdigit() or 
        if admin_id == None:
            if self.user_list[-1][0].isdigit():
                user_id = int(self.user_list[-1][0]) + 1
                # print(user_id)
            else:
                user_id = 0
            
            self._user_id = str(user_id)
        else:
            self._user_id = admin_id

        # self.admin_list = [user if user[6]=="Admin" for user in self._user_list]
        self._permission = "Admin"


    def read_csv_into_user_list(self):

        with open(self.filename,'r') as csv_file:
            csv_reader =csv.reader(csv_file)
            for line in csv_reader:
                self.user_list.append(line)

    def writing_into_csv_file(self,_row):
        with open(self.filename,'a',newline='\n') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(self._row)

    def check_admin_id(self,admin_id):
        # admin_id_list = [user[0] if user[6]=="Admin" for user in self.user_list]
        admin_id_list = [user[0]  for user in self.user_list if user[6]=="Admin"]
        if admin_id in admin_id_list:
            return True
        else:
            return False
        
    def add_admin(self):
        self._row=[self._user_id, self._name, self._date_of_birth, self._mob_no, self._email_id, self._gender, self._permission]

        self.user_list.append(self._row)
        self.writing_into_csv_file(self._row)
        print(f"user{self._name} admin added with {self._user_id}")
        return self._user_id

