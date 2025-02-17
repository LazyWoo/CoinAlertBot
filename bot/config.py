from dotenv import load_dotenv
from  os import  getenv


class Config:
    def __init__(self) -> None:
        load_dotenv()

        self.bot_token = getenv('BOT_TOKEN')
        self.coingecko_api_key = getenv('COINGECKO_API_KEY')

        self._validate()

    def _validate(self) -> None:
        if not self.bot_token:
            raise  ValueError('BOT_TOKEN is not set in the environment variables.')
        if not self .coingecko_api_key:
            raise ValueError('COINGECKO_KEY is not set in the environment variables.')

    def __repr__(self) -> str:
        return '<Config(bot_token=***, coingecko_key=***>'
