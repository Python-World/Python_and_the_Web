import logging
from datetime import datetime

from bot import run_python_bot
from pytz import timezone

TIMEZONE = "Asia/Kolkata"

logging.Formatter.converter = lambda *args: datetime.now(
    tz=timezone(TIMEZONE)
).timetuple()

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
    datefmt="%d/%m/%Y %I:%M:%S %p",
)

logger = logging.getLogger()
logger.setLevel(20)

run_python_bot.bot()
