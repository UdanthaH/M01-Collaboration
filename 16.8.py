from sqlalchemy import create_engine, MetaData, Table, Column, String, select

db_url = "sqlite:///books.db"

engine = create_engine(db_url)

metadata = MetaData()

books_table = Table('books', metadata,
                    Column('title', String),
                    Column('author', String),
                    Column('year', String))  

print(repr(books_table))

with engine.connect() as conn:
    stmt = select([books_table.columns.title]).order_by(books_table.columns.title)

    results = conn.execute(stmt).fetchall()

    print("Titles in alphabetical order:")
    for result in results:
        print(result.title)
