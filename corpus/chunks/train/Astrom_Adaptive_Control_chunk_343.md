# Finding a Controller Structure

The first step in the design procedure is to find a suitable controller structure. The tools for doing this were developed in Section 3.2. Let the process be described by the continuous-time model

$$A y (t) = b _ {0} B u (t) \tag {5.64}$$

where it is assumed that the polynomials A and B do not have common factors and the polynomial B is monic and assumed to have all its zeros in the left half-plane. Furthermore, the polynomial is normalized so that B is monic. The variable $b_{0}$ is called the instantaneous gain or the high-frequency gain. A general linear controller can be written as

$$R u (t) = - S y (t) + T u _ {c} (t) \tag {5.65}$$

where $u_{c}$ is the command signal. Since the polynomial B is stable, the corresponding poles can be canceled by the controller. This corresponds to $R = R_{1}B$ . The closed-loop system obtained when the controller is applied to the process (5.64) is described by

$$\left(A R _ {1} + b _ {0} S\right) y = b _ {0} T u _ {c} \tag {5.66}$$

If polynomial $T$ is chosen to be $T = t_0A_0$ , where $A_0$ is a stable monic polynomial and $R_1$ and $S$ satisfy

$$A R _ {1} + b _ {0} S = A _ {0} A _ {m} \tag {5.67}$$

it is possible to achieve perfect model-following with the model

$$A _ {m} y _ {m} (t) = b _ {0} t _ {0} u _ {c} (t) \tag {5.68}$$
