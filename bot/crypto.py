import logging
from aiohttp import ClientSession, ClientTimeout, ClientResponseError
from .config import Config


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class CoinGeckoAPI:
    def __init__(self, config = None):
        self.config = config or Config()
        self.base_url = 'https://api.coingecko.com/api/v3/coins/markets'
        self.params = {
            'vs_currency': 'usd',
            'order': 'market_cap_desc',
            'per_page': 100,
            'page': 1,
            'sparkline': 'false'
        }
        self.session: ClientSession = None

    async def get_top_100_coins(self) -> dict | None:
        await  self._create_session()
        try:
            async with self.session.get(self.base_url, params=self.params) as response:
                response.raise_for_status()
                return await response.json()
        except ClientResponseError as e:
            logger.error(f"Error when requesting API CoinGecko: {e}")
            return None
        except Exception as e:
            logger.error(f"An unexpected error occurred: {e}")
            return None
        finally:
            await self._close_session()

    async def _create_session(self) -> None:
        if not self.session:
            self.session = ClientSession(timeout=ClientTimeout(total=10))

    async def _close_session(self) -> None:
        if self.session:
            await self.session.close()
            self.session = None
