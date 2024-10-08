class star_cinema:
  hall_list=[]
  def entry_hall(self,hall_objects):
    self.hall_list.append(hall_objects)
class Hall(star_cinema):
  def __init__(self,rows,columns,hall_no) -> None:
    self.seat={}
    self.show_list=[]
    self.rows=rows
    self.columns=columns
    self.hall_no=hall_no
    self.entry_hall(self)
  def entry_show(self,id,movie_name,time):
   self.movie_name=movie_name
   self.time=time
   self.show_list.append((id,movie_name,time))
   self.seat[id]=[[0 for _ in range(self.columns)]for _ in range(self.rows)]
  def book_seats(self,movie_id,seat_info):
    if movie_id in self.seat:
      row,column=seat_info
      if 0<=row <=self.rows and 0<=column and column<=self.columns:
        if self.seat[movie_id][row][column]==0:
          self.seat[movie_id][row][column]==1
          for show in self.show_list:
            if show[0]==movie_id:
              movie_name,time=show[1],show[2]
              break
          print(f"Congratulation! seat[{row}][{column}] Booked Successful")
          print(f"Enjoy '{movie_name}' in {time} and have chill!")
        else:
          print(f"Sorry! Seat Is Already Booked\nTry Another Movie thank You")
      else:
        print(f"invalid Seat[{row}][{column}] Position\nPlease Enter Valid One")
    else:
      print(f"Sorry Your Enterd Id-{movie_id} Is Not Exist")
  def view_show_list(self):
    for show in self.show_list:
      (movieId, movieName, streamingTime) = show
      print(f"Running Movie Information\nMovie Name: {movieName}\nShedule: {streamingTime}\nMovie Id: {movieId}")
  def view_available_seats(self, id):
    if id in self.seat:
      for row in range(self.rows):
        for col in range(self.columns):
          if self.seat[id][row][col] == 0:
            print(f"Avaiable Seat[{row}][{col}]")
    else:
      print(f"Sorry Your Enterd ID:{id} Is Not Found")
  print(f"\n\n                                            NETFLIX                                            \n")

new_hall = Hall(13, 11, 1)
new_hall = Hall(4, 4, 2)
new_hall = Hall(27, 11, 3)
new_hall = Hall(9, 10, 4)
new_hall.entry_show(8, "Dark", "Tues-6pm")
new_hall.entry_show(13, "Alice in Borderland", "Sun-7pm")
new_hall.entry_show(27, "Taare Zameen Par", "mon-4pm")
new_hall.entry_show(20, "Rockstar", "fri-8pm")
print(f"Please Choose An Option")
print(f"\tOPTION 1: VIEW SHOW LIST\n\tOPTION 2: AVAILABLE SEATS\n\tOPTION 3: BOOK A SEAT\n\tOPTION 0: EXIT")
while True:
  option = int(input())
  if option == 1:
    new_hall.view_show_list()
    
  elif option == 2:
    (f"Please Insert Movie Id For Available Seat")
    movie_ID = int(input())
    new_hall.view_available_seats(movie_ID)
  elif option == 3:
    print("Please Insert 1.Movie Id 2.Seat Row 3.Seat Coloumn")
    id = int(input())
    seatRow = int(input())
    seatColoumn = int(input())
    new_hall.book_seats(id, (seatRow, seatColoumn))
  elif option == 0:
    print(f"Thanks For Browsing")
    break