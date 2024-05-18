class Star_Cinema:
    hall_list = []

    @staticmethod
    def entry_hall(hall):
        Star_Cinema.hall_list.append(hall)

class Hall:
    def __init__(self, rows, cols, hall_no):
        self.seats = {}
        self.show_list = []
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no

    def entry_show(self, id, movie_name, time):
        self.show_list.append([id, movie_name, time])
        self.seats[id] = [[0] * self.cols for _ in range(self.rows)]
    
    def book_seats(self, id, seats):
        if id not in self.seats:
            raise Exception("id not found.")
        for seat in seats:
            if seat[0] < 0 or seat[0] > self.rows or seat[1] < 0 or seat[1] > self.cols:
                raise Exception("Invalid seat")
        for seat in seats:
            self.seats[id][seat[0]][seat[1]] = 1
    
    def view_show_list(self):
        for show in self.show_list:
            print(str(show[0]) + ": " + show[1] + " (" + show[2] + ")")
    
    def view_available_seats(self, id):
        for i in range(self.rows):
            print(self.seats[id][i])

hall = Hall(10, 10, 1)
hall.entry_show(1, "Terminator 2", "01/01/2024")
hall.entry_show(2, "Terminator 3", "02/01/2024")
Star_Cinema.entry_hall(hall)

while True:
    print("---------")
    print("1. VIEW ALL SHOW TODAY")
    print("2. VIEW AVAILABLE SEATS")
    print("3. BOOK TICKET")
    print("4. Exit")

    inp = int(input("ENTER OPTION: "))

    if inp == 4:
        break
    if inp == 1:
        hall.view_show_list()
    if inp == 2:
        id = int(input("ENTER SHOW ID: "))
        if id not in hall.seats:
            print("Invalid ID. Please try again.")
            continue
        hall.view_available_seats(id)
    if inp == 3:
        id = int(input("Show ID: "))
        if id not in hall.seats:
            print("Invalid ID. Please try again.")
            continue
        num_tickets = int(input("Number of Tickets: "))
        seats = []
        for i in range(num_tickets):
            print("Ticket " + str(i+1) + " details: ")
            row = int(input("Enter Row: "))
            col = int(input("Enter Col: "))
            seats.append((row, col))
        hall.book_seats(id, seats)
        print(str(num_tickets) + " seats booked successfully.")

