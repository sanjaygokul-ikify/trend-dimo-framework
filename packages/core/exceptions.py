class DIMOException(Exception):
    pass

class EngineError(DIMOException):
    def __init__(self, message: str):
        self.message = message
        super().__init__(message)
