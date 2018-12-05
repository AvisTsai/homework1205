import sqlite3

connection = sqlite3.connect("ntub.db")

def get_books():   #搜尋
    c = connection.cursor()
    books = c.execute("select * from book").fetchall()
    c.close()
    return books


def get_book(pk):
    c = connection.cursor()
    books = c.execute("select * from book where id =?", [pk]).fetchone()
    c.close()
    return books

# print(get_book('1'))

def create_book(name,price):
    c = connection.cursor()
    c.execute("insert into book (name , price) values(?, ?)", [name, price])
    last_id = c.lastrowid
    connection.commit()
    c.close()
    return last_id

def update_book(pk, name, price):
    if get_book(pk) is None:
        return False
        
    c = connection.cursor()
    c.execute("update book set name = ?, price=? where id =?", [name, price, pk])
    connection.commit()
    c.close()
        
def delete_book(pk):
    if get_book(pk) is None:
        return False

    c = connection.cursor()
    c.execute("delete from book where id = ?", [pk])
    connection.commit()
    c.close()
            
create_book(name,price)
print(get_books())

print('''
功能選單:
    g -> 搜尋資料
    ls -> 列出所有資料
    C -> 新增資料
    d -> 刪除資料
    u -> 更改資料
    e -> 離開程式
''')

choice = input("請輸入你需要的功能")

while True:
    
    if  choice  == 'g':
        # 問使用者要哪個ID的書 1
        book_id = input("請問要輸入哪個ID的書")
        # 找書
        
        # 輸出