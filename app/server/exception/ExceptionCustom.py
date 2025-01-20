class ScrapyError(Exception):
    def __init__(self, message):
        super().__init__(message)

class ETLError(Exception):
    def __init__(self, message):
        super().__init__(message)