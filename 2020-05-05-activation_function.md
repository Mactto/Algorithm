---
layout: post
title: "활성함수"
subtitle: 딥러닝의 활성함수들
categories: deeplearning
tags: deeplearning activate function
comments: true
---

> '딥러닝에서의 활성함수들'

---
딥러닝에서는 다양한 활성함수가 존재한다.
어떠한 활성 함수를 사용하느냐에 따라 그 출력 값이 달라지기 때문에, 적절한 활성함수를 사용하는 것은 매우 중요하다.

딥러닝 초기에 가장 많이 쓰인 활성함수는 Sigmoid였다.
Sigmoid 활성함수는 0(거짓) 또는 1(참)을 분류하는 로지스틱 회귀분석에 적합한 함수이다.
예를 들면 고양이가 맞는지 아닌지 분류하는 모델이라 하면 사진이 주어졌을 때 고양이가 맞다 아니다를 판별하기에 적합한 함수이다.
현재에도 로지스틱 회귀분석 또는 Binary classification(이진 분류)에서는 유용하게 쓰이고 있는 함수가 바로 Sigmoid 함수이다.

그렇다면 왜 다른 활성 함수들이 등장했을까?

Sigmoid에 Gradient Vanising(기울기 소실 문제)가 존재했다.
기울기 소실 문제란 학습을 할 때 Hidden Layer가 증가할 수록, 즉 신경망이 깊어질수록 미분을 했을 때 기울기가 매우 작아진다.
이 매우 작은 기울기는 Gradient Descent(경사 하강법)의 수행을 방해한다.
기울기가 매우 작기 때문에 학습 진행이 매우 느려지는 것이다.

이러한 문제를 해결하기 위해 Hyperbolic Tangent(tanh) 활성함수가 등장했다.
tanh 함수는 sigmoid를 위아래로 늘려 출력범위가 2배가 되게 만들어 기울기 소실 문제를 해결하고자 한 활성함수이다.
tanh는 어느정도 기울기 소실 문제를 해결하였지만 그저 sigmoid를 늘린 것이기 때문에 매우 깊은 신경망에서는 기울기 소실 문제를 해결하지 못했다.

그래서 기울기 소실 문제를 완전히 해결하기 위해 또다른 활성함수가 등장했다.
바로 Rectified Linear Unit (ReLU)이다.
ReLU는 0보다 작은 값이 나온 경우 0을 반환하고, 0보다 큰 값이 나온 경우 그 값을 그대로 반환한다.
이는 아래와 같은 그래프를 가진다.
오늘날 ReLU는 딥러닝의 기본 활성함수로 자리잡았으며 특별한 이유가 없다면 대개 ReLU 활성함수를 사용한다.
![ReLU](https://mactto.github.io/assets/img/deeplearning/ReLU.jpg)
