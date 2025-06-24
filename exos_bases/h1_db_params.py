from sqlalchemy import create_engine 
my_db_name="minibank_db"
my_db_url=f"sqlite:///./{my_db_name}"  # ou bien url mysql ou autre (ex : postgres)

my_db_sql_alchemy_engine = create_engine(my_db_url)