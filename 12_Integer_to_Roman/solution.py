class Solution:
    def intToRoman(self, num: int) -> str:
        # Approach:
        #   Subtract largest values from num working down towards smaller values, appending each value
        #   since large-to-small == left-to-right appending order

        # Define list of tuples for Roman numerals (key) and correponding integer (value)
        roman_numeral_map = [
            ("M", 1000), 
            ("CM", 900), 
            ("D", 500), 
            ("CD", 400),
            ("C", 100), 
            ("XC", 90), 
            ("L", 50), 
            ("XL", 40),
            ("X", 10), 
            ("IX", 9), 
            ("V", 5), 
            ("IV", 4),
            ("I", 1)
        ]
        
        # List to store the Roman numeral components
        result = []
        
        # Iterate through the roman_numeral_map and subtract values from num
        for numeral_symbol, value in roman_numeral_map:
            while num >= value:
                result.append(numeral_symbol)  # Append the Roman symbol
                num -= value  # Subtract the corresponding value from num
        
        # Join all parts and return the Roman numeral string
        return ''.join(result)