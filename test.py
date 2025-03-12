# filename= ['user.csv','movie.csv','reserve.csv']
# field_list=[["user_id","name","date_of_birth","phone","email","gender"],
#             ["movie_id","movie_name","movie_description","movie_status","total_seats","booked_seats","available_seats"],
#             ["reserve_id","user_id","movie_id","reserve_seat"]]

# result = [item[0] for item in field_list[1:]]

# print(result)

# data = {
#             "Book": [
#                 {
#                     "book_id": 1,
#                     "title": "1984",
#                     "author_name": "George Orwell",
#                     "stock": 5,
#                     "avilable": True
#                 },
#                 {
#                     "book_id": 1,
#                     "title": "1984",
#                     "author_name": "George Orwell",
#                     "stock": 6,
#                     "avilable": True
#                 }
#             ]
#         }

# for book in data["Book"]:
#     # print(book)
#     if book['stock'] > 0:
#         book['stock'] -= 1
#     # for item in book:
#     #     if item == "stock" and book[item] > 0:
#     #         book[item] += 1
#     # for value in book["stock"]:
#     #     if value > 5:
#     #         book["stock"] += 1

# print(data)


data={
    "Book": [
        {
            "book_id": 1,
            "title": "sss",
            "author_name": "George Orwell",
            "stock":4
        },
        {
            "book_id": 2,
            "title": "1984",
            "author_name": "George Orwell",
            "stock":4
        }

    ]
}

book_name = "1984"

found = False
for book in data["Book"]:
    
    if book['title'] == book_name:
        found = True
        if book['stock'] > 0:
            book['stock'] -=1
            print(book['title'])
            break
    else:
        continue 
if not found:
    print("Book not found out of stock")

print(data)