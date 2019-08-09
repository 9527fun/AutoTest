class Tools(object):
    count = 0

    @classmethod
    def show_tools_counts(cls):
        print("工具的数量%d" % cls.count)

    def __init__(self, name):
        self.name = name

        Tools.count += 1


tools = Tools("锤子")
tools = Tools("剪刀")
#  引用类方法是“类名.”即可
Tools.show_tools_counts()

