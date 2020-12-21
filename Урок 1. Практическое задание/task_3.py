"""
Задание 3.

Для этой задачи:
1) придумайте 1-3 решения (желательно хотя бы два)
2) оцените сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему

Примечание:
Без выполнения пунктов 2 и 3 задание считается нерешенным. Пункты 2 и 3 можно выполнить
через строки документации в самом коде.
Если у вас возникают сложности, постарайтесь подумать как можно решить задачу,
а не писать "мы это не проходили)".
Алгоритмизатор должен развивать мышление, а это прежде всего практика.
А без столкновения со сложностями его не развить.


Сама задача:
Имеется хранилище с информацией о компаниях: название и годовая прибыль.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
Реализуйте поиск трех компаний с наибольшей годовой прибылью.
Выведите результат.
"""

company = {
    'Roga&Kopyta': 1000,
    'Romashka': 1150,
    'Solnyshko': 2000,
    'OOO': 1500,
    'Popov&Co': 1780,
    'Sova': 1250,
    'Tiger': 1850,
}


# Сложность: O(N)
def max_income_1(lst):
    max_company = {}
    lst_dict = dict(lst)
    for i in range(3):
        max_inc_comp = max(lst_dict.items(), key=lambda inc: inc[1])
        del lst_dict[max_inc_comp[0]]
        max_company[max_inc_comp[0]] = max_inc_comp[1]
    return max_company


print(max_income_1(company))

