#example
# def isEven(value):
#    return value % 2 == 0

'''
+ всего одно действие
+ понятный

- нет защиты от неправильных типов
- неправильно определяет дробные числа
'''

# my version
def isEven_new(value):
    
    allowedTypes = [int, float]
    valueType = type(value)
    typeIsOkay = False
    
    for _type in allowedTypes:
        if (_type == valueType):
            typeIsOkay = True
            currentType = _type
            break

    if (typeIsOkay):
        if (currentType == int):
            return (value & 1) == 0
        elif (currentType == float):
            while ((value % 1.0) != 0.0):
                value = value * 10.0
            return (int(value) & 1) == 0
    else:
        return "isEven_new ERROR! Wrong value type!"


'''
+ защита от ввода некорректных данных
+ работает со всеми numeric типами
+ легорасширяемая функция: достаточно добавить допустимый тип в список и ветку elif для выполнения соответсвующих действий

- использование циклов сильно повышает сложность алгоритма относительно исходного
- более высокая сложность восприятия функции относительно исходной
'''

