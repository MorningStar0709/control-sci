$$
H _ {\Pi} \left[ \begin{array}{l} I \\ \Pi \end{array} \right] = \left[ \begin{array}{l} I \\ \Pi \end{array} \right] A _ {\Pi}, \tag {6.4.42}
$$

其中

$$
H _ {\Pi} = \left[ \begin{array}{c c} A _ {F} + Z B _ {1} B _ {1} ^ {\mathrm{T}} P & Z B _ {1} B _ {1} ^ {\mathrm{T}} Z \\ - P B _ {1} B _ {1} ^ {\mathrm{T}} P & - (A _ {F} + Z B _ {1} B _ {1} ^ {\mathrm{T}} P) ^ {\mathrm{T}} \end{array} \right].
$$

考察 Riccati 方程 (6.4.3) 所对应的 Hamilton 矩阵

$$
H _ {X} = \left[ \begin{array}{c c} A & B _ {1} B _ {1} ^ {\mathrm{T}} - B _ {2} B _ {2} ^ {\mathrm{T}} \\ - C _ {1} C _ {1} ^ {\mathrm{T}} & - A ^ {\mathrm{T}} \end{array} \right].
$$

容易验证

$$H _ {\Pi} = W ^ {- 1} H _ {X} W,$$

其中 $W$ 为非奇异阵

$$
W = \left[ \begin{array}{l l} I & - Y \\ P & Z \end{array} \right].
$$

于是将上式代入式 (6.4.42), 得

$$
H _ {X} \left[ \begin{array}{c} X _ {1} \\ X _ {2} \end{array} \right] = \left[ \begin{array}{c} X _ {1} \\ X _ {2} \end{array} \right] A _ {\Pi},
$$

其中

$$
\left[ \begin{array}{l} X _ {1} \\ X _ {2} \end{array} \right] = W \left[ \begin{array}{l} I \\ \Pi \end{array} \right] = \left[ \begin{array}{l} I - Y \Pi \\ P - Z ^ {\mathrm{T}} \Pi \end{array} \right].
$$

由于式(6.4.41)成立， $X_{1} = I - Y\Pi$ 是非奇异阵，故

$$
H _ {X} \left[ \begin{array}{l} I \\ X \end{array} \right] = \left[ \begin{array}{l} I \\ X \end{array} \right] A _ {X}, \tag {6.4.43}
$$

其中 $X = X_{2}X_{1}^{-1}$ , $A_{X} = X_{1}A_{\Pi}X_{1}^{-1}$ . 这表明 $X$ 是式 (6.4.3) 的半正定解, 且 $A_{X} = A + (B_{1}B_{1}^{\mathrm{T}} - B_{2}B_{2}^{\mathrm{T}})X$ 是稳定阵.
