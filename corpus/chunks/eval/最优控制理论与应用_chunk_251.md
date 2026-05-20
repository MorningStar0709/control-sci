$$
\begin{array}{l} \boldsymbol {\Phi} _ {i + 1} = \boldsymbol {E} ^ {\mathrm{T}} \boldsymbol {\Phi} _ {i} \boldsymbol {E} - (\boldsymbol {E} ^ {\mathrm{T}} \boldsymbol {\Phi} _ {i} \boldsymbol {G} + \boldsymbol {W}) (\boldsymbol {G} ^ {\mathrm{T}} \boldsymbol {\Phi} _ {i} \boldsymbol {G} + \boldsymbol {H}) ^ {- 1} (\boldsymbol {E} ^ {\mathrm{T}} \boldsymbol {\Phi} _ {i} \boldsymbol {G} + \boldsymbol {W}) + \boldsymbol {Q} \\ \boldsymbol {E} = (\boldsymbol {I} - \boldsymbol {A}) ^ {- 1} (\boldsymbol {I} + \boldsymbol {A}), \\ \boldsymbol {G} = 2 (\boldsymbol {I} - \boldsymbol {A}) ^ {- 1} \boldsymbol {B}, \\ \boldsymbol {H} = \boldsymbol {R} + \boldsymbol {B} ^ {\mathrm{T}} (\boldsymbol {I} - \boldsymbol {A} ^ {\mathrm{T}}) ^ {- 1} \boldsymbol {Q} (\boldsymbol {I} - \boldsymbol {A}) ^ {- 1} \boldsymbol {B}, \\ \boldsymbol {W} = \boldsymbol {Q} (\boldsymbol {I} - \boldsymbol {A}) ^ {- 1} \boldsymbol {B} \\ \end{array}
$$

如果 $\pmb{\Phi}_{i+1}$ 收敛于一个常数矩阵，即 $\| \pmb{\Phi}_{i+1} - \pmb{\Phi}_i \| < \varepsilon$ ，则可以得出代数黎卡提方程的解为：

$$\boldsymbol {P} = 2 \left(\boldsymbol {I} - \boldsymbol {A} ^ {\mathrm{T}}\right) ^ {- 1} \boldsymbol {\Phi} _ {i + 1} (\boldsymbol {I} - \boldsymbol {A}) ^ {- 1}$$

上面的迭代算法可以用 MATLAB 来实现：

$$
\begin{array}{l} \% * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * \\ \mathrm{I} = \text { eye } (\text { size } (\mathrm{A})) ; \\ \end{array}
$$

```matlab
iA = inv(I - A);
E = iA * (I + A);
G = 2 * iA^2 * B;
H = R + B' * iA' * Q * iA * B;
W = Q * iA * B;
P0 = zeros(size(A));
i = 0;
while(1), i = i + 1;
    P = E' * P0 * E - (E' * P0 * G + W) * inv(G' * P0 * G + H) * (E' * P0 * G + W)' + Q;
    if(norm(P - P0) < eps), break;
    else, P0 = P;
    end
end
P = 2 * iA' * P * iA; 
```

把这个文件命名为 mylq.m, 方便以后调用来求解代数黎卡提方程。方法二：

在 MATLAB 的控制系统工具箱中提供了求解代数黎卡提方程的函数 lqr()，其调用的格式为：

$$[ \mathrm{K}, \mathrm{P}, \mathrm{E} ] = \operatorname{lqr} (\mathrm{A}, \mathrm{B}, \mathrm{Q}, \mathrm{R})$$

式中，输入矩阵为 A, B, Q, R，其中 $(A, B)$ 为给定的对象状态方程模型， $(Q, R)$ 分别为加权矩阵 Q 和 R；返回矩阵 K 为状态反馈矩阵，P 为代数黎卡提方程的解，E 为闭环系统的零极点。

这里的求解是建立在 MATLAB 的控制系统工具箱中给出的一个基于 Schur 变换的黎卡提方程求解函数 are() 基础上的, 该函数的调用格式为:

$$\mathbf {X} = \operatorname{are} (\mathbf {M}, \mathbf {T}, \mathbf {V})$$

其中， $M, T, V$ 矩阵满足下列代数黎卡提方程，are是Algebraic Riccati Equation的缩写。

$$\boldsymbol {M} \boldsymbol {X} + \boldsymbol {X} \boldsymbol {M} ^ {\mathrm{T}} - \boldsymbol {X} \boldsymbol {T} \boldsymbol {X} + \boldsymbol {V} = \boldsymbol {0}$$

对比前面给出的黎卡提方程,可以容易得出
