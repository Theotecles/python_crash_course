from admin import Admin
from users import User

me = Admin('brian', 'mochtyak', 'cincinnati', 'us', 27)
me.privileges.show_privileges()

me = User('brian', 'mochtyak', 'covington', 'america', 27)
me.describe_user()
me.greet_user()

shauna = User('shauna', 'combs', 'cincinnati', 'america', 26)
shauna.describe_user()
shauna.greet_user()

me.increment_login_attempts()
me.increment_login_attempts()
me.increment_login_attempts()
me.increment_login_attempts()
me.increment_login_attempts()
me.increment_login_attempts()

print(me.login_attempts)
me.reset_login_attempts()
print(me.login_attempts)