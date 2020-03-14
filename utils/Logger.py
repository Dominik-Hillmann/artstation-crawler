# Python libraries
from datetime import datetime
import os

class Logger:
    """Logs which pictures were successfully captured and which did not."""

    def __init__(self, log_dir):
        self.file_path = os.path.join(log_dir, 'downloads.log')


    def info(self, message):
        message = self._modify_log_message(message, 'info')
        print(message)
        self._write_to_file(message)


    def warn(self, message):
        message = self._modify_log_message(message, 'warn')
        print(message)
        self._write_to_file(message)


    ###################
    # Private methods #
    ###################

    def _modify_log_message(self, message, log_type):
        now = datetime.now()
        now_formatted = now.strftime('%a %d.%m.%Y %H:%M:%S')
        log_type = log_type[:4].upper()
        modified_message = '{} | {} | {}\n'.format(
            log_type,
            now_formatted,
            message
        )

        return modified_message


    def _write_to_file(self, message):
        try:
            with open(self.file_path, 'a+') as log_file:
                log_file.write(message)
        
        except IOError:
            with open(self.file_path, 'w+') as log_file:
                log_file.write(message)
