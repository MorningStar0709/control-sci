$$J = \mathbf {x} ^ {T} (T) \mathbf {S x} (T) + \frac {1}{2} \int_ {t _ {0}} ^ {T} \mathbf {u} ^ {T} (t) \mathbf {R u} (t) d t, \tag {4.161}$$

where

$$
\mathbf {S} = \left[ \begin{array}{c c c} I & | & 0 \\ - & + & - \\ 0 & | & 0 \end{array} \right] \text {and} \mathbf {R} = \left[ \begin{array}{c c c} b & | & 0 \\ - & + & - \\ 0 & | & b \end{array} \right]
$$

where b is an element of the positive definite matrix R.

Now the performance index reduces to

$$J = x _ {1} ^ {2} (T) + x _ {2} ^ {2} (T) + \frac {1}{2} \int_ {t _ {0}} ^ {T} (u _ {1} ^ {2} + u _ {2} ^ {2}) d t. \tag {4.162}$$

In Section 4.8.3 we noted in connection with (4.121) that the term ${ \mathbf { u } } ^ { T } ( t ) { \mathbf { R u } } ( t )$ discourages the use of excessive large control effort. In a similar manner, we can say that if the term b is chosen to be small, the missile designer is willing to expend whatever acceleration is required to minimize the terminal miss distance (assuming, of course, that the missile is capable of producing and sustaining such accelerations). On the other hand, if b is chosen to be large, the magnitude of the acceleration available will be limited in achieving small miss distance. Using (4.132), we have

$$\mathbf {u} ^ {*} (\mathbf {x}, t) = - \mathbf {R} ^ {- 1} \mathbf {B} ^ {T} \mathbf {P} (t) \mathbf {x} (t) = - (1 / b) [ 0: I ] \mathbf {P} (t) \mathbf {x} (t), \tag {4.163}$$

and from (4.130),

$$
- \frac {d \mathbf {P} (t)}{d t} = \mathbf {P} \left[ \begin{array}{c c c} 0 & | & I \\ - & + & - \\ 0 & | & 0 \end{array} \right] + \left[ \begin{array}{c c c} 0 & | & 0 \\ - & + & - \\ I & | & 0 \end{array} \right] \mathbf {P} - \mathbf {P} \left[ \begin{array}{c} 0 \\ - - \\ I \end{array} \right] (1 / b) [ 0: I ] \boldsymbol {P}. \tag {4.164}
$$

Equations (4.163) and (4.164) can be solved analytically yielding the control law as follows:

$$
\begin{array}{l} u _ {t} = \left[ \begin{array}{c} u _ {1} (t) \\ u _ {2} (t) \end{array} \right] \\ = \left[ \begin{array}{c c c c} - 3 t _ {g o} / (3 b + t _ {g o} ^ {3}) & 0 & - 3 t _ {g o} ^ {2} / (3 b + t _ {g o} ^ {3}) & 0 \\ 0 & - 3 t _ {g o} / (3 b + t _ {g o} ^ {3}) & 0 & - 3 t _ {g o} ^ {2} / (3 b + t _ {g o} ^ {3}) \end{array} \right], \tag {4.165} \\ \end{array}
$$

where $t _ { g o } = T - t = - R / ( d R / d t )$ (note that T and $t _ { g o }$ are design parameters). If we assume $b = 0$ , then (4.165) becomes

$$u _ {1} (t) = - (3 / t _ {g o} ^ {2}) x _ {1} - (3 / t _ {g o}) x _ {3}, \tag {4.166a}u _ {2} (t) = - (3 / t _ {g o} ^ {2}) x _ {2} - (3 / t _ {g o}) x _ {4}, \tag {4.166b}$$
