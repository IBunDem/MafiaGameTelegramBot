class BotTokenNotFoundException(Exception):
    def __init__(self, message: str = 'Not found telegram bot API token. Add it to your .env file with key TOKEN'):
        super().__init__(message)
