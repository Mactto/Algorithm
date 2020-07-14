---
layout: post
title: "Python에서의 self"
subtitle: Python에서 self란 무엇일까?
categories: python
tags: python grammer self
comments: true

---
## self의 개념

python에서 self란 무엇일까?

python에서 메서드를 호출하거나 생성할 때 self라는 인스턴스 값이 맨 처음에 들어간다.
이 self는 클래스의 객체가 여러번 호출되었을 때 혼동을 주지 않기 위해 사용하는 인스턴스이다.

쉽게 말해, 아래와 같은 예를 들어 보겠다.

```python
class test:
    def func1(self):
        print("This is function1")

    def func2():
        print("This is function2")
```

위와 같이 test라는 클래스가 있고 메서드로 func1()과 func2()를 작성하였다.
이때 self를 이해하기 위해 func1()에만 self를 인자로 받게했다.

그 다음 아래와 같이 test 클래스의 객체를 생성하고 두 개의 메서드를 각각 호출해본다.



```python
t = test()
t.func1()
t.func2()
```

그러면 func1()의 내용은 정상적으로 출력되지만 func2()에서는 오류가 발생할 것이다.

    TypeError: func2(0 takes 0 positional arguments but 1 was given

오류의 내용을 살펴보면 func2에 변수가 하나 넘어갔지만 받지 못했다고 한다.
우리가 func2를 호출할 때 아무런 인수를 넘겨주지 않았는데 무언가가 하나 인수로 넘어갔다.

이를 이해하기 위해 먼저 생성한 test 객체의 id를 다음과 같이 출력해보자

```python
print(id(t))     # 객체의 이름이 t이기 때문에 t의 id를 출력한다.
```

그럼 일련의 숫자들이 출력될 것이다.
이 숫자들은 객체의 메모리 주소를 의미한다.

python에서는 C++ 등과 같은 다른 객체지향언어들과 달리
따로 네임스페이스를 지정해주지 않는다.

따라서 클래스의 객체를 생성할 때마다 각 객체에 위와 같이 id값을 부여하게 되고
이 id값이 바로 self인 것이다.

따라서 self를 넘겨주고 받는 이유는 어떤 클래스의 객체에서 호출했는지 구분해주기 위해서이다.
이를 구분하지 않는다면 한 클래스의 여러 객체를 생성했을 때 컴파일 시 컴파일러에게 혼동을 줄 것이다.
그러면 실제로 self에 넘어가는 값이 객체의 id값과 같은지 출력해보자

아래와 같이 func1()의 코드를 추가하고 출력해본다.

```python
class test:
    def func1(self):
        print(id(self))
        print("This is function1")

    def func2():
        print("This is function2")

t = test()
print(id(t))
t.func1()
```

위 코드의 출력결과는 객체 t의 id값과 func1()의 self의 값이 동일하다는 것을 증명해준다.

따라서 python에서는 어떤 객체의 메서드를 호출할 때 항상 그 객체의 id를 self라는 인스턴스로 넘겨주기 때문에
func2()를 호출했을 때 넘어간 self라는 인자를 받을 수 있는 변수가 없기 때문에 오류가 발생한 것이다.

여기까지 python에서의 self에 대한 포스팅이었다.
