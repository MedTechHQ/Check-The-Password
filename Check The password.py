import re 
 
def check_password_strength(password) :
   if len(password) < 8:
     return "Weak: Password should be at least 8 characters long. "
   if not re.search(r"\d", password ) :
      return "Weak!: Add at least one number. "
   if not re.search(r"[A-Z]" , password):
      return "Medium: Add at least one uppercase letter."
   if not re.search(r"[@#%ù§$]" , password):
      return "Medium: Add at least one special character (@,#,%,ù,§,$)."
   return('Strong Password!')

password = input('Enter your password: ')
print(check_password_strength(password))     