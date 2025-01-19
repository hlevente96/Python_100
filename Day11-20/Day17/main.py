class User:
    def __init__(self, user_id, username, follower = 0, following=0):
        self.id = user_id
        self.username = username
        self.followers = follower
        self.following = following

    def follow(self, user):
        user.followers += 1
        self.following += 1

user_1 = User("001","Levi",10)
user_2 = User("002","Vanda",100)

user_1.follow(user_2)
print(user_2.followers)
