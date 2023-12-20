'''
Задание:
На языке Python предложить алгоритм, который быстрее всего (по процессорным тикам) отсортирует данный ей массив чисел.
Массив может быть любого размера со случайным порядком чисел (в том числе и отсортированным).
Объяснить, почему вы считаете, что функция соответствует заданным критериям.
'''


'''
Ответ:
Учитывая, что на входной массив нет ограничений, лучшим алгоритмом будет Timsort,
в настоящий момент реализованный по-умолчанию для метода sort() в Python.
Данный алгоритм является гибридом, сочетающим в себе сортировку вставками и сортировку слияниями (достаточно быстрые виды сортировок),
а также включающий ряд дополнительных условий для оптимизации работы.




Обоснование:
Нет общего алгоритма, который ВСЕГДА будет работать быстрее.
Какие-то алгоритмы работают быстрее с отсортированными или околоотсортированными данными,
какие-то - с реальными данными из жизни, какие-то - с искусственными, полностью рандомными.

Нужно понимать, какие данный ожидаются в конкретном случае и для конкретного случая выбирать подходящую сортировку.

Гибридные алгоритмы можно считать своего рода усреднениями,
благодаря своей гибридности работающими не хуже и не медленнее, чем составные части этих алгоритмов по-отдельности.

Таким образом, для данного абстрактного задания в общем случае подойдёт алгоритм Timsort, он быстрый и стабильный,
в большинстве стандартных ситуаций он покажет себя с лучшей стороны
'''
