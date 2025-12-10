import unittest
import os
from details import * 


class TestClientProgram(unittest.TestCase):
    def test_initial_clients_exist(self):
        self.assertIn("Sibusiso".clients)
        self.assertIn("Khaya".clients)
        underage_names = [name for name, info in underage_file]
        adult_names = [name for name, info in adult_file]

       
        self.assertIn("Khaya", underage_names)
        self.assertIn("Jada", underage_names)

        
        self.assertIn("Sibahle", adult_names)
        self.assertIn("Sisipho", adult_names)


    def test_ex_clients(self):
        ex_names = [name for name, info in ex_clients]

        self.assertIn("Khaya", ex_names)
        self.assertNotIn(("Khaya", clients["Khaya"]),underage_file)
        self.assertNotIn(("Khaya", clients["Khaya"]),adult_file)

    def test_client_file_written(self):
        self.assertTrue(os.path.exists("clients.txt"))

        with open("clients.txt", "r") as f:
            text = f.read()

        self.assertIn("Name: Sibusiso", text)
        self.assertIn("Join date:", text)

if __name__ == "__main__":
    unittest.main()
