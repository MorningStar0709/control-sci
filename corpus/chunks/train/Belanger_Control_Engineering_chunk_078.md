In Equation 3.9, $e^{A\Delta}$ is computed once and used to step forward in time by $\Delta$ , iteratively.

The matrix exponential has several important properties, of which six are examined here. The first three are quite analogous to properties of the scalar exponential; the others are specifically matrix properties.

◆ Property I $e^{A0} = I$

This is easily seen by inserting $t = 0$ in Equation 3.8.

◆ Property II $e^{A(t_{1}+t_{2})}=e^{At_{2}}e^{At_{1}}=e^{At_{1}}e^{At_{2}}$

To show this, break the "trip" from 0 to $t_1 + t_2$ into two parts, the first from 0 to $t_1$ and the second from $t_1$ to $t_1 + t_2$ . Starting with $\mathbf{x}(0)$ , we have

$$\mathbf {x} (t _ {1}) = e ^ {A t _ {1}} \mathbf {x} (0)$$

and

$$\mathbf {x} (t _ {1} + t _ {2}) = e ^ {A t _ {2}} \mathbf {x} (t _ {1}) = e ^ {A t _ {2}} e ^ {A t _ {1}} \mathbf {x} (0).$$

Now,

$$\mathbf {x} (t _ {1} + t _ {2}) = e ^ {A (t _ {1} + t _ {2})} \mathbf {x} (0)$$

so that

$$e ^ {A (t _ {1} + t _ {2})} \mathbf {x} (0) = e ^ {A t _ {2}} e ^ {A t _ {1}} \mathbf {x} (0).$$

Since this must hold for any vector $\mathbf{x}(0)$ , it follows that

$$e ^ {A (t _ {1} + t _ {2})} = e ^ {A t _ {2}} e ^ {A t _ {1}}.$$

The argument is repeated with a first step of $t_{2}$ followed by a step of $t_{1}$ to establish the second equation of Property II. ♦

◆ Property III $(e^{At})^{-1}=e^{-At}$

To see this, write

$$e ^ {A t} e ^ {- A t} = e ^ {A t} e ^ {A (- t)} = e ^ {A (t - t)} = e ^ {A 0} = I.$$

This also shows that $e^{At}$ always has an inverse.

◆ Property IV $e^{A^{T}t} = (e^{At})^{T}$

This follows by transposition of each side of Equation 3.8 and the fact that $(A^k)^T = (A^T)^k$ .

◆ Property V $Ae^{At} = e^{At} A$

It is seen that

$$A (A ^ {k} t ^ {k}) = A ^ {k + 1} t ^ {k} = (A ^ {k} t ^ {k}) A$$

so that pre- or postmultiplying Equation 3.8 by A yields the same result.

◆ Property VI $\frac{d}{dt}e^{At}=Ae^{At}$

We write

$$\dot {\mathbf {x}} = \left(\frac {d}{d t} e ^ {A t}\right) \mathbf {x} _ {0} = A \mathbf {x} = A e ^ {A t} \mathbf {x} _ {0}.$$

The result follows from the fact that this equality must hold for all $x_{0}$ .
