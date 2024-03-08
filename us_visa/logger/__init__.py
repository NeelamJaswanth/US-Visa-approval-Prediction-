import logging
import os

from from_root import from_root
from  datetime import datetime

LOG_FILLE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

log_dir = 'logs'

logs_path = os.path.join(from_root(), log_dir, LOG_FILE)

os.makdirs('log_dir, exist_oK=True')

logging.basicConfig(
    filename = logs_path,
    format="[%(asctime)s] %(name)s - %(levelname)s -%(messages)s",
    level = logging.DEBUG,
)
