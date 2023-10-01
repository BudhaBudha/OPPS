import re


""" A  module for authenticating  user registraton info """

class Authenticate_user_registration_info():

          def __init__(self, reg_number:str, email: str, password:str, 
                        phone_number: str, first_name:str, second_name: str,
                        ):
                                    
                  
                   self.reg_number = reg_number
                   self.email = email
                   self.password = password
                   self.phone_number = phone_number
                   self.first_name = first_name
                   self.second_name = second_name

          """ a method to verify user phone number """
          def verify_user_registration_number(self)-> bool:
                  pattern = r'^\+254\d{9}$'
                  if re.match(pattern,self.phone_number ):
                         phone_number = "0"+self.phone_number[4:]
                         print(phone_number)
                         if re.match("^(07|01)\d{8}$", phone_number):
                                return True
                         
                         return False
                  
                  else:
                         return False
                  
          """ a method to verify user email"""
          def verify_user_registration_email(self)-> bool:
                 if re.match(r"[^@]+@[^@]+\.[^@]+", self.email):
                    return True
    
                 return False
          
          """ a method to verify user password """
          def verify_user_password(self)-> bool:
                if not len(self.password)< 6:
                      return True
                
                return False
       
