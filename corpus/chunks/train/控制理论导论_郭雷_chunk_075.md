$$\boldsymbol {T} _ {1} = \boldsymbol {Q} _ {c 2} \boldsymbol {Q} _ {c 1} ^ {\mathrm{T}} (\boldsymbol {Q} _ {c 1} \boldsymbol {Q} _ {c 1} ^ {\mathrm{T}}) ^ {- 1}, \quad \boldsymbol {T} _ {2} = (\boldsymbol {Q} _ {o 1} ^ {\mathrm{T}} \boldsymbol {Q} _ {o 1}) ^ {- 1} \boldsymbol {Q} _ {o 1} ^ {\mathrm{T}} \boldsymbol {Q} _ {o 2}.$$

于是由式 (1.5.17) 有

$$
\begin{array}{l} \boldsymbol {T} _ {2} \boldsymbol {T} _ {1} = \left(\boldsymbol {Q} _ {o 1} ^ {\mathrm{T}} \boldsymbol {Q} _ {o 1}\right) ^ {- 1} \boldsymbol {Q} _ {o 1} ^ {\mathrm{T}} \boldsymbol {Q} _ {o 2} \boldsymbol {Q} _ {c 2} \boldsymbol {Q} _ {c 1} ^ {\mathrm{T}} \left(\boldsymbol {Q} _ {c 1} \boldsymbol {Q} _ {c 1} ^ {\mathrm{T}}\right) ^ {- 1} \\ = \left(Q _ {o 1} ^ {\mathrm{T}} Q _ {o 1}\right) ^ {- 1} Q _ {o 1} ^ {\mathrm{T}} Q _ {o 1} Q _ {c 1} Q _ {c 1} ^ {\mathrm{T}} \left(Q _ {c 1} Q _ {c 1} ^ {\mathrm{T}}\right) ^ {- 1} = I _ {n}. \\ \end{array}
$$

因此 $\pmb{T}_{2} = \pmb{T}_{1}^{-1}$ . 再由式 (1.5.17) 得

$$Q _ {c 1} = T _ {2} Q _ {c 2}, \quad Q _ {o 1} = Q _ {o 2} T _ {1}.$$

因而有

$$\boldsymbol {B} _ {1} = \boldsymbol {T} _ {2} \boldsymbol {B} _ {2}, \quad \boldsymbol {C} _ {1} = \boldsymbol {C} _ {2} \boldsymbol {T} _ {2} ^ {- 1}.$$

又由式 (1.5.16) 推知，

$$Q _ {o 1} A _ {1} Q _ {c 1} = Q _ {o 2} A _ {2} Q _ {c 2} = Q _ {o 1} T _ {2} A _ {2} T _ {2} ^ {- 1} Q _ {c 1}.$$

在上式两边分别左乘 $(Q_{o1}^{\mathrm{T}}Q_{o1})^{-1}Q_{o1}^{\mathrm{T}}$ ，右乘 $Q_{c1}^{\mathrm{T}}(Q_{c1}Q_{c1}^{\mathrm{T}})^{-1}$ 则得

$$\boldsymbol {A} _ {1} = \boldsymbol {T} _ {2} \boldsymbol {A} _ {2} \boldsymbol {T} _ {2} ^ {- 1}.$$

这说明 $(A_{1}, B_{1}, C_{1})$ 与 $(A_{2}, B_{2}, C_{2})$ 是代数等价的.

定理 1.5.4 和定理 1.5.5 是最小实现的基本性质。它说明一个真有理分式矩阵 $W(s)$ 的最小实现是完全能控和完全能观测的，两个不同最小实现之间是代数等价的，因而在代数等价意义下最小实现是唯一的。
