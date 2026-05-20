$$F (s) = \frac {C _ {1}}{s - p _ {1}} + \frac {C _ {2}}{(s - p _ {1}) ^ {2}} + \frac {C _ {3}}{(s - p _ {1}) ^ {3}} + \frac {C _ {4}}{s - p _ {4}} + \dots + \frac {C _ {n}}{s - p _ {n}}$$

由前面讨论的方法，我们可以确定常数 $C_4$ 到 $C_n$ 。如果我们在上式两边同时乘以 $(s - p_1)^3$ 得到

$$(s - p _ {1}) ^ {3} F (s) = C _ {1} (s - p _ {1}) ^ {2} + C _ {2} (s - p _ {1}) + C _ {3} + \dots + \frac {C _ {n} (s - p _ {1}) ^ {3}}{s - p _ {n}} \tag {A.25}$$

如果令 $s = p_{1}$ ，除了 $C_3$ ，式(A.25)右边的所有因子都将是零，所以，有

$$C _ {3} = (s - p _ {1}) ^ {3} F (s) \mid_ {s = p _ {1}}$$

为了确定其他因子，将式(A.25)两边分别对拉普拉斯变量 s 求微分：

$$\frac {\mathrm{d}}{\mathrm{d} s} \left[ (s - p _ {1}) ^ {3} F (s) \right] = 2 C _ {1} (s - p _ {1}) + C _ {2} + \dots + \frac {\mathrm{d}}{\mathrm{d} s} \left[ \frac {C _ {n} (s - p _ {1}) ^ {3}}{s - p _ {n}} \right] \tag {A.26}$$

再令 $s = p_{1}$ ，我们有

$$C _ {2} = \frac {\mathrm{d}}{\mathrm{d} s} [ (s - p _ {1}) ^ {3} F (s) ] _ {s = p _ {1}}$$

类似的，如果对式(A.26)再次微分，且令 $s = p_{1}$ ，得

$$C _ {1} = \frac {1}{2} \frac {\mathrm{d} ^ {2}}{\mathrm{d} s ^ {2}} \left[ (s - p _ {1}) ^ {3} F (s) \right] _ {s = p _ {1}}$$

总之，可以求出 k 重极点因子的系数 $C_{i}$

$$C _ {k - i} = \frac {1}{i !} \left[ \frac {\mathrm{d} ^ {i}}{\mathrm{d} s ^ {i}} \left[ (s - p _ {1}) ^ {k} F (s) \right] \right] _ {s = p _ {1}}, i = 0, \dots , k - 1$$

例 A. 10 部分分式展开法：重实根

求拉普拉斯逆变换为

$$F (s) = \frac {s + 3}{(s + 1) (s + 2) ^ {2}}$$

时间函数 $f(t)$ 。

解答。部分分式展开形式为

$$F (s) = \frac {C _ {1}}{s + 1} + \frac {C _ {2}}{s + 2} + \frac {C _ {3}}{(s + 2) ^ {2}}$$

那么

$$
\begin{array}{l} C _ {1} = (s + 1) F (s) \mid_ {s = - 1} = \frac {s + 3}{(s + 2) ^ {2}} \mid_ {s = - 1} = 2 \\ C _ {2} = \frac {\mathrm{d}}{\mathrm{d} s} [ (s + 2) ^ {2} F (s) ] | _ {s = - 2} = - 2 \\ C _ {3} = (s + 2) ^ {2} F (s) \mid_ {s = - 2} = \frac {s + 3}{s + 1} \mid_ {s = - 2} = - 1 \\ \end{array}
$$

函数 $f(t)$ 是

$$f (t) = (2 \mathrm{e} ^ {- t} - 2 \mathrm{e} ^ {- 2 t} - t \mathrm{e} ^ {- 2 t}) 1 (t)$$

用 Matlab 中的 residue 函数计算部分分式展开为

$$
\begin{array}{l} \text { num } [ 1 3 ]; \quad \% \text { formnumerator } \\ \mathrm{den} = \operatorname{conv} ([ 1 1 ], [ 1 4 4 ]), \quad \% \text {formdenominator} \\ [ r, p, k ] = \text { residue(num,den) } \% \text { computeresidues } \\ \end{array}
$$

得出结果

$$\boldsymbol {r} = \left[ - 2 - 1, 2 \right] ^ {\mathrm{T}}, \quad \boldsymbol {p} = \left[ - 2 - 2 - 1 \right] ^ {\mathrm{T}}, \quad k = [ ]$$

与手算结果相同。

对于拉普拉斯反变换，在 Matlab 中使用如下命令也可以得到相同的结果：

$$
\begin{array}{l} \text {syms s t} \\ \text {ilaplace((s + 3) / ((s + 1) ^ {*} (s + 2) ^ {2}) .} \end{array}
$$
