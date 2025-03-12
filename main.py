import csv
from person import *
from reservation import Reservation
from movie import Movie
from database import Database
from contextmanager import ContextManager
from fastapi import FastAPI
from pydantic import BaseModel
from enum import Enum
import datetime

filename= ['user.csv','movie.csv','reserve.csv']
field_list=[["user_id","name","date_of_birth","mob_no","email_id","gender","username","password","token","permission"],
            ["movie_id","movie_name","movie_status","movie_description","total_seats","booked_seats","available_seats"],
            ["reserve_id","user_id","movie_id","reserve_seat"]]


# function to read users_data from csv files based on member_type and certain field
def read_from_csv(filename,mode,field_index,data_type):
    with ContextManager(filename,mode) as csv_file:
        csv_reader = csv.reader(csv_file)
        specific_user_list = [line for line in csv_reader if line[field_index] == data_type]
    return specific_user_list


# #function to read available movies from movies csv files
# def read_from_movies_csv(filename,mode,status_type):
#     with ContextManager(filename,mode) as csv_file:
#         csv_reader = csv.reader(csv_file)
#         specific_user_list = [line for line in csv_reader if line[6] == member_type]
#     return specific_user_list
from enum import StrEnum

class GenderType(StrEnum):
    male = "Male"
    female ="Female"

class MemberType(StrEnum):
    admin = "Admin"
    member = "Member"

from typing import Optional


class Users(BaseModel):
    name: str
    date_of_birth : str
    mob_no : int    
    email : str
    gender : GenderType
    username : str
    password : str
    permission : MemberType
    token : Optional[str] = None
    

# asd = Users(**{})
# asd.model_dump()



def create_database():
    for f_name,f_list in zip(filename,field_list):
        d = Database(f_name,f_list)
        d.check_database_already_created()


app = FastAPI()


@app.get('/')
def show_helloworld():
    return "Hello World"

@app.post('/users/')
def create_users(users: Users):
    create_database()
    u = users.model_dump()
    u['token'] = uuid.uuid1()
    user_details = list(u.values())
    
    username_list = read_from_csv(filename[0],'r',6,users.username)
    print(users.username)
    print(username_list)
    #logic if username_list is empty there is no username in database
    if len(username_list) == 0:
        if users.permission == "Admin":
            a = Admin(*user_details,filename[0])
            token_id = a.add_admin()
        else:
            m = Member(*user_details,filename[0])
            token_id = m.add_member()
        # return {key : value for key, value in u.items() if key not in ['password','permission','token']}
        return f{"Username {u.username} with {u.permission} permission is created successfully"}

    else:
        return {"error":"Please try another username"}



# app.post('/login/{username}')








# if __name__ == '__main__':

#     while(True):
         
#         input_string = input(INPUT_STRING)

#         #creates necessary database csv files
#         if input_string == "1":
#             for f_name,f_list in zip(filename,field_list):
#                     d = Database(f_name,f_list)
#                     d.check_database_already_created()
#         elif input_string =="2":
#             choice = input("Enter 1 to add admin or 2 to add member:")
#             user_details = [input(f"Enter your {field_list[0][index]}:") for index in range(1,len(field_list[0])-1)]
#             if choice == '1':
#                 a = Admin(*user_details,filename[0])
#                 a.add_admin()
#             elif choice == '2':
#                 m = Member(*user_details,filename[0])
#                 m.add_member()
#             # code left for if there is already user with info
#             # we can use uuid for unique uuid
            
        

#         elif input_string =='3':
#             admin_id = input("Enter your admin_id to add movies:")
#             # todo read from users.csv
#             index = 6 #index 6 has permission data in files
#             admin_list = read_from_csv(filename[0],'r',index,'Admin')
#             admin_data = None

#             #checking if there is such admin id 
#             for admin in admin_list:
#                 if admin_id == admin[0]:
#                     admin_data = admin
#                     break
#                 #slicing done admin class does not take user_id and permission it in constructor it creates data by default
    
#             if admin_data != None:
#                 a = Admin(*admin_data[1:6],filename[0],admin_data[0],admin_data[6])
#                 movie_details = [input(f"Enter  Movie {detail}:") for detail in ["Name","Description","Status"]]
#                 m = Movie(*movie_details,filename[1])
#                 m.add_movie()
#             else:
#                 print(f"Please try again No such {admin_id} admin id")
            
            

#         elif input_string =='4':
#             index = 2 # 2 has movie_status data to list out only "Available movies"
#             movie_list = read_from_csv(filename[1],'r',index,"Available")

#             # shows available movies
#             for movie in movie_list:
#                 print(movie)
            
#             reserve_choice = input("Do you Want to reserve movies from above available list\nPress 1 to reserve and any key to go back:")
#             if reserve_choice == '1':
#                 member_id = input("Enter your member_id to reserve:")
#                 member_list = read_from_csv(filename[0],'r',6,"Member")# 6 has permission for users

#                 member_data = None
#                 #checking if there is such member id
#                 for member in member_list:
#                     if member_id == member[0]:
#                         member_data = member
#                         break

#                 if member_data != None:
#                     m1 = Member(*member_data[1:6],filename[0],member_data[0],member_data[6])
#                     movie_id = input("Enter movie id that you want to reserve:")
#                     movie_data = None

#                     #checking to see if such movie id is there in database
#                     for movie in movie_list:
#                         if movie[0]==movie_id:
#                             movie_data = movie
#                             break
                    
#                     if movie_data != None:
    
#                         mo1 = Movie(*movie_data[1:4],filename[1],movie_data[0])
                       
#                         print(f"{movie_data[6]} Available seats for {movie_data[1]}")
#                         while True:
#                             no_of_seats = input("Enter the no_of_seats you want to reserve:")
#                             if int(no_of_seats) <= int(movie_data[6]):
#                                 break
#                             else:
#                                 print("Please enter seats that are available")
#                         r1 = Reservation(member_id,movie_id,no_of_seats,filename[2])

#                         #Now reserves only if update_booked_seats updates and returns false
#                         if mo1.update_booked_seats(movie_id,no_of_seats,0):
#                             reserve_data = r1.reserve_show()
#                             print(f"You have successfully reserved the {reserve_data[3]} seats with reserve id: {reserve_data[0]} for  {movie_data[1]} movie ")
#                         else:
#                             print("Reservation failed")

#                     else:
#                         print(f"No such movie id")
                


#                 else:
#                     print(f"No such member id {member_id}")
                       


#         elif input_string == "5":
#             member_id = input("Enter your member_id to unreserve seats movie:")
#             reserve_list = []
#             reserve_list = read_from_csv(filename[2],'r',1,member_id)
#             if reserve_list != []:
#                 print(reserve_list)
                
#                 while True:
#                     reserve_id =input("Enter your reserve id that you want to unreserve:")
#                     reserve_data = []
#                     for data in reserve_list:
#                         if data[0] == reserve_id:
#                             reserve_data = data
#                             break
#                     if reserve_data == []:
#                         print(f"Please enter correct reserve_id")
#                     else:
#                         break

#                     #creating reservation object 
#                 r = Reservation(*reserve_data[1:],filename[2],reserve_data[0])
#                 #movie data will have list within list
#                 movie_data = read_from_csv(filename[1],'r',0,reserve_data[2])
#                 # print(filename[1],movie_data[0])
#                 m = Movie(*movie_data[0][1:4],filename[1],movie_data[0])
#                 # print("movie_data",movie_data,movie_data[0])
#                 seats_to_unreserve = input("Enter number of seats to unreserve")
#                 if r.cancel_reserve(seats_to_unreserve,movie_name=movie_data[0][1]):
#                     if m.update_booked_seats(movie_data[0][0],no_of_seats=0,no_of_seats_unreserve=seats_to_unreserve):
#                         print(f"Successfully updated movie database after unreserving movies")





#                     # and updates movie seats









#         else:
#              exit()

     

       
    
    # # Trying to create csv file for movie
    # try:
    #     create_csv(filename=filename_m, field_list=field_list_m)
    # except FileExistsError as e:
    #     print(f"File already existed {filename}")

    # m = Movie("Avengers","Adventure movie", "Available")
    # m.add_movie()
    # m.show_movies()


    # #logic for reserving 
    # user_id = int(input("Enter your user_id:"))
    # movie_id = int(input("Enter movie id you want to reserve:"))
    # no_of_seats = int(input(f"Enter no of seats you want to reserve for  {movie_id} id:"))
    # m.update_booked_seats(movie_id,no_of_seats)
    # r= Reservation(user_id,movie_id,no_of_seats)
    # r.reserve_show()
