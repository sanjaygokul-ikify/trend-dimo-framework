class DIMOException(Exception):
    pass

class EngineError(DIMOException):
    def __init__(self, message: str):
        self.message = message
        super().__init__(message)

class TimeoutError(DIMOException):
    def __init__(self, timeout_duration: int):
        self.timeout_duration = timeout_duration
        super().__init__(f'Timeout after {timeout_duration} seconds')
