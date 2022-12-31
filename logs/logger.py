import logging
logging.basicConfig(level=logging.INFO)

logger_api = logging.getLogger("api_log")

file_handler = logging.FileHandler('logs/api_log.txt', encoding='utf-8')
file_handler.setLevel(logging.INFO)
logger_api.addHandler(file_handler)
formatter_one = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
file_handler.setFormatter(formatter_one)
logger_api.warning("logger api is working")