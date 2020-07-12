class UserGroup:
  def __init__(self, users, permissions):
    self.user_list = users
    self.permissions = permissions

  def __iter__(self):
    return iter(self.user_list)

  def __len__(self):
    return len(self.user_list)

  def __contains__(self, user):
    return user in self.user_list


class User:
    def __init__(self, user_name):
        self.user_name = user_name

Dianna = User('Dianna')
Frank = User('Frank')
Jenn = User('Jenn')

can_edit = UserGroup([Dianna, Frank], {'can edit pag':True})
can_delet = UserGroup([Dianna, Jenn], {'can delete posts': True})

print(len(can_edit))

