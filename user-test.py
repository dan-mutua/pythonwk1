import unittest
from user import User


class TestUser(unittest.TestCase):
    def setUp(self):
        """
        Setup method for the test class to create a new user
        """
        self.new_user = User("wilson", "kinyua",
                             "developerwilson", "pass21")

    def test_user_created(self):
        """
        Test to check if the user object is created
        """
        self.assertEqual(self.new_user.first_name, "wilson")
        self.assertEqual(self.new_user.last_name, "kinyua")
        self.assertEqual(self.new_user.username, "developerwilson")
        self.assertEqual(self.new_user.password, "pass21")

    def test_user_save(self):
        """
        check whether the user object is saved to the user accounts list
        """
        self.assertEqual(len(User.user_accounts), 0)
        self.new_user.save_user()
        self.assertEqual(len(User.user_accounts), 1)

    def test_delete_user(self):
        """
        check whether the user was removed from the user accounts list
        """
        self.assertEqual(len(User.user_accounts), 0)
        self.new_user.save_user()
        self.assertEqual(len(User.user_accounts), 1)
        self.new_user.delete_user()
        self.assertEqual(len(User.user_accounts), 0)

    def test_find_user(self):
        """
        check whether the user account exists in the user accounts list
        """
        self.found_user = User.find_user("developerwilson")

    def test_user_exists(self):
        """
        check whether the user account exists in the user accounts list
        """
        self.found_user = User.user_exist("developerwilson")


if __name__ == '__main__':
    unittest.main()