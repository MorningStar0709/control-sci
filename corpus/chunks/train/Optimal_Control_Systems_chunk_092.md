2 Lagrange Multiplier Method: Now we solve the above problem by applying Lagrange multiplier method. We form a new function to be extremized by adjoining a given condition to the original function. The new adjoined function is extremized in the normal way by taking the partial derivatives w.r.t. all its variables, making them equal to zero, and solving for these variables which are extremals. Let the original volume relation (2.5.1) to be extremized be rewritten as

$$f (d, h) = \pi d ^ {2} h / 4 \tag {2.5.8}$$

and the condition (2.5.2) to be satisfied as

$$g (d, h) = 2 \pi d ^ {2} / 4 + \pi d h - A _ {0} = 0. \tag {2.5.9}$$

Then a new adjoint function $\mathcal{L}$ (called Lagrangian) is formed as

$$
\begin{array}{l} \mathcal {L} (d, h, \lambda) = f (d, h) + \lambda g (d, h) \\ = \pi d ^ {2} h / 4 + \lambda (2 \pi d ^ {2} / 4 + \pi d h - A _ {0}) \tag {2.5.10} \\ \end{array}
$$

where, $\lambda$ , a parameter yet to be determined, is called the Lagrange multiplier. Now, since the Lagrangian L is a function of three optimal variables d, h, and $\lambda$ , we take the partial derivatives of $\mathcal{L}(d, h, \lambda)$ w.r.t. each of the variables d, h and $\lambda$ and set them to zero. Thus,

$$\frac {\partial \mathcal {L}}{\partial d} = \pi d h / 2 + \lambda (\pi d + \pi h) = 0 \tag {2.5.11}\frac {\partial \mathcal {L}}{\partial h} = \pi d ^ {2} / 4 + \lambda (\pi d) = 0 \tag {2.5.12}\frac {\partial \mathcal {L}}{\partial \lambda} = 2 \pi d ^ {2} / 4 + \pi d h - A _ {0} = 0. \tag {2.5.13}$$

Now, solving the previous three relations (2.5.11) to (2.5.13) for the three variables $d^*$ , $h^*$ , and $\lambda^*$ , we get

$$d ^ {*} = \sqrt {\frac {2 A _ {0}}{3 \pi}}; h ^ {*} = \sqrt {\frac {2 A _ {0}}{3 \pi}}; \lambda^ {*} = - \sqrt {\frac {A _ {0}}{2 4 \pi}}. \tag {2.5.14}$$

Once again, to maximize the volume of a cylindrical tank, we need to have the height $(h^{*})$ equal to the diameter $(d^{*})$ of the tank. Note that we need to take the negative value of the square root function for $\lambda$ in (2.5.14) in order to satisfy the physical requirement that the diameter d obtained from (2.5.12) as

$$d = - 4 \lambda \tag {2.5.15}$$

is a positive value.

Now, we generalize the previous two methods.
