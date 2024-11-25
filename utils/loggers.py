import datetime

class Logger:
    def log(self, level, message):
        raise NotImplementedError("Subclasses should implement this method.")

    def format_message(self, level, message):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return f"[{timestamp}] [{level.upper()}] {message}"

class FileLogger(Logger):
    def __init__(self, filename):
        self.filename = filename

    def log(self, level, message):
        formatted_message = self.format_message(level, message)
        with open(self.filename, "a") as file:
            file.write(formatted_message + "\n")

class ConsoleLogger(Logger):
    def log(self, level, message):
        formatted_message = self.format_message(level, message)
        print(formatted_message)

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
