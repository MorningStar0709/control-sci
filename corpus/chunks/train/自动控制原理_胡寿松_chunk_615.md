6) $\Phi(t_2 - t_0) = \Phi(t_2 - t_1)\Phi(t_1 - t_0)$ (9-37)

证明 由于

$$\boldsymbol {x} (t _ {2}) = \boldsymbol {\Phi} (t _ {2} - t _ {0}) \boldsymbol {x} (t _ {0}), \quad \boldsymbol {x} (t _ {1}) = \boldsymbol {\Phi} (t _ {1} - t _ {0}) \boldsymbol {x} (t _ {0})$$

则 $\pmb {x}(t_2) = \pmb {\Phi}(t_2 - t_1)\pmb {x}(t_1) = \pmb {\Phi}(t_2 - t_1)\pmb {\Phi}(t_1 - t_0)\pmb {x}(t_0)$

$$= \boldsymbol {\Phi} (t _ {2} - t _ {0}) \boldsymbol {x} (t _ {0})$$

![](image/87bca91373597008b8345b74ade0f086dee970441f1e76ca3d24f9627ff78566.jpg)

<details>
<summary>text_image</summary>

x
Φ(t₂−t₀)
x(t₀)
Φ(t₁−t₀)
Φ(t₂−t₁)
t₀
t₁
t₂
x(t₂)
</details>

图 9-13 状态转移矩阵性质 6)

故式(9-37)成立。

根据转移矩阵的这一性质,可把一个转移过程分为若干个小的转移过程来研究,如图 9-13 所示。

7) $[\pmb{\Phi}(t)]^k = \pmb{\Phi}(kt)$ (9-38)

证明 由于

$$[ \boldsymbol {\Phi} (t) ] ^ {k} = (\mathrm{e} ^ {\boldsymbol {A} t}) ^ {k} = \mathrm{e} ^ {k \boldsymbol {A} t} = \mathrm{e} ^ {\boldsymbol {A} (k t)} = \boldsymbol {\Phi} (k t)$$

故式(9-38)成立。

8) 若 $\Phi(t)$ 为 $\dot{x}(t) = Ax(t)$ 的状态转移矩阵, 则引入非奇异变换 $x = Px$ 后的状态转移矩阵为

$$\bar {\boldsymbol {\Phi}} (t) = \boldsymbol {P} ^ {- 1} \mathrm{e} ^ {\boldsymbol {A} t} \boldsymbol {P} \tag {9-39}$$

证明 将 $x = P\bar{x}$ 代入 $\dot{x}(t) = Ax(t)$ ，有

$$\boldsymbol {P} \dot {\boldsymbol {x}} = \boldsymbol {A} \boldsymbol {P} \bar {\boldsymbol {x}}, \quad \dot {\boldsymbol {x}} = \boldsymbol {P} ^ {- 1} \boldsymbol {A} \boldsymbol {P} \bar {\boldsymbol {x}}\bar {\boldsymbol {x}} (t) = \overline {{{\boldsymbol {\Phi}}}} (t) \bar {\boldsymbol {x}} (0) = \mathrm{e} ^ {\boldsymbol {P} ^ {- 1} \boldsymbol {A P t}} \bar {\boldsymbol {x}} (0)$$

式中 $e^{P^{-1}APt}=I+P^{-1}APt+\frac{1}{2}(P^{-1}AP)^{2}t^{2}+\cdots+\frac{1}{k!}(P^{-1}AP)^{k}t^{k}+\cdots$

$$= \boldsymbol {P} ^ {- 1} \boldsymbol {I P} + \boldsymbol {P} ^ {- 1} \boldsymbol {A P t} + \frac {1}{2} \boldsymbol {P} ^ {- 1} \boldsymbol {A} ^ {2} \boldsymbol {P t} ^ {2} + \dots + \frac {1}{k !} \boldsymbol {P} ^ {- 1} \boldsymbol {A} ^ {k} \boldsymbol {P t} ^ {k} + \dots= \boldsymbol {P} ^ {- 1} \left(\boldsymbol {I} + \boldsymbol {A} t + \frac {1}{2} \boldsymbol {A} ^ {2} t ^ {2} + \dots + \frac {1}{k !} \boldsymbol {A} ^ {k} t ^ {k} + \dots\right) \boldsymbol {P} = \boldsymbol {P} ^ {- 1} \mathrm{e} ^ {\boldsymbol {A} t} \boldsymbol {P}$$

因而式(9-39)成立。

9）两种常见的状态转移矩阵。设 $A = \text{diag}[\lambda_{1}, \lambda_{2}, \cdots, \lambda_{n}]$ ，即 A 为对角阵，且具有互异元素，则
