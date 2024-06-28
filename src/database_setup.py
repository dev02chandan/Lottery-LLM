# database_setup.py
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URI = 'sqlite:///lottery_game.db'
engine = create_engine(DATABASE_URI, echo=True)
Base = declarative_base()

# Define the LotteryGame table
class LotteryGame(Base):
    __tablename__ = 'lottery_game'
    id = Column(Integer, primary_key=True)
    game_name = Column(String)
    jackpot = Column(Float)
    draw_date = Column(String)

# Create the table
Base.metadata.create_all(engine)

# Insert some dummy data
Session = sessionmaker(bind=engine)
session = Session()

lottery_games = [
    LotteryGame(game_name='Mega Millions', jackpot=370500000, draw_date='2024-07-01'),
    LotteryGame(game_name='Powerball', jackpot=410000000, draw_date='2024-07-02'),
    LotteryGame(game_name='Super Lotto', jackpot=100000000, draw_date='2024-07-03'),
    LotteryGame(game_name='Daily Grand', jackpot=25000000, draw_date='2024-07-04'),
    LotteryGame(game_name='Lotto Max', jackpot=70000000, draw_date='2024-07-05'),
    LotteryGame(game_name='EuroMillions', jackpot=150000000, draw_date='2024-07-06'),
    LotteryGame(game_name='EuroJackpot', jackpot=90000000, draw_date='2024-07-07'),
    LotteryGame(game_name='Cash4Life', jackpot=7000000, draw_date='2024-07-08'),
    LotteryGame(game_name='UK Lotto', jackpot=20000000, draw_date='2024-07-09'),
    LotteryGame(game_name='Australia Powerball', jackpot=60000000, draw_date='2024-07-10'),
    LotteryGame(game_name='Canada Lotto 6/49', jackpot=5000000, draw_date='2024-07-11'),
    LotteryGame(game_name='Japan Jumbo Draw', jackpot=10000000, draw_date='2024-07-12'),
    LotteryGame(game_name='Germany Lotto', jackpot=45000000, draw_date='2024-07-13')
]

session.add_all(lottery_games)
session.commit()

print("Database setup complete with dummy data.")
