# Python libraries
from argparse import ArgumentParser
import json


class ParameterParser:
    """Converts console parameters and config file into a dictionary that
    will be used throughout the program."""

    def __init__(self, config_file_name = 'config.json'):
        self.config_file_name = config_file_name
        self.command_line_args = self._parse_command_line_parameters()
        self.config_args = self._parse_config_file()

    
    def get_params(self):
        """Get the parsed parameters.

        Returns:
            dict: The parameter dictionary.
        """

        all_params = {}
        all_params.update(self.command_line_args)
        all_params.update(self.config_args)        
        return all_params


    ###################
    # Private methods #
    ###################

    def _parse_command_line_parameters(self):
        param_parser = ArgumentParser()
        
        param_parser.add_argument(
            '-s', '--search-terms', 
            type = str,
            required = True,
            action = 'store',
            nargs = '+',
            help = 'Required: the search terms with pictures will be searched for.'
        )
        
        param_parser.add_argument(
            '-n', '--number-pictures',
            type = int,
            required = True,
            action = 'store',
            help = 'Required: the number of pictures you want to download.'
        )

        param_parser.add_argument(
            '-l', '--links-only',
            action = 'store_true',
            required = False,
            help = 'If flag is set, only new links will be extracted from the \
            search page and put into the queue.'
        )

        param_parser.add_argument(
            '-p', '--pictures-only',
            action = 'store_true',
            required = False,
            help = 'If flag is set, only pictures from the queue will be downloaded.'
        )

        param_dict = vars(param_parser.parse_args())
        if param_dict['links_only'] and param_dict['pictures_only']:
            raise ValueError('You can only use either the links-only flag or \
            the pictures-only flag but not both.')

        return param_dict


    def _parse_config_file(self):
        with open(self.config_file_name, mode = 'r') as config_file:
            config_json = json.loads(config_file.read(), encoding = 'utf-8')
            
            return self._remove_u_str_keys(config_json)
    

    @staticmethod
    def _remove_u_str_keys(dictionary):
        re_dict = {}
        for key, value in dictionary.items():
            if type(value) is unicode:
                re_dict[str(key)] = str(value)
            else:
                re_dict[str(key)] = value

        return re_dict 
