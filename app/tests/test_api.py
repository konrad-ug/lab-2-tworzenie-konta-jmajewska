import requests
import unittest
from ..Konto import Konto

class TestApi(unittest.TestCase):
    body = {
      "imie": "Julia",
      "nazwisko": "Majewska",
      "pesel" : "12345678999"
    }

    updateBody = {
      "imie": "Maja",
      "nazwisko": "Juliewska"
    }

    URL = "http://127.0.0.1:5000"

    def test_1_create_account(self):
      response = requests.post(f"{self.URL}/konta/stworz_konto", json=self.body)
      self.assertEqual(response.status_code, 201)

    def test_2_create_account_with_used_pesel(self):
      response = requests.post(f"{self.URL}/konta/stworz_konto", json=self.body)
      self.assertEqual(response.status_code, 400)

    def test_3_find_existing_account(self):
      response = requests.get(f"{self.URL}/konta/konto/{self.body['pesel']}")
      self.assertEqual(response.status_code, 200)

    def test_4_find_not_existing_account(self):
      response = requests.get(f"{self.URL}/konta/konto/12345678987")
      self.assertEqual(response.status_code, 404)

    def test_5_update_account(self):
      response = requests.put(f"{self.URL}/konta/konto/zmien_konto/{self.body['pesel']}", json=self.updateBody)
      self.assertEqual(response.status_code, 201)

    def test_6_update_not_existing_account(self):
      response = requests.put(f"{self.URL}/konta/konto/zmien_konto/12345678987",json=self.updateBody)
      self.assertEqual(response.status_code, 404)

    def test_7_account_count(self):
      response = requests.get(f"{self.URL}/konta/ile_kont")
      self.assertEqual(response.status_code, 200)

    def test_8_delete_account(self):
      response = requests.delete(f"{self.URL}/konta/usun_konto/{self.body['pesel']}")
      self.assertEqual(response.status_code, 204)
    
    def test_9_delete_non_existing_account(self):
      response = requests.delete(f"{self.URL}/konta/usun_konto/1234567898")
      self.assertEqual(response.status_code, 404)