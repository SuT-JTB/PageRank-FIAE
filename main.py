import sqlalchemy
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost", user="root", password="", database="wiki"
)


def main():
    print("")
    mycursor = mydb.cursor()
    mycursor.execute("""
		SELECT page.page_id, page.page_title, linktarget.lt_title FROM page
		INNER JOIN pagelinks ON page.page_id = pagelinks.pl_from
		INNER JOIN linktarget ON pagelinks.pl_target_id  = linktarget.lt_id
		WHERE linktarget.lt_title = 'Python'
		""")

    myresult = mycursor.fetchall()
    if myresult is not None:
        for x in myresult:
            print(x)


if __name__ == "__main__":
    main()
