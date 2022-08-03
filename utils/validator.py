from class_document import Document
from random import randint


class Validator(Document):
    def __init__(self, choice) -> None:
        super().__init__(choice)
         
    def document_validator(self):
        try:
            if len(self._document) == 11:
                sum_first_checker = 0
                multiply = [10, 9, 8, 7, 6, 5, 4, 3, 2]

                for index, digit in enumerate(self._document[0:9]):
                    result = int(self._document[index]) * multiply[index]
                    sum_first_checker += result
                    
                rest_first_checker = sum_first_checker % 11
                first_checker = 11 - rest_first_checker

                if first_checker >= 10:
                    first_checker = 0
                    
                sum_second_checker = 0
                multiply_2 = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2]
                    
                for index, digit in enumerate(self._document[0:10]):
                    result = int(self._document[index]) * multiply_2[index]
                    sum_second_checker += result
                    
                rest_second_checker = sum_second_checker % 11
                second_checker = 11 - rest_second_checker

                if second_checker >= 10:
                    second_checker = 0
                if str(first_checker) == self._document[9] and str(second_checker) == self._document[10]:
                    return True
                else:
                    return False

            elif len(self._document) == 14:
                sum_first_checker = 0
                multiply = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]

                for index, digit in enumerate(self._document[:12]):
                    result = int(self._document[index]) * multiply[index]
                    sum_first_checker += result
                
                rest_first_checker = sum_first_checker % 11

                if rest_first_checker < 2:
                    first_checker = 0
                else:
                    first_checker = 11 - rest_first_checker
                
                sum_second_checker = 0
                multiply_2 = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]

                for index, digit in enumerate(self._document[:13]):
                    result = int(self._document[index]) * multiply_2[index]
                    sum_second_checker += result
                
                rest_second_checker = sum_second_checker % 11

                if rest_second_checker < 2:
                    second_checker = 0
                else:
                    second_checker = 11 - rest_second_checker
                if int(self._document[12]) == first_checker and int(self._document[13]) == second_checker:
                    return True
                else:
                    return False
                

        except AttributeError:
            pass

        