import time


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = int(age)

    def __eq__(self, other):
        return self.nickname == other


class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = int(duration)
        self.time_now = int(time_now)
        self.adult_mode = bool(adult_mode)

    def __eq__(self, other):
        return self.title == other


class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        for i in self.users:
            if i.nickname == nickname and i.password == hash(password):
                self.current_user = nickname

    def register(self, nickname, password, age):
        k = False
        for user in self.users:
            if user.nickname == nickname:
                print(f"Пользователь {nickname} уже существует")
                k = True
                break
            else:
                k = False
        if k == False:
            new_user = User(nickname, password, age)
            self.users.append(new_user)
            self.current_user = new_user.nickname

    def log_out(self):
        self.current_user = None

    def add(self, *args):
        for video in args:
            k = False
            for i in range(len(self.videos)):
                if self.videos[i] == video:
                    k = True
                    break
                else:
                    k = False
            if k == False:
                self.videos.append(video)

    def get_videos(self, query):
        get = []
        query = query.lower()
        video_ = ""
        for video in self.videos:
            video_ = video.title.lower()
            if video_.count(query) > 0:
                get.append(video.title)
        return get

    def watch_video(self, search):
        if self.current_user == None:
            return print("Войдите в аккаунт, чтобы смотреть видео")
        age = 0
        for user in self.users:
            if user.nickname == self.current_user:
                age = user.age
        for video in self.videos:
            if video.title == search:
                if video.adult_mode == True and age <= 18:
                    return print("Вам нет 18 лет, пожалуйста покиньте страницу")
                else:
                    for second in range(1, video.duration + 1):
                        print(second, end=' ')
                        time.sleep(1)
                    print("Конец видео")


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
