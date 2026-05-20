2 Lagrange Multiplier Method: Here, we use the ideas developed in the previous section on the extremization of functions with conditions. Consider the optimization of the functional (2.6.25) with the boundary conditions (2.6.26) under the condition describing the plant (2.6.27). First we rewrite the condition (2.6.27) as

$$g (x (t), \dot {x} (t), u (t)) = \dot {x} (t) + x (t) - u (t) = 0. \tag {2.6.36}$$

Now, we form an augmented functional as

$$
\begin{array}{l} J = \int_ {0} ^ {1} \left[ x ^ {2} (t) + u ^ {2} (t) + \lambda (t) \left\{\dot {x} (t) + x (t) - u (t) \right\} \right] d t \\ = \int_ {0} ^ {1} \mathcal {L} (x (t), \dot {x} (t), u (t), \lambda (t)) d t \tag {2.6.37} \\ \end{array}
$$

where, $\lambda(t)$ is the Lagrange multiplier, and

$$
\begin{array}{l} \mathcal {L} (x (t), \dot {x} (t), u (t), \lambda (t)) = x ^ {2} (t) + u ^ {2} (t) \\ + \lambda (t) \left\{\dot {x} (t) + x (t) - u (t) \right\} \tag {2.6.38} \\ \end{array}
$$

is the Lagrangian. Now, we apply the Euler-Lagrange equation to the previous Lagrangian to get

$$\left(\frac {\partial \mathcal {L}}{\partial x}\right) _ {*} - \frac {d}{d t} \left(\frac {\partial \mathcal {L}}{\partial \dot {x}}\right) _ {*} = 0 \longrightarrow 2 x ^ {*} (t) + \lambda^ {*} (t) - \dot {\lambda} ^ {*} (t) = 0 \tag {2.6.39}\left(\frac {\partial \mathcal {L}}{\partial u}\right) _ {*} - \frac {d}{d t} \left(\frac {\partial \mathcal {L}}{\partial \dot {u}}\right) _ {*} = 0 \longrightarrow 2 u ^ {*} (t) - \lambda^ {*} (t) = 0 \tag {2.6.40}\left(\frac {\partial \mathcal {L}}{\partial \lambda}\right) _ {*} - \frac {d}{d t} \left(\frac {\partial \mathcal {L}}{\partial \dot {\lambda}}\right) _ {*} = 0 \longrightarrow \dot {x} ^ {*} (t) + x ^ {*} (t) - u ^ {*} (t) = 0 \tag {2.6.41}$$

and solve for optimal $x^{*}(t)$ , $u^{*}(t)$ , and $\lambda^{*}(t)$ . We get first from (2.6.40) and (2.6.41)

$$\lambda^ {*} (t) = 2 u ^ {*} (t) = 2 \left(\dot {x} ^ {*} (t) + x ^ {*} (t)\right). \tag {2.6.42}$$

Using the equation (2.6.42) in (2.6.39)

$$2 x ^ {*} (t) + 2 \left(\dot {x} ^ {*} (t) + x ^ {*} (t)\right) - 2 \left(\ddot {x} ^ {*} (t) + \dot {x} ^ {*} (t)\right) = 0. \tag {2.6.43}$$

Solving the previous equation, we get

$$\ddot {x} ^ {*} (t) - 2 x ^ {*} (t) = 0 \longrightarrow x ^ {*} (t) = C _ {1} e ^ {- \sqrt {2} t} + C _ {2} e ^ {\sqrt {2} t}. \tag {2.6.44}$$

Once we know $x^{*}(t)$ , we get $\lambda^{*}(t)$ and hence $u^{*}(t)$ from (2.6.42) as
