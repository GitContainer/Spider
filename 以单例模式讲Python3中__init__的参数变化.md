### 以单例模式讲 Python3 中魔术方法 `__init__`的参数变化

### [TypeError: object() takes no parameters after defining __new__](https://stackoverflow.com/questions/34777773/typeerror-object-takes-no-parameters-after-defining-new)

>I really don't get where is the error in this little code :

```
#!/usr/bin/python3


class Personne:

def __init__(self, nom, prenom):
    print("Appel de la méthode __init__")
    self.nom = nom
    self.prenom = prenom

def __new__(cls, nom, prenom):
    print("Appel de la méthode __new__ de la classe {}".format(cls))
    return object.__new__(cls, nom, prenom)

personne = Personne("Doe", "John")
```

This code presented above is giving me the error :

```
Traceback (most recent call last):
File "/home/bilal/Lien vers python/21_meta_classes/1_instanciation.py", line 21, in <module>
personne = Personne("Doe", "John")
File "/home/bilal/Lien vers python/21_meta_classes/1_instanciation.py", line 14, in __new__
return object.__new__(cls, nom, prenom)
TypeError: object() takes no parameters
```

### 高票答案解释

In Python 3.3 and later, if you're overriding both `__new__` and `__init__`, you need to avoid passing any extra arguments to the `object` methods you're overriding. If you only override one of those methods, it's allowed to pass extra arguments to the other one (since that usually happens without your help).

So, to fix your class, change the `__new__` method like so:

```
def __new__(cls, nom, prenom):
    print("Appel de la méthode __new__ de la classe {}".format(cls))
    return object.__new__(cls) # don't pass extra arguments here!
```

The call to `__init__` isn't made by `object.__new__`, but rather by `type.__call__` (bound to the class object). So `object.__new__` doesn't need to see the same arguments that your `__init__`function expects

#### 翻译如下

从 Python 3.3 以后，如果覆写了 `__new__` 和 `__init__` ，你需要避免传递任何参数给所覆盖的 object 方法，如果你只是更改这些方法中的一个，允许传递参数给另外一个。

调用 `__init__` 不是通过`object.__new__ ` 生成，而是通过`type.__call__`，（绑定到类对象)，所以`object.__new__` 。所以`object.__new__` 不需要去看见`__init__` 函数期待的同样的参数。

渣翻，不过原文说的也挺够绕的。

暂时没完全理解，反正意思就是 `__new__` 中不要让`super().__new__(cls)` 接收另外的参数就是了。

正确的代码

```python
class Singleton(object):

    def __new__(cls, *args, **kwargs):
        print(args)
        print(kwargs)
        if not hasattr(cls, '__instance'):
            cls.__instance = super(
                Singleton, cls).__new__(cls)
        return cls.__instance

    def __init__(self, num):
        self.num = num


s1 = Singleton(2)
s2 = Singleton(3)
print(s1)
print(s2)
print(s1.num)
print(s2.num)
```
