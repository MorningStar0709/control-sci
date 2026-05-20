# Specifications

The properties of the closed-loop system are specified indirectly by requiring that the polynomial $A_{c}$ is the discrete-time equivalent of

$$s ^ {2} + 2 \zeta \omega s + \omega^ {2}$$

Hence

$$A _ {c} (z) = z ^ {2} - 2 z e ^ {- \zeta \omega h} \cos \left(\omega h \sqrt {1 - \zeta^ {2}}\right) + e ^ {- 2 \zeta \omega h} = z ^ {2} + a _ {c 1} z + a _ {c 2}$$

An observer of second order is required if we want a controller with integral action. The observer polynomial is chosen as the discrete-time equivalent of a continuous system with two poles at $s = -\alpha$ . Hence

$$A _ {o} (z) = (z - e ^ {- \alpha h}) ^ {2} = z ^ {2} + a _ {o 1} z + a _ {o 2}$$
