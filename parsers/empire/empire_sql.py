from sqlalchemy import create_engine

empire_engine = create_engine('sqlite:///db/empire.db')
empire_engine.connect()

