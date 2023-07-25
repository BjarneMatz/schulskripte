#Color Constants
RED = '\033[91m'
YELLOW = '\033[93m'
VIOLET = '\033[95m'
GRAY = '\033[90m'

LOG_PATH = "logs/"

class Logger:
    def __init__(self, logger_name: str, log_to_console: bool = True, log_to_file: bool = True):
        self.log_path = f"{LOG_PATH}{logger_name}.log"
        self.logger_name = logger_name
        self.log_to_console = log_to_console
        self.log_to_file = log_to_file


    def toggle_log_to_console(self, log_to_console: bool):
        self.log_to_console = log_to_console
        
    def toggle_log_to_file(self, log_to_file: bool):
        self.log_to_file = log_to_file


    def log(self, message, log_type: str = "debug"):
        if log_type == "debug":
            console_log_message = f"{GRAY}[DEBUG] ({self.logger_name}) {message}"
            file_log_message = f"[DEBUG] ({self.logger_name}) {message}"
            
        elif log_type == "info":
            console_log_message = f"{VIOLET}[INFO] ({self.logger_name}) {message}"
            file_log_message = f"[INFO] ({self.logger_name}) {message}"
            
        elif log_type == "warning":
            console_log_message = f"{YELLOW}[WARNING] ({self.logger_name}) {message}"
            file_log_message = f"[WARNING] ({self.logger_name}) {message}"
            
        elif log_type == "error":
            console_log_message = f"{RED}[ERROR] ({self.logger_name}) {message}"
            file_log_message = f"[ERROR] ({self.logger_name}) {message}"
            
        else:
            raise ValueError(f"Log type {log_type} is not valid!")
        
        if self.log_to_console:
            self._log_to_console(console_log_message)
        
        if self.log_to_file:
            self._log_to_file(file_log_message)

    def _log_to_console(self, message):
        print(message)
    
    def _log_to_file(self, message):
        with open(self.log_path, 'a') as f:
            f.write(message + '\n')