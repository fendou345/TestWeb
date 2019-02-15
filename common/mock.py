
import string, random


class SetRandom(object):

    def __init__(self):
        pass

    # 随机生成手机号码
    def createPhone(self):
        prelist = ["130", "131", "132", "133", "134", "135", "136", "137", "138", "139", "150", "151", "152",
                   "153", "155", "156", "157", "158", "159", "186", "187", "188"]
        return random.choice(prelist) + "".join(random.choice("0123456789") for i in range(8))

    # 随机生成邮箱
    def createEmail(self):
        choice = "".join(random.sample(string.ascii_lowercase + string.digits, random.randint(3, 8)))
        return choice + "@qq.com"

    # 随机生成用户名
    def createUser(self):
        name = "".join(random.sample(string.ascii_letters + string.digits, random.randint(3, 5)))
        return name

    #随机生成网址
    def createUrl(self):
        name = "".join(random.sample(string.ascii_letters + string.digits, random.randint(3, 5)))
        url = "http://" + name + ".com"
        return url


