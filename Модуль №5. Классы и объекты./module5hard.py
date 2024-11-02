class Video:
    def __init__(self, title, duration, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode

    def __str__(self):
        return self.title

    def __repr__(self):
        return self.title



class UrTube:
    def __init__(self):
        self.current_user = None
        self.users = []
        self.videos = []

    def register(self, nickname, password, age):
        new_user = User(nickname, password, age)
        if new_user not in self.users:
            self.users.append(new_user)
            self.current_user = new_user
        else:
            print(f"Пользователь {nickname} уже существует")

    def log_in(self, nickname, password):
        for user in self.users:
            if (nickname, hash(password)) == user.temp():
                self.current_user = user

    def log_out(self):
        self.current_user = None

    def add(self, *args:Video):
        for video in args:
            if video not in self.videos:
                self.videos.append(video)

    def get_videos(self, search):
        search_list = []
        for video in self.videos:
            if search.lower() in video.title.lower():
                search_list.append(video)
        return search_list

    def watch_video(self, title):
        for video in self.videos:
            if title == video.title:
                while video.time_now < video.duration:
                    video.time_now += 1
                    print(video.time_now)
                video.time_now = 0
                print('Конец видео')




class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def temp(self):
        return self.nickname, self.password

    def __str__(self):
        return self.nickname


if __name__ == "__main__":
    # urtube_instance = UrTube()
    # user1 = User('insane', 'qwerty123', 23)
    # user2 = User('simple', 'qwerty456', 24)
    # user3 = User('complicated', 'qwerty789', 18)
    # user4 = User('easy', 'qwerty91011', 17)

    ur = UrTube()
    v1 = Video('Лучший язык программирования 2024 года', 200)
    v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

    # Добавление видео
    ur.add(v1, v2)

    # Проверка поиска
    print(ur.get_videos('лучший'))
    print(ur.get_videos('ПРОГ'))

    # Проверка на вход пользователя и возрастное ограничение
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('vasya_pupkin', 'lolkekcheburek', 13)
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
    ur.watch_video('Для чего девушкам парень программист?')

    # Проверка входа в другой аккаунт
    ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
    print(ur.current_user)

    # Попытка воспроизведения несуществующего видео
    ur.watch_video('Лучший язык программирования 2024 года!')
