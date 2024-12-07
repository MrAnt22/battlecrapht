import datetime

def log_decorator(func):
    def wrapper(self, level, message):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        formatted_message = f"[{timestamp}] [{level.upper()}] {message}"
        return func(self, level, formatted_message)
    return wrapper

class Logger:
    def log(self, level, message):
        raise NotImplementedError("Subclasses should implement this method.")

class FileLogger(Logger):
    def __init__(self, filename):
        self.filename = filename

    @log_decorator
    def log(self, level, message):
        with open(self.filename, "a") as file:
            file.write(message + "\n")

class ConsoleLogger(Logger):
    @log_decorator
    def log(self, level, message):
        print(message)

class MultiLogger(Logger):
    def __init__(self, *loggers):
        self.loggers = loggers

    def log(self, level, message):
        for logger in self.loggers:
            logger.log(level, message)

class LevelFilterLogger(Logger):
    def __init__(self, logger, min_level):
        self.logger = logger
        self.min_level = min_level
        self.levels = {"debug": 1, "info": 2, "warning": 3, "error": 4}

    def log(self, level, message):
        if self.levels[level] >= self.levels[self.min_level]:
            self.logger.log(level, message)