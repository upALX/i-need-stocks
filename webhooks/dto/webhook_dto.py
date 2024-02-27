from datetime import datetime
class WebhookDTO:

    def __init__(self, webhook_key: str, creation_date: datetime) -> None:
        self.webhook_key = webhook_key
        self.creation_date = creation_date
