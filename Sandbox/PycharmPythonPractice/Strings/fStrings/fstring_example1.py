import datetime
today = datetime.datetime.today()
print(f"{today:%Y-%m-%d}")
print(f"{today:%Y}")

x =10
y = 25
print(f"x={x}, y={y}")
print(f"{x = }, {y = }")
print(f"{x = :.3f}")

# Nested F-Strings
number = 254.3463
print(f"{f'${number:.3f}':>10s}")

print(f"{(lambda x: x**2)(3)}")