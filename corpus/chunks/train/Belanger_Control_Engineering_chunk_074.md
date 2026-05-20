b. Zero-state linearity: Let $\mathbf{x}_{1}(t)$ be the zero-state response to an input $\mathbf{u}_{1}(t)$ , and $\mathbf{x}_{2}(t)$ be the zero-state response to an input $\mathbf{u}_{2}(t)$ . Then the zero-state response to an input $\alpha\mathbf{u}_{1}(t)+\beta\mathbf{u}_{2}(t)$ , with $\alpha$ and $\beta$ constants, is $\mathbf{x}(t)=\alpha\mathbf{x}_{1}(t)+\beta\mathbf{x}_{2}(t)$ . This is established, as above, by inserting $\mathbf{x}(t)$ in Equation 3.3:

$$\dot {\mathbf {x}} = \alpha \dot {\mathbf {x}} _ {1} + \beta \dot {\mathbf {x}} _ {2} = \alpha (A \mathbf {x} _ {1} + B \mathbf {u} _ {1}) + \beta (A \mathbf {x} _ {2} + B \mathbf {u} _ {2})= A \left(\alpha \mathbf {x} _ {1} + \beta \mathbf {x} _ {2}\right) + B \left(\alpha \mathbf {u} _ {1} + \beta \mathbf {u} _ {2}\right)= A \mathbf {x} + B (\alpha \mathbf {u} _ {1} + \beta \mathbf {u} _ {2})$$

so that $\mathbf{x}$ is a solution, with $\alpha \mathbf{u}_1 + \beta \mathbf{u}_2$ as the input. Since

$$\mathbf {x} (0) = \alpha \mathbf {x} _ {1} (0) + \beta \mathbf {x} _ {2} (0) = \mathbf {0}$$

x is also a zero-state solution. Uniqueness is invoked to establish that it is the one and only solution.

c. Additivity: The complete solution to Equation 3.1 is the sum of the zero-input and zero-state solutions. This is easily shown by inserting $\mathbf{x}_{zi} + \mathbf{x}_{zs}$ into Equation 3.1. The details are left to the reader.
