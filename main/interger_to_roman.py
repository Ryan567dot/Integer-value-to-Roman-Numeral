class int_to_roman:
    def int_to_Roman(self, number):
        value = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,1]
        syllable = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"]
        roman_num = ""
        i = 0
        
        while  num > 0:
            for a in range(num // value[i]):
                roman_num += syllable[i]
                num -= value[i]
            i += 1
        return roman_num


print(int_to_roman().int_to_Roman(1))
print(int_to_roman().int_to_Roman(4000))