# Python libraries
from argparse import ArgumentParser
import json
# External libraries

class ParameterParser:

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
            type = list, 
            action = 'store',
            nargs = '+',
            help = 'Required: the search terms with pictures will be searched for.'
        )
        param_parser.add_argument(
            '-n', '--number_pictures',
            type = int,
            action = 'store',
            nargs = 1,
            help = 'Required: the number of pictures you want to downloaded.'
        )

        return vars(param_parser.parse_args())

    def _parse_config_file(self):
        with open('config.json', 'r') as config_file:
            config = json.load(config_file)

            # for key, value in config.items():
            #     config[str(key)] = str(value)
            #     del config[key]

            return config
            

test = ParameterParser().get_params()
print(test)