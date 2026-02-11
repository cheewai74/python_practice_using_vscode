import decimal

width = 8
precision = 3
value = decimal.Decimal("42.12345")
print(f"output: {value:{width}.{precision}}")
value = decimal.Decimal("142.12345")
print(f'Result: {value:{"4.2" if value < 100 else "8.3"}}')