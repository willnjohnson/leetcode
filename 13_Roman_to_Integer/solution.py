class Solution:
    def romanToInt(self, s: str) -> int:
        # Dictionary to store the Roman numeral values
        #   Note: for edge-case values such as 4, 9, etc., need to subtract
        dict_roman_to_int = {
            'I': 1, 
            'V': 5, 
            'X': 10, 
            'L': 50,
            'C': 100, 
            'D': 500, 
            'M': 1000
        }
        
        # Variable to store the total value
        value = 0
        
        # Loop through string, except last character
        for i in range(len(s) - 1):
            # If current numeral is smaller than next one, subtract it
            if dict_roman_to_int[s[i]] < dict_roman_to_int[s[i + 1]]:
                value -= dict_roman_to_int[s[i]]
            else:
                value += dict_roman_to_int[s[i]]
        
        # Add value of last character (no need to check next character)
        value += dict_roman_to_int[s[-1]]
        
        return value
