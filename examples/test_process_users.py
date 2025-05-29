import json
import os
import unittest

from process_users import get_users, get_name_age


class GetUsersTestCase(unittest.TestCase):
    users = [
        {
            "email": "martha.foster@example.com",
            "age": 42
        },
        {
            "first_name": "Arthur",
            "last_name": "Fox",
            "age": 34
        },
        {
            "name": "Josh Kennedy",
            "age": 32
        },
    ]

    @classmethod
    def setUpClass(cls):
        # Arrange
        with open("users.json", "w") as f:
            json.dump(cls.users, f)
        with open("users.txt", "w") as f:
            f.write("test")

    @classmethod
    def tearDownClass(cls):
        os.remove("users.json")
        os.remove("users.txt")

    def test_nonexistent_file(self):
        result = get_users("nonexistent.txt")
        self.assertIsInstance(result, list)
        self.assertEqual(0, len(result))

    def test_invalid_json_file(self):
        # Act & Assert
        # self.assertRaises(json.JSONDecodeError, get_users, "users.txt")
        with self.assertRaises(json.JSONDecodeError):
            get_users("users.txt")

    def test_valid_json_file(self):
        # Act
        result = get_users("users.json")

        # Assert
        self.assertIsInstance(result, list)
        self.assertEqual(3, len(result))
        self.assertListEqual(self.users, result)

    def test_valid_json_file_with_filtering(self):
        # Act
        result = get_users("users.json", age_min=32, age_max=40)

        # Assert
        self.assertIsInstance(result, list)
        self.assertEqual(1, len(result))
        self.assertDictEqual({
                "first_name": "Arthur",
                "last_name": "Fox",
                "age": 34
            }, result[0])


class GetNameAgeTestCase(unittest.TestCase):
    def test_no_name(self):
        # Arrange
        user = {"age": 20}

        # Act & Assert
        with self.assertRaises(ValueError):
            get_name_age(user)

    def test_user_has_name(self):
        users = [
            {"name": "Jane", "age": 20},
            {"first_name": "Anna", "last_name": "Smith", "age": 40},
        ]
        expected_results = [
            ("Jane", 20),
            ("Anna Smith", 40),
        ]

        for user, expected_result in zip(users, expected_results):
            with self.subTest(f"Test failed for user = {user}"):
                result = get_name_age(user)
                self.assertEqual(result, expected_result)
