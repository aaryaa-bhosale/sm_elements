"""
@package base

TestDataReader class implementation

It reads the testdata files needed for the automation

Example:
    self.testdata = TestDataReader(filename=filename)
    self.testdata.testdata_read()
    value = self.testdata.get_testdata(section, option)


"""
from base.config_reader import ConfigReader


class SampleDataReader(ConfigReader):

    def sample_data_read(self):
        self.config_read()

    def get_sample_data(self, section, option):
        """
        Get value of the provided option and section
        :param section: Section in the file under which options exist
        :param option: Option whose corresponding value is needed
        :return: value of the provided option
        """
        sample_data_map = self.config_section_map(section)
        option_value = sample_data_map[option]
        return option_value

    def test_method(self):
        value = SampleDataReader.get_sample_data(self,'Question_1','text')
        print(value)


#sd = SampleDataReader(filename="test_data.ini")
#sd.sample_data_read()
#sd.test_method()
