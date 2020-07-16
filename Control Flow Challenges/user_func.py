## Function defined with one required and one optional parameter
def create_user(user_name, is_admin=False):
    create_email(user_name)
    set_permissions(is_admin)

# Calling with two arguments uses the default value for is_admin
user1 =create_user('johnny_thunder', True)
user2 = create_user('djohansen')



# We can make all three parameters optional
def create_user(username=None, is_admin=False):
  if username is None:
    username = "Guest"
  else:
    create_email(username)
  set_permissions(is_admin)

# So we can call with just one value
user3 = create_user('ssylvain')
# Or no value at all, which would create a Guest user
user4 = create_user()
