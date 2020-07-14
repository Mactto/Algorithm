---
layout: post
title: "수치 미분 & 역전파 심층 신경망 학습 비교"
subtitle: 수치 미분을 이용한 신경망 학습과 역전파 알고리즘을 이용한 신경망 학습을 코드를 통해 비교한다.
categories: deeplearning
tags: python deeplearning forwardpropergation backpropergation
comments: true

---
# 수치 미분을 이용한 심층 신경망 학습
## Import Modules
```python
import time         # 시간 제어 라이브러리
import numpy as np  # numpy 라이브러리
```

## 유틸리티 함수
```python
epsilon = 0.0001

def _t(x):
    # 매개변수로 x 매트릭스 받아 transpose 해준다.
    return np.transpose(x)

def _m(A, B):
    # matmul = matrix multiplex -> 매트릭스 곱 연산 수행
    return np.matmul(A, B)

def sigmoid(x):
    # 활성함수 sigmoid 식을 명시해준다
    return 1 / (1 + np.exp(-x))

def mean_squared_error(h, y):
    return 1 / 2 * np.mean(np.square(h - y))
```

## Dense Layer 구현
```python
# Dense란 하나의 hidden layer를 의미한다
class Dense:
    # 객체 생성시 __init__을 호출하게 되고
    # __init__에서는 매개변수로 받은 것들을 모두 초기화 해준다.
    def __init__(self, W, b, a):
        self.W = W
        self.b = b
        self.a = a

        self.dW = np.zeros_like(self.W)
        self.db = np.zeros_like(self.b)

    def __call__(self, x):
        #
        return self.a(_m(_t(self.W), x) + self.b)
```

## 심층신경망 구현
```python
class DNN:
    # 인자로 히든 레이어의 갯수, 뉴런의 갯수, input&output 갯수, 활성함수(default=sigmoid)가 주어짐
    def __init__(self, hidden_depth, num_neuron, num_input, num_output, activation=sigmoid):
        # Weight(가중치)와 bias를 랜덤하게 초기화
        def init_var(i, o):
            return np.random.normal(0.0, 0.01, (i, o)), np.zeros((o,))

        # 전체 layer를 가질 sequence 리스트로 선언
        self.sequence = list()

        # First hidden layer
        W, b = init_var(num_input, num_neuron)
        self.sequence.append(Dense(W, b, activation))

        # Hidden layers
        for _ in range(hidden_depth - 1):
            W, b = init_var(num_neuron, num_neuron)
            self.sequence.append(Dense(W, b, activation))

        # Output layer
        W, b = init_var(num_neuron, num_output)
        self.sequence.append(Dense(W, b, activation))

    # 객체 호출 시 각
    def __call__(self, x):
        # 각 Dense의 __call__ 호출 -> 계산
        for layer in self.sequence:
            x = layer(x)
        return x

    # gradient 계산
    def calc_gradient(self, x, y, loss_func):
        # 새로운 sequence를 갱신해 반환
        def get_new_sequence(layer_index, new_layer):
            # 새로운 sequence 리스트 선언
            new_sequence = list()

            # enumerate는 돌고있는 인덱스를 반환
            for i, layer in enumerate(self.sequence):
                # 인덱스가 원하는 layer에 위치할 경우 새로운 sequence에 추가
                if i == layer_index:
                    new_sequence.append(new_layer)
                # 아닐 경우 그대로의 layer 새로운 sequence에 추가
                else:
                    new_sequence.append(layer)
            return new_sequence

        # 새로운 sequence 평가
        def eval_sequence(x, sequence):
            for layer in sequence:
                x = layer(x)
            return x

        # 기준이 될 loss 값
        loss = loss_func(self(x), y)

        # 모든 가중치 스칼라에 대해,
        # 모든 bias 스칼라에 대해 numerical gradient 계산
        for layer_id, layer in enumerate(self.sequence):
            for w_i, w in enumerate(layer.W):
                for w_j, ww in enumerate(w):
                    W = np.copy(layer.W)
                    W[w_i][w_j] = ww + epsilon

                    new_layer = Dense(W, layer.b, layer.a)
                    new_seq = get_new_sequence(layer_id, new_layer)
                    h = eval_sequence(x, new_seq)

                    num_grad = (loss_func(h, y) - loss) / epsilon
                    layer.dW[w_i][w_j] = num_grad

            for b_i, bb in enumerate(layer.b):
                b = np.copy(layer.b)
                b[b_i] = bb + epsilon

                new_layer = Dense(layer.W, b, layer.a)
                new_seq = get_new_sequence(layer_id, new_layer)
                h = eval_sequence(x, new_seq)

                num_grad = (loss_func(h, y) - loss) / epsilon
                layer.db[b_i] = num_grad

        return loss
```
## 경사하강 학습법
```python
def gradient_descent(network, x, y, loss_obj, learning_late=0.01):
    loss = network.calc_gradient(x, y, loss_obj)
    for layer in network.sequence:
        layer.W += -learning_late * layer.dW
        layer.b += -learning_late * layer.db
    return loss
```
## 동작 테스트
```python
x = np.random.normal(0.0, 1.0, (10,))
y = np.random.normal(0.0, 1.0, (2,))

dnn = DNN(hidden_depth=10, num_neuron=32, num_input=10, num_output=2, activation=sigmoid)

t = time.time()
for epoch in range(100):
    loss = gradient_descent(dnn, x, y, mean_squared_error, 0.01)
    print('Epoch {}: Test loss {}'.format(epoch, loss))
print('{} seconds elapsed.'.format(time.time() - t))
```

# 역전파 학습법을 이용한 심층 신경망 학습

## import modules
```python
import time
import numpy as np
```

## 유틸리티 함수
```python
def _t(x):
    return np.transpose(x)

def _m(A, B):
    return np.matmul(A, B)
```

## Sigmoid 구현
```python
class Sigmoid:
    def __init__(self):
        self.last_o = 1

    def __call__(self, x):
        self.last_o = 1.0 / (1.0 + np.exp(-x))
        return self.last_o

    def grad(self):   # sigmoid(x)(1 - sigmoid(x))
        return self.last_o * (1.0 - self.last_o)
```
## Mean Squared Error 구현
```python
class MeanSquaredError: # 1/2 * mean((h - y)^2) --> h - y
    def __init__(self):
        self.dh = 1
        self.last_diff = 1

    def __call__(self, h, y):
        self.last_diff = h - y
        return 1 / 2 * np.mean(np.square(self.last_diff))

    def grad(self):
        return self.last_diff
```
## Dense Layer 구현
```python
class Dense:
    def __init__(self, W, b, a_obj):
        self.W = W
        self.b = b
        self.a = a_obj()

        self.dW = np.zeros_like(self.W)
        self.db = np.zeros_like(self.b)
        self.dh = np.zeros_like(_t(self.W))

        self.last_x = np.zeros((self.W.shape[0],))
        self.last_h = np.zeros((self.W.shape[1],))

    def __call__(self, x):
        self.last_x = x
        self.last_h = _m(_t(self.W,), x) + self.b
        return self.a(self.last_h)

    def grad(self):
        return self.W * self.a.grad()

    def grad_W(self, dh):
        grad = np.ones_like(self.W)
        grad_a = self.a.grad()
        for j in range(grad.shape[1]): # dy / dw = x
            grad[:, j] = dh[j] * grad_a[j] * self.last_x
        return grad

    def grad_b(self, dh): # dy / db = 1
        return dh * self.a.grad()
```
## 심층신경망 구현
```python
class DNN:
    def __init__(self, hidden_depth, num_neuron, input, output, activation=Sigmoid):
        def init_var(i, o):
            return np.random.normal(0.0, 0.01, (i, o)), np.zeros((o,))

        self.sequence = list()
        W, b = init_var(input, num_neuron)
        self.sequence.append(Dense(W, b, activation))

        for index in range(hidden_depth):
            W, b = init_var(num_neuron, num_neuron)
            self.sequence.append(Dense(W, b, activation))

        W, b = init_var(num_neuron, output)
        self.sequence.append(Dense(W, b, activation))

    def __call__(self, x):
        for layer in self.sequence:
            x = layer(x)
        return x

    def calc_gradient(self, loss_obj):
        loss_obj.dh = loss_obj.grad()
        self.sequence.append(loss_obj)

        # back-prop loop
        for i in range(len(self.sequence) - 1, 0, -1):
            l1 = self.sequence[i]
            l0 = self.sequence[i - 1]

            l0.dh = _m(l0.grad(), l1.dh)
            l0.dW = l0.grad_W(l1.dh)
            l0.db = l0.grad_b(l1.dh)

        self.sequence.remove(loss_obj)
```
## 경사하강 학습법
```python
def gradient_descent(network, x, y, loss_obj, alpha=0.01):
    loss = loss_obj(network(x), y)
    network.calc_gradient(loss_obj)
    for layer in network.sequence:
        layer.W += -alpha * layer.dW
        layer.b += -alpha * layer.db
    return loss
```
## 동작 테스트
```python
x = np.random.normal(0.0, 1.0, (10,))
y = np.random.normal(0.0, 1.0, (2,))

t = time.time()
dnn = DNN(hidden_depth=5, num_neuron=32, input=10, output=2, activation=Sigmoid)
loss_obj = MeanSquaredError()
for epoch in range(100):
    loss = gradient_descent(dnn, x, y, loss_obj, alpha=0.01)
    print('Epoch {}: Test loss {}'.format(epoch, loss))
print('{} seconds elapsed.'.format(time.time() - t))
```
