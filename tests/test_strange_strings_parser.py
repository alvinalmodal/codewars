import unittest
from src.strange_strings_parser import word_splitter


class TestStrangeStringsParser(unittest.TestCase):
    def test_word_splitter(self):
        #self.assertEqual(["12","56C","144","1000","1200"] , word_splitter("12:56C:144:1000:1200"))
        #self.assertEqual(["340000.00","-140.49902","ELEVATION","24000000","END"] , word_splitter("340000.00*-140.49902*ELEVATION*24000000*END"))
        #self.assertEqual(['11', '11', '11', '11', '11'] , word_splitter("11:11:11:11:11"))
        #self.assertEqual(['CODE', 'SEVEN', 'FOURTY', 'THREE', 'HUNDRED'] , word_splitter("CODE*SEVEN|FOURTY#THREE&HUNDRED"))
        #self.assertEqual(['R320000R', '56', '.7200RPM.', '-MODE-', '65', 'LATCH', 'ON'] , word_splitter("R320000R;56:.7200RPM.#-MODE-%65>LATCH?ON"))
        self.assertEqual(['3sXICc58g287Js', 'teYfLI-Kwkzp', 'I--F3J', '7', 'LG6sfe', 'q3PC1MLgYOOfZ', 'XoGkEg-rT', 'Nn', 'Mx', 'kTV', 'IbHP5jNr68TA', 'R'] , 
                            word_splitter("3sXICc58g287Js:teYfLI-Kwkzp+I--F3J!7#LG6sfe%q3PC1MLgYOOfZ&XoGkEg-rT*Nn|Mx,kTV;IbHP5jNr68TA=R"))