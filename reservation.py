import csv
class Reservation:
    
    

    def __init__(self,user_id, movie_id, reserve_seat, filename, reserve_id=None):
        self._reserve_list = []
        self.filename = filename
        if len(self._reserve_list) == 0:
            self.read_csv_into_reserve_list()

        if reserve_id == None:
            if self._reserve_list[len(self._reserve_list)-1][0].isdigit():
                reserve_id = int(self._reserve_list[len(self._reserve_list)-1][0]) + 1
            else:
                reserve_id = 0
            self._reserve_id = str(reserve_id)
        else:
            self._reserve_id = reserve_id

        self._user_id= user_id
        self._movie_id = movie_id
        self._reserve_seat = reserve_seat
        
    def reserve_show(self):
        #created to append it into _reserve_list and csv
        self._row=[self._reserve_id, self._user_id, self._movie_id, self._reserve_seat]
        self._reserve_list.append(self._row)
        self.writing_into_csv_file(self._row)
        return self._reserve_id,self._user_id,self._movie_id,self._reserve_seat

    def cancel_reserve(self,no_of_seats,movie_name):
        if int(no_of_seats) < int(self._reserve_seat):
            self._reserve_seat=int(self._reserve_seat) - int(no_of_seats)
            self._row=[self._reserve_id, self._user_id, self._movie_id, self._reserve_seat]
            for index,reserve in enumerate(self._reserve_list):
                if reserve[0] == self._reserve_id:
                    self._reserve_list[index] = self._row
                    break
            
        
        elif int(no_of_seats) == int(self._reserve_seat):
            for index,reserve in enumerate(self._reserve_list):
                if reserve[0] == self._reserve_id:
                    del self._reserve_list[index]
                    break
        
        else:
            print("Invalid no_of_seats entered")
            return False
                    
            
        #Overwriting the data in movie.
        with open(self.filename,'w',newline='\n') as csv_file:
            # field_list=["movie_id","movie_name","movie_description","movie_status","total_seats","booked_seats","available_seats"]
            csv_writer = csv.writer(csv_file)
            # csv_writer.writerow(field_list)
            csv_writer.writerows(self._reserve_list)
        
        print(f"{no_of_seats} have been unreserved successfully")

        return True
        
        


    def delete_reserve():
        pass


     #read movie.csv into class attribute _movie_list
    def read_csv_into_reserve_list(self):

        with open(self.filename,'r') as csv_file:
            csv_reader =csv.reader(csv_file)
            for index,line in enumerate(csv_reader):
                if index != 0:
                    line[1] = int(line[1])
                    line[2] = int(line[2])
                    line[3] = int(line[3])
                self._reserve_list.append(line)

    #adding the data to the movie.csv file
    def writing_into_csv_file(self,_row):

        with open(self.filename,'a',newline='\n') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(self._row)


    def __repr__(self):
        return f"Reservation('reserve.id':{self._reserve_id},'user_id':{self._user_id},'movie_id':{self._movie_id},'reserve_seat':{self._reserve_seat})"

