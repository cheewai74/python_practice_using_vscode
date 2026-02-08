# mypy broadcast_notification.py



import logging
from typing import Iterable

#  mypy broadcast_notification.py:
#  mask code: error: Name "logger" is not defined  [name-defined] Found 1 error in 1 file (checked 1 source file)
#  unmask code: Success: no issues found in 1 source file

logger = logging.getLogger(__name__)    

def broadcast_notification(message: str, relevant_user_emails: Iterable[str]):
    for email in relevant_user_emails:
        logger.info("Sending %r to %r", message, email)

print(broadcast_notification("welcome", "user1@domain.com"))