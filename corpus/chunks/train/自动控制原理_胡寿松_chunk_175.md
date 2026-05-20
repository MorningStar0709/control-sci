$$
\begin{array}{l} E (s) = \frac {\omega s}{(s + 1 / T) \left(s ^ {2} + \omega^ {2}\right)} \\ = - \frac {T \omega}{\left(T ^ {2} \omega^ {2} + 1\right)} \cdot \frac {1}{(s + 1 / T)} \\ + \frac {T \omega}{\left(T ^ {2} \omega^ {2} + 1\right)} \cdot \frac {s}{\left(s ^ {2} + \omega^ {2}\right)} + \frac {T ^ {2} \omega^ {3}}{\left(T ^ {2} \omega^ {2} + 1\right)} \cdot \frac {1}{\left(s ^ {2} + \omega^ {2}\right)} \\ \end{array}
$$

所以得 $e_{s}(t) = \frac{T\omega}{T^{2}\omega^{2} + 1}\cos \omega t + \frac{T^{2}\omega^{2}}{T^{2}\omega^{2} + 1}\sin \omega t$

显然， $e_{s}(\infty)\neq 0$ 。由于正弦函数的拉氏变换式在虚轴上不解析，所以此时不能应用终值定理法来计算系统在正弦函数作用下的稳态误差，否则会得出

$$e _ {s} (\infty) = \lim _ {s \rightarrow 0} s E (s) = \lim _ {s \rightarrow 0} \frac {\omega s ^ {2}}{(s + 1 / T) (s ^ {2} + \omega^ {2})} = 0$$

的错误结论。

应当指出, 对于高阶系统, 除了应用 MATLAB 软件, 误差信号 $E(s)$ 的极点一般不易求得, 故用反变换法求稳态误差的方法并不实用。在实际使用过程中, 只要验证 $sE(s)$ 满足要求的解析条件, 无论是单位反馈系统还是非单位反馈系统, 都可以利用式(3-73)来计算系统在输入信号作用下位于输入端的稳态误差 $e_{ss}(\infty)$ 。
