class sexerror(Exception):
    def __init__(self,abc):
        self.abc=abc
    def __str__(self):
        return self.abc
boyschool=["男","男","女","男"]
for i in boyschool:
    if(i=="女"):
        raise sexerror("性别错误！")