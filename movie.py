# creating class for movies
import csv

class Movie:
    

    def __init__(self, movie_name, movie_description, movie_status,filename,movie_id=None):
        self._movie_list= []
        self.filename = filename
        if len(self._movie_list) == 0:
            self.read_csv_into_movie_list()

        if movie_id == None:
            if self._movie_list[-1][0].isdigit():
                movie_id = int(self._movie_list[-1][0]) + 1
            else:
                movie_id = 0
            self._movie_id = str(movie_id)
        else:
            self._movie_id = movie_id


        self._movie_name = movie_name
        self._movie_description = movie_description
        self._movie_status = movie_status #[either available or un_available]
        if self._movie_status == "Unavailable":
            self._total_seats = 0
        self._total_seats = 200
        self._booked_seats = 0
        self._available_seats = self._total_seats - self._booked_seats
        

    #read movie.csv into class attribute _movie_list
    def read_csv_into_movie_list(self):

        with open(self.filename,'r') as csv_file:
            csv_reader =csv.reader(csv_file)
            for index,line in enumerate(csv_reader):
                # breakpoint()
                # print(type(line[5]))
                if index != 0:
                    # line[0]= int(line[0])
                    line[5]= int(line[5])
                    line[6]= int(line[6])
                self._movie_list.append(line)

    #adding the data to the movie.csv file
    def writing_into_csv_file(self,_row):

        with open(self.filename,'a',newline='\n') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(self._row)


    #movie add can be done only by admins
    def add_movie(self):
        self._row=[self._movie_id, self._movie_name,self._movie_status, self._movie_description, self._total_seats, self._booked_seats, self._available_seats]

        self._movie_list.append(self._row)
        self.writing_into_csv_file(self._row)


    def delete_movie(self):
        pass

   

    def update_booked_seats(self,movie_id,no_of_seats=0,no_of_seats_unreserve=0):

        # next(self._movie_list)
        index= 0
        #can do optimization
        for i,row in enumerate(self._movie_list):
            if i==0:
                continue
            if row[0] == movie_id:
                # print(row)
                index = i
                # print(index)
                break
        # Changing the booked_seats and availbale in _movie_list
        # print(self._movie_list[index][5],self._movie_list[index][6],type(no_of_seats))
        # this code if will be used to reserve the seats
        # self._movie_list[index][5]  has booked seats data 
        # self._movie_list[index][5] has available seats data for a movie
        if no_of_seats != 0: 
            self._movie_list[index][5] = int(self._movie_list[index][5]) + int(no_of_seats)
            self._movie_list[index][6] = int(self._movie_list[index][6]) - int(no_of_seats)
            print(f"index:{index}")
            #if available_seats is zero set it to Fully reserve
            if self._movie_list[index][6] == 0:
                self._movie_list[index][2] ="Fully Reserved"
                print(f"Movie id {self._movie_id} {self._movie_name} is Fully Reserved")
        #whereas this below code will run for seats to unreserve the seat
        else:
            print(f"index this :{index}")
            self._movie_list[index][5] = int(self._movie_list[index][5]) - int(no_of_seats_unreserve)
            self._movie_list[index][6] = int(self._movie_list[index][6]) + int(no_of_seats_unreserve)
            
            #if available_seats is not zero set it to Available
            if self._movie_list[index][6] != 0:
                self._movie_list[index][2] ="Available"
                # print(f"Movie id {self._movie_id} {self._movie_name} is Available")
        

        #Overwriting the data in movie.
        with open(self.filename,'w',newline='\n') as csv_file:
            # field_list=["movie_id","movie_name","movie_description","movie_status","total_seats","booked_seats","available_seats"]
            csv_writer = csv.writer(csv_file)
            # csv_writer.writerow(field_list)
            csv_writer.writerows(self._movie_list)


        # self._movie_list[1+movie_id][5] += no_of_seats
        print(f"updated seats")
        for movies in self._movie_list:
            print(movies)
        return True



    

    # def check_movie_id_in_movie_list(self,movie_id):
    #     # def is_available(row):
    #     #     return row[2]=="Available"
    #     # #using filter to show only Available movies

    #     # available_movies = list(filter(is_available,self._movie_list))
    #     # print(available_movies)

    #     movie_id_list = [item[0] for item in self._movie_list[1:]]
    #     return True if movie_id in movie_id_list else False
    

    #  def show_movies(self):

    #     def is_available(row):
    #         return row[2]=="Available"
    #     #using filter to show only Available movies

    #     availabe_movies = list(filter(is_available,self._movie_list))
    #     print("Available Movies only")
    #     for movies in availabe_movies:
    #         print(movies)
    
    def show_available_seats(self):
        pass
       


    

