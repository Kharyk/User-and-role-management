from lessonone import models

user_1 = models.User(name = "Alina",
                     email = 'email@gmail.com',
                     role = "admin")

user_1.save()

user = User.objects.filter(email="email@gmail.com").first()
user.email = 'whatever@gmail.com'
user.save()
print(user)