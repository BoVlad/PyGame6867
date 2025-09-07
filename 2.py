# 1. Ви створюєте конвертер градусів Цельсія у градуси Фаренгейта.
# Напишіть функцію, яка використовує градуси Цельсія як аргумент та поверне відповідне значення у градусах Фаренгейта.
# Приклад даних 36, 50, 120 Приклад результату 96.8, 122, 248
# Оброби можливі помилки (опціонально)
#
# 2. Напишіть функцію, яка обчислює площу фігури на основі переданих параметрів.
# Функція повинна приймати назву фігури (круг, прямокутник, трикутник) та відповідні параметри. Використайте **kwargs
# Приклад вхідних даних: calculate_area(shape="круг", radius=5)
# Приклад виводу: Площа круга: 78.54 кв. од.
# Приклад вхідних даних: calculate_area(shape="прямокутник", width=4, height=6)
# Приклад виводу: Площа прямокутника: 24 кв. од.



def convert_temp(Celsia):
    return Celsia * 1.8 + 32

a = int(input())
print(convert_temp(a))

-----

def calculate_area(**kwargs):
    shape = kwargs.get("shape")
    if shape == "круг":
        radius = kwargs.get("first_param")
        Pi = 3.14
        return f"Площа прямокутника: {Pi * radius ** 2} кв. од."
    if shape == "прямокутник":
        width = kwargs.get("first_param")
        height = kwargs.get("second_param")
        return f"Площа прямокутника: {width * height} кв. од."
    if shape == "трикутник":
        base = kwargs.get("first_param")
        height = kwargs.get("second_param")
        return f"Площа трикутника: {(base * height) / 2} кв. од."
    else:
        return "Error missing arguments"

user_shape = input("Введіть фігуру (круг, прямокутник, трикутник): ")
user_first_param = int(input("Введіть перший параметр: "))
user_second_param = int(input("Введіть другий параметр: "))

print(calculate_area(shape=user_shape, first_param=user_first_param, second_param=user_second_param))




