$$\frac {d V}{d t} = - \xi_ {1} ^ {2} + \xi_ {1} \xi_ {2} + x _ {3} \left(\xi_ {2} + \frac {\partial a _ {1}}{\partial \hat {\theta}} \frac {d \hat {\theta}}{d t}\right) + \bar {\theta} \left(\xi_ {1} f + \xi_ {2} \frac {\partial a _ {1}}{\partial \xi_ {1}} f (\xi_ {1}) - \frac {d \hat {\theta}}{d t}\right)$$

The term containing $\tilde{\theta}$ can be eliminated by choosing

$$\frac {d \hat {\theta}}{d t} = b _ {2} (\xi_ {1}, \xi_ {2})$$

where

$$b _ {2} = \xi_ {1} f (\xi_ {1}) + \xi_ {2} \frac {\partial a _ {2}}{\partial \xi_ {1}} f (\xi_ {1}) \tag {5.97}$$

The function $b_{2}(\xi_{1},\xi_{2})$ can be interpreted as a good way to choose the parameter update rate $d\hat{\theta}/dt$ based on $\xi_{1}$ and $\xi_{2}$ . The “control variable” $x_{3}$ can be chosen to give

$$\frac {d V}{d t} = - \xi_ {1} ^ {2} - \xi_ {2} ^ {2}$$

Using $b_{2}$ as an estimate of $d\hat{\theta} / dt$ , we now rewrite Eq. (5.96) as

$$
\begin{array}{l} \frac {d \xi_ {2}}{d t} = - \xi_ {1} - \xi_ {2} + x _ {3} + \xi_ {1} + \xi_ {2} + \frac {\partial a _ {1}}{\partial \xi_ {1}} (- \xi_ {1} + \xi_ {2} + \tilde {\theta} f) \\ + \frac {\partial a _ {1}}{\partial \hat {\theta}} b _ {2} + \frac {\partial a _ {1}}{\partial \hat {\theta}} \left(\frac {d \hat {\theta}}{d t} - b _ {2}\right) \tag {5.98} \\ \end{array}
$$

Now define

$$a _ {2} \left(\xi_ {1}, \xi_ {2}, \hat {\theta}\right) = \xi_ {1} + \xi_ {2} + \frac {\partial a _ {1}}{\partial \xi_ {1}} \left(- \xi_ {1} + \xi_ {2}\right) + \frac {\partial a _ {1}}{\partial \hat {\theta}} b _ {2} \tag {5.99}$$

and introduce the state variable $\xi_{3}$ as

$$\xi_ {3} = x _ {3} + a _ {2} (\xi_ {1}, \xi_ {2}, \hat {\theta})$$

The differential equation (5.98) can be written as

$$\frac {d \xi_ {2}}{d t} = - \xi_ {1} - \xi_ {2} + \xi_ {3} + \frac {\partial a _ {1}}{\partial \xi_ {1}} \tilde {\theta} f + \frac {\partial a _ {1}}{\partial \hat {\theta}} \left(\frac {d \hat {\theta}}{d t} - b _ {2}\right) \tag {5.100}$$

The derivative of $\xi_{3}$ becomes

$$\frac {d \xi_ {3}}{d t} = u + \frac {\partial a _ {2}}{\partial \xi_ {1}} \cdot \frac {d \xi_ {1}}{d t} + \frac {\partial a _ {2}}{\partial \xi_ {2}} \cdot \frac {d \xi_ {2}}{d t} + \frac {\partial a _ {2}}{\partial \hat {\theta}} \cdot \frac {d \hat {\theta}}{d t} \tag {5.101}$$
