import re

barcode_count = int(input())

barcode_pattern = r"@#+([A-Z][A-Za-z0-9]{4,}[A-Z])@#+"
digit_pattern = r'\d'

for i in range(barcode_count):
    current_barcode = input()
    is_valid = re.fullmatch(barcode_pattern, current_barcode)
    if is_valid:
        digits = re.findall(digit_pattern, current_barcode)
        if digits:
            print(f"Product group: {''.join(digits)}")
        else:
            print("Product group: 00")
    else:
        print('Invalid barcode')
