# Solution:

After defining

$$\overline {{V}} (t, x) := \inf _ {u [ t, t + \Delta t ] \rightarrow U} \left(\int_ {t} ^ {t + \Delta t} L (s, x (s), u (s)) d s + V (t + \Delta t, x (t + \Delta t))\right) \tag {332}$$

We have shown that $V ( t , x ) \geq \overline { { V } } ( t , x )$ . We can finish the proof of the equality by proving that $V ( t , x ) \leq \overline { { V } } ( t , x )$ By definition of the value function, we have:

$$V (t, x) := \inf _ {u: [ t, t _ {1} ] \rightarrow U, u \in V} J (t, x, u) \tag {333}$$

From the previous results, we can continue the chain of inequalities:

$$\overline {{V}} (t, x) = \int_ {t} ^ {t + \Delta t} L (s, x _ {\varepsilon}, u _ {\varepsilon} (s)) d s + \inf _ {u: [ t + \Delta t, t _ {1} ] \rightarrow U} J (t + \Delta t, x _ {\varepsilon} (t + \Delta t), u) \tag {334}\geq \inf _ {u: [ t, t _ {1} ] \rightarrow U \in V} \int_ {t} ^ {t + \Delta t} L (s, x _ {\varepsilon}, u _ {\varepsilon} (s)) d s + \int_ {t + \Delta t} ^ {t _ {1}} L (s, x _ {\varepsilon}, u _ {\varepsilon} (s)) d s + K (t _ {1}, x _ {\varepsilon}) \tag {335}= \inf _ {u: [ t, t _ {1} ] \rightarrow U \in V} \int_ {t} ^ {t _ {1}} L (s, x _ {\varepsilon}, u _ {\varepsilon} (s)) d s + K (t _ {1}, x _ {\varepsilon}) \tag {336}= \inf _ {u _ {\varepsilon}: [ t, t _ {1} ] \rightarrow U, u \in V} J (t, x, u) \tag {337}= V (t, x) \tag {338}$$

Thus, we have shown that $V ( t , x ) \leq \overline { { V } } ( t , x )$ . Combined with the already proved $V ( t , x ) \geq \overline { { V } } ( t , x )$ , we have shown the equality:

$$V (t, x) = \overline {{V}} (t, x) \tag {339}$$

![](image/58c6bbbc5f234a4e0a108a3c77d8e19e440012ae9b4ae1459959914a88b98fb5.jpg)
