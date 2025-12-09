# TODO Найдите количество книг, которое можно разместить на дискете
disceta_syze_Mb = 1.44
book_list = 100
list_strok = 50
stroka_simv = 25
simv_b = 4

book_syze_Mb = simv_b * stroka_simv * list_strok * book_list / (1024 ** 2)

count_book = int(disceta_syze_Mb // book_syze_Mb)
print("Количество книг, помещающихся на дискету:", count_book)
