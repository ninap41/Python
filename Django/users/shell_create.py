from apps.user_login.models import User
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

# use this function to create users with validations
def create_valid_user():

    user = {}
    print "Enter a First Name"
    user['first_name'] = raw_input()

    print "Enter a Last Name"
    user['last_name'] = raw_input()

    print "Enter an Email Address"
    user['email'] = raw_input()

    print "Enter an Age"
    user['age'] = raw_input()