def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")

    inner_function() #результат не выводится, т.к. функция находится в локальном пространстве test_function(),
    # иными словами, test_function() является объемлющей функцией для inner_function()
    # при этом, реализация inner_function() необходима, т.к. это влияет на функциональность test_function() - передаёт в неё print

#inner_function() - вывод не работает, т.к. функция находится в локальном пространстве test_function(), соответственно,
# не может вывести print из объемлющей области test_function(),
# выдаёт ошибку NameError: name 'inner_function' is not defined. Did you mean: 'test_function'?

test_function() #для работоспособности необходимо вывести "основную" заявленную функцию