from unittest import TestCase, main

def somar(x, y):
    return x + y

def subtrair(x, y):
    return x - y


class Teste(TestCase):

    def test_soma(self):
        self.assertEqual(somar(5, 5), 10)
        self.assertLess(somar(5, 5), 11)

    def teste_sub(self):
        self.assertEqual(subtrair(5, 5), 0)
        self.assertLessEqual(subtrair(15, 5), 10)

if __name__ == "__main__":
    main()