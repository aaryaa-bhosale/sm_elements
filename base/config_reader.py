"""
@package base

ConfigReader class implementation

It reads the configuration files needed for the framework

Example:
    self.config = ConfigReader(filename=filename)
    self.config.config_read()
    value = self.config.get_configuration(section, option)


"""
from configparser import ConfigParser
import os

class ConfigReader(object):

    def __init__(self,filename):
        self.parser = ConfigParser()
        script_directory = os.path.dirname(__file__)
        relative_path = "../configfiles/"+filename
        #script_directory = "/Users/aaryabhosale/PycharmProjects/sm_elements/"
        #relative_path = "configfiles/" + filename
        abs_file_path = os.path.join(script_directory,relative_path)
        self.file = abs_file_path

    def config_read(self):
        self.parser.read(self.file)

    def config_section_map(self,section):
        """
        Returns a dictionary of 'Option and Value' under a section



        :param section: Section in the file under which options exist

        :return: Dictionary of 'Option and Value'
        """
        config = {}
        options = self.parser.options(section)
        for option in options:
            try:
                config[option] = self.parser.get(section, option)
                if config[option] == -1:
                    print("skip: %s" %option)
            except:
                print("exception on %s!" %option)
                config[option] = None

        return config

    def get_configuration(self, section, option):
        """
        Get value of the provided option and section
        :param section: Section in the file under which options exist
        :param option: Option whose corresponding value is needed
        :return: value of the provided option
        """
        config_map = self.config_section_map(section)
        option_value = config_map[option]
        return option_value

    def test_method(self):
        value = ConfigReader.get_configuration(self,'SiteConfiguration','password')
        print(value)


#cfg = ConfigReader(filename="test_environment.ini")
#cfg.config_read()
#cfg.test_method()

