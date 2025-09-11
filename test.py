import logging

logging.basicConfig(
    filename="app.log",          # Log file name
    level=logging.INFO,          # Log level
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)
logger.info("This is written to the file")

