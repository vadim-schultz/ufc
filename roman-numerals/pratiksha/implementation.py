from abc import ABC, abstractmethod


class RomanConversionStrategy(ABC):
    @abstractmethod
    def convert(self, value):
        pass


class IntegerToRomanStrategy(RomanConversionStrategy):
    SYMBOLS = [
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
        ("I", 1),
    ]

    def convert(self, number):
        if not isinstance(number, int) or number < 1 or number > 3000:
            raise ValueError("Number must be an integer between 1 and 3000.")
        
        result = ""
        for symbol, value in self.SYMBOLS:
            while number >= value:
                result += symbol
                number -= value
        return result


class RomanToIntegerStrategy(RomanConversionStrategy):
    SYMBOL_MAP = {
        "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000
    }

    def convert(self, roman):
        if not isinstance(roman, str) or not roman:
            raise ValueError("Invalid Roman numeral string.")
        
        RomanConverter.validate_roman(roman)

        total = 0
        prev_value = 0
        for char in reversed(roman):
            value = RomanConverter.SYMBOL_MAP[char]  
            if value < prev_value:
                total -= value
            else:
                total += value
            prev_value = value
        return total


class RomanConverter:
    SYMBOL_MAP = RomanToIntegerStrategy.SYMBOL_MAP  

    def __init__(self, strategy: RomanConversionStrategy):
        self.strategy = strategy

    def convert(self, value):
        return self.strategy.convert(value)

    @staticmethod
    def validate_roman(roman):
        """Validate Roman numeral based on established rules."""
        RomanConverter.check_characters(roman)
        RomanConverter.check_repetitions(roman)
        RomanConverter.check_subtraction_rules(roman)
        RomanConverter.check_max_value(roman)

    @staticmethod
    def check_max_value(roman):
        """Ensure the total value of the Roman numeral does not exceed 3000."""
        total = 0
        prev_value = 0
        for char in reversed(roman):
            value = RomanConverter.SYMBOL_MAP[char]
            if value < prev_value:
                total -= value
            else:
                total += value
            prev_value = value

        if total > 3000:
            raise ValueError(f"Roman numeral {roman} represents a value greater than 3000.")


    @staticmethod
    def check_characters(roman):
        """Ensure all characters are valid Roman numeral symbols."""
        valid_symbols = RomanConverter.SYMBOL_MAP.keys()
        for char in roman:
            if char not in valid_symbols:
                raise ValueError(f"Invalid character: {char}")

    @staticmethod
    def check_repetitions(roman):
        """Check for invalid repetitions of Roman numeral symbols."""
        prev_char = None
        count_repeats = 0

        for char in roman:
            if char == prev_char:
                count_repeats += 1
                if count_repeats > 2 and char in "IXCM":
                    raise ValueError(f"Too many repeats of {char}.")
                elif count_repeats > 0 and char in "VLD":
                    raise ValueError(f"Invalid repetition of {char}.")
            else:
                count_repeats = 0
            prev_char = char

    @staticmethod
    def check_subtraction_rules(roman):
        """Ensure Roman numeral follows valid subtraction patterns."""
        for i in range(len(roman) - 1):
            current = roman[i]
            next_char = roman[i + 1]

            if RomanConverter.SYMBOL_MAP[current] < RomanConverter.SYMBOL_MAP[next_char]:
                if not RomanConverter.is_valid_subtraction(current, next_char):
                    raise ValueError(f"Invalid subtraction: {current}{next_char}.")

    @staticmethod
    def is_valid_subtraction(prev, current):
        """Checks if a subtraction like 'IX' or 'XC' is valid."""
        valid_subtractions = {
            "I": ["V", "X"],
            "X": ["L", "C"],
            "C": ["D", "M"],
        }
        return prev in valid_subtractions and current in valid_subtractions[prev]


class RomanConverterFactory:
    @staticmethod
    def get_converter(conversion_type):
        if conversion_type == "to_roman":
            return RomanConverter(IntegerToRomanStrategy())
        elif conversion_type == "from_roman":
            return RomanConverter(RomanToIntegerStrategy())
        else:
            raise ValueError(f"Unknown conversion type: {conversion_type}")


def to_roman(integer):
    converter = RomanConverterFactory.get_converter("to_roman")
    return converter.convert(integer)


def from_roman(roman):
    converter = RomanConverterFactory.get_converter("from_roman")
    return converter.convert(roman)
