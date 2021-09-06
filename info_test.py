import unittest
from info import info 

class TestCredentials(unittest.TestCase):
    
    def setUp(self):
        """
        setup method to run each Testcase
        """
        self.new_credentials=info("gmail","kinuthia@gmail.com","abc123")
        
    def test_init(self): 
        """
        test if object is initialized well
        """ 
        self.assertEqual(self.new_credentials.account,"gmail")
        self.assertEqual(self.new_credentials.username,"kinuthia@gmail.com") 
        self.assertEqual(self.new_credentials.password,"abc123") 
        
    def test_save_credentials(self):
        """
        test whether credentials are saved in the credentials_list
        """ 
        self.new_credentials.save_credentials()
        self.assertEqual(len(info.credentials_list),1)
        
    def tearDown(self): 
        """
        clears up after every test is done
        """ 
        info.credentials_list=[] 
        
    def test_multiple_credentials(self):
        """
        tests whether we can save multiple credentials in the credentials list
        """
        self.new_credentials.save_credentials()
        test_credentials=info("gmail","jogu@gmail","cdf123")
        test_credentials.save_credentials()
        self.assertEqual(len(info.credentials_list),2)
        
    def  test_delete_credentials(self):
        """
        tests whether credentials can be removed from the credentials_list
        """ 
        self.assertEqual(len(info.credentials_list),0)  
        self.new_credentials.save_credentials()
        self.assertEqual(len(info.credentials_list),1)
        self.new_credentials.delete_credentials() 
        
    def  test_find_by_account(self): 
        """
        tests whether a user can find account using account name
        """
        self.new_credentials.save_credentials()
        test_credentials = info("gmail","jogu@gmail.com","cdf123") # new credentials 
        test_credentials.save_credentials() 
        
        found_credentials=info.find_by_acc("account")
       
        
    def  test_display_credentials(self):
        """
        method that displays all credentials saved by the user
        """  
        self.assertEqual(info.display_credentials(),info.credentials_list) 
        
        
        
if __name__ == '__main__':
    unittest.main()                           
