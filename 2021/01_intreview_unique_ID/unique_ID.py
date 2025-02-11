"""
Note that from 48 to 122 we have the numbers and letters
So ... I have to generate numbers between that values
However, there are some characteres like &*$... that need to be excluded

draw a number (bettween 48 to 122)
n = random range (48,122 + 1)

# After that, I need to change the number to its respective 
characters using chr(n)
"""

from random import randrange
class UniqueID():
    """
    Generate a Unique ID
    - You can choose the length
    - You can choose if have number or not
    - You can choose if have uppercase or lowercase characters
    """

    #-----------------excluded characteres--------------------
    excluded_chars = ",.~;:*^`\"%+-'?!@#$%¨&()-_+={[}]><\/"
    excluded_numbers = "0123456789"
    #---------------------------------------------------------



    def __init__(self,length, numbers, upper_lower='both'):
        """
        Constrctor Arguments:
        :length: - defines length of unique ID.
        :numbers: - defines if you wanna excluded the numbers (True/False).
        :upper_lower: define the character lower or upper ("both","upper","lower")
        """
        self.length = length
        self.numbers = numbers # True or False
        self.upper_lower = upper_lower

    

    def get_random_number(self):
        """
        Method returns random number between 48 - 122
        """
        return randrange(48,122+1)

    
    
    def generate_id(self):
        """
        Method generates unique ID.
        """
        unique_id = ""

        while len(unique_id) < self.length:

            characteres = chr(self.get_random_number())

            if self.numbers:
                if characteres not in self.excluded_chars:
                    if self.upper_lower == 'both':
                        unique_id += characteres
                    elif self.upper_lower == 'upper':
                        unique_id += characteres.upper()
                    elif self.upper_lower == 'lower':
                        unique_id += characteres.lower()

            else:
                if characteres not in self.excluded_chars and characteres not in self.excluded_numbers:
                    if self.upper_lower == 'both':
                        unique_id += characteres
                    elif self.upper_lower == 'upper':
                        unique_id += characteres.upper()
                    elif self.upper_lower == 'lower':
                        unique_id += characteres.lower()
            

        return unique_id

# Function to call my class and construct my object
def get_unique_id(length_id, numbers_id, upper_lower_id):
    """
    Function returns unique ID.
    """
    unique_id = UniqueID(length=length_id, numbers=numbers_id, upper_lower = upper_lower_id)

    return unique_id.generate_id()


# Testing
print(get_unique_id(length_id = 100,numbers_id = True, upper_lower_id='lower'))
