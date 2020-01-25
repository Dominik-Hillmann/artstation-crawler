# Python libraries
from argparse import ArgumentParser
import json


class ParameterParser:
    """Converts console parameters and config file into a dictionary that
    will be used throughout the program.
    """

    def __init__(self):
        self.command_line_args = self._parse_command_line_parameters()
        self.config_args = self._parse_config_file()

    
    def get_params(self):
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

        param_dict = vars(param_parser.parse_args())
        return param_dict


    def _parse_config_file(self):
        with open('config.json', mode = 'r') as config_file:
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
