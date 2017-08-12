### Python 单例模式
```
class Singleton:
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super().__new__(cls)
        return cls.instance


if __name__ == '__main__':
    a = Singleton()
    b = Singleton()
    print(id(a))
    print(id(b))
```
