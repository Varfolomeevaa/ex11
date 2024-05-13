from solution_2 import Basket, Good


def main(bskt):
    flag = False
    while not flag:
        menu = ('1.Загружать данные о товарах из файла. \n'
                '2.Добавлять товар в корзину. \n'
                '3.Удалять товар из корзины. \n'
                '4.Просмотреть содержание корзины. \n')
        print(menu)

        try:
            answer = int(input('Ваш ответ: '))
            flag = True

        except:
            print('Ошибка!')
    if answer == 1:
        with open(bskt, encoding='utf-8') as f:
            lines = []
            for n in f:
                if n[-1] == '\n':
                    lines.append(Good(n[:-1]))
                else:
                    lines.append(Good(n))
            for i in lines:
                if i not in basket.all_goods:
                    basket.add_good(i)
            for i in basket.all_goods:
                if i not in lines:
                    basket.delete_good(i)

        ans = input('Хотите сделать что-то ещё? ')
        if ans.lower() == 'да':
            print()
            main(bskt)
    if answer == 2:
        good = input('Введите товар, который хотите добавить в корзину: ')
        with open(bskt, 'a', encoding='utf-8') as f:
            print(good, file=f)
        ans = input('Хотите сделать что-то ещё? ')
        if ans.lower() == 'да':
            print()
            main(bskt)
    if answer == 3:
        good = input('Введите товар, который хотите удалить из корзины: ')
        with open(bskt, encoding='utf-8') as f:
            lines = []
            for n in f:
                if n[-1] == '\n':
                    lines.append(n[:-1])
                else:
                    lines.append(n)
        try:
            ind = lines.index(good)
            with open(bskt, 'w', encoding='utf-8') as f:
                for i in range(len(lines)):
                    if i != ind:
                        print(lines[i], file=f)
        except:
            print('Такого товара нет в корзине!')

        ans = input('Хотите сделать что-то ещё? ')
        if ans.lower() == 'да':
            print()
            main(bskt)
    if answer == 4:
        print(basket)
        ans = input('Хотите сделать что-то ещё? ')
        if ans.lower() == 'да':
            print()
            main(bskt)
    else:
        print('Ошибка!')
        main(bskt)


basket = Basket()
print('Здравствуйте, что хотите сделать?')
main('bskt_3.txt', )
