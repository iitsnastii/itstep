import requests
help(requests)
import sys
import requests

print(sys.executable)
print(sys.version)
print(sys.platform)
print(sys.argv)
# modules
for module_name, module_path in sys.modules.items():
    print(module_name, module_path)


class BuildingEror(Exception):
    def __str__(self):
        return f"With so much material the house cannot be built!"
def check_material(amount_of_material, limit_value):
    if amount_of_material > limit_value:
        return "enough material"
    else:
        raise BuildingEror(amount_of_material)
materials = 301
check_material(materials, 300)






try:
    numerator = int(input("Введіть чисельник: "))
    denominator = int(input("Введіть знаменник: "))
    result = numerator / denominator
    print("Результат:", result)
except ZeroDivisionError:
    print("Помилка: Ділити на нуль не можна.")
except ValueError:
    print("Помилка: Введені дані не є числом.")

