class Meta(type):
    def __init__(cls, *args, **kwargs):
        cls.attr = None
        super().__init__(*args, **kwargs)

    def __call__(cls, *args, **kwargs):
        if cls.attr is None:
            cls.attr = super().__call__(*args, **kwargs)
            return cls.attr
        else:
            return cls.attr


class My(metaclass=Meta):
    def __init__(self):
        pass


a = My()
b = My()
print(a is b)
