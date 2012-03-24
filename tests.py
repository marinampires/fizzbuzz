import unittest

from fizzbuzz import *

class TestFizzBuzz(unittest.TestCase):

  def test_deve_retornar_um_quando_numero_for_um(self):
    retorno = fizz_buzz(1)
    self.assertEqual(1, retorno)

  def test_deve_retornar_dois_quando_for_numero_dois(self):
    dois = fizz_buzz(2)
    self.assertEqual(2, dois)

  def test_deve_retornar_fizz_quando_for_numero_tres(self):
    fizz = fizz_buzz(3)
    self.assertEqual('fizz',fizz)

  def test_deve_retornar_fizz_quando_numero_for_seis(self):
    self.assertEqual('fizz', fizz_buzz(6))

  def test_deve_retornar_fizz_quando_numero_for_nove(self):
    self.assertEqual('fizz', fizz_buzz(9))

  def test_deve_retornar_buzz_quando_numero_for_cinco(self):
    self.assertEqual('buzz', fizz_buzz(5))

  def test_deve_retonar_buzz_quando_numero_for_dez(self):
    self.assertEqual('buzz', fizz_buzz(10))

  def test_deve_retornar_fizzbuzz_quando_numero_for_15(self):
    self.assertEqual('fizzbuzz', fizz_buzz(15))

  def test_deve_retornar_fizzbuzz_quando_numero_for_30(self):
    self.assertEqual('fizzbuzz', fizz_buzz(30))

if __name__ == '__main__':
  unittest.main()
