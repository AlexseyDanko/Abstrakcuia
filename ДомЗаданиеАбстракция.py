from abc import abstractmethod
class SocialClass:
    def __init__(self):
        pass
    @abstractmethod
    def to_eat(self):
        pass
    @abstractmethod
    def drink(self):
        pass
    @abstractmethod
    def sleep(self):
        pass
    @abstractmethod
    def work(self):
        pass
    @abstractmethod
    def earn_money(self):
        pass
    @abstractmethod
    def entertainments(self):
        pass
    @abstractmethod
    def life_expectancy(self):
        pass
    @abstractmethod
    def freedom_of_speech(self):
        pass
class The_impoverished(SocialClass):
    def __init__(self):
        pass
    def freedom_of_speech(self):
        print("имеет своё мнение, но кто его спрашивает")
    def to_eat(self):
        print("Питается чем придётся")
    def drink(self):
        print(" Пьёт всё ,не брезгует ничем")
    def sleep(self):
        print("Спит при любой возможности")
    def work(self):
        print("Работает на самом социальном дне")
    def earn_money(self):
        print("Деньги для него, не являеться инструментом для улучшения своего уровня жизни")
    def entertainments(self):
        print("Любимое развлечение гонять голубей и смотреть на огонь")
    def life_expectancy(self):
        print("Продолжительность его жизни предугадать невозможно, это как русская рулетка")
class The_working(SocialClass):
    def __init__(self):
        pass
    def freedom_of_speech(self):
        print("Имеет своё мнение, но оно навязано социумом")
    def to_eat(self):
        print("Питается продуктами низгого качества")
    def drink(self):
        print("Часто выпивает алкогольные напитки, принебрегает водой")
    def sleep(self):
        print("Режим сна нарушен, пытается его соблюдать, но для него это слишком сложно")
    def work(self):
        print("Имеет работу низкого социального уровня")
    def earn_money(self):
        print("Денег зарабатывает только на еду и коммуналку")
    def entertainments(self):
        print("Развлечение это бабушкин домик")
    def life_expectancy(self):
        print("Продолжительность его жизни, находиться в самой низкой точке социума")
class The_middle(SocialClass):
    def __init__(self):
        pass
    def freedom_of_speech(self):
        print("Имеет своё собственное мнение, но стараеться быть осторожным с выражениями")
    def to_eat(self):
        print("Питается продуктами среднего качества, иногда себя радует ПП")
    def drink(self):
        print("Пьёт воду и другие напитки, алкоголь по праздникам ")
    def sleep(self):
        print("Режим сна есть, но иногда страдает от нервов")
    def work(self):
        print("Имеет приличную работу, социальный уровень уверенности достаточно высок")
    def earn_money(self):
        print("Работа хоть и приличная, но на ней не заработаешь")
    def entertainments(self):
        print("Может позволить себе море раз в год, при условии отсутствия детей, либо порвёт жоп...но свозит и детей")
    def death(self):
        print("Продолжительность его жизни,почти соответствует статистике")
class The_top(SocialClass):
    def __init__(self):
        pass
    def freedom_of_speech(self):
        print("Его мнение распространяется на классы ниже его")
    def to_eat(self):
        print("Питается правильно, следит за диетой")
    def drink(self):
        print("Пьёт только качественную воду и другие напитки")
    def sleep(self):
        print("Режим сна подобран индивидуально и идеально для его организма")
    def work(self):
        print("Работа это не способ разбогатеть, а метод поулчения власти")
    def earn_money(self):
        print("После первого миллиона $ считает его деньги, личный финансист")
    def entertainments(self):
        print("Ему доступны любые развлечения этого продажного мира")
    def death(self):
        print("В погоне за лишним годом жизни, может себе купить и новые сердца и другие органы ")

