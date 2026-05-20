# Cancellation of Poles and Zeros

In Sec. 5.2 it was assumed that no process poles or zeros are canceled by the controller. In some cases it is possible to cancel process poles and zeros that are well damped. This is done in several design methods. Assume that the polynomials A and B are factored as

$$
\begin{array}{l} \boldsymbol {A} = \boldsymbol {A} ^ {+} \boldsymbol {A} ^ {-} \\ \boldsymbol {B} = \boldsymbol {B} ^ {+} \boldsymbol {B} ^ {-} \end{array} \tag {5.20}
\boldsymbol {B} = \boldsymbol {B} ^ {+} \boldsymbol {B} ^ {-}
$$

where $A^{+}$ and $B^{+}$ are the factors that can be canceled. To obtain unique factorizations polynomials $A^{+}$ and $B^{+}$ are chosen to be monic. In this section we will drop all arguments indicating the independent variable in the polynomials to simplify the writing. The polynomials $A^{+}$ and $B^{+}$ must have all their roots inside the unit disc. Because a process pole that is canceled must be a controller zero and vice versa, it follows that the polynomials R, S, and T have the following structure:

$$\boldsymbol {R} = \boldsymbol {B} ^ {+} \bar {\boldsymbol {R}}S = A ^ {-} \bar {S} \tag {5.21}\boldsymbol {T} = \boldsymbol {A} ^ {-} \bar {\boldsymbol {T}}$$

It follows from Eq. (5.4) that the characteristic polynomial of the closed-loop system is

$$\boldsymbol {A} _ {c l} = \boldsymbol {A} \boldsymbol {R} + \boldsymbol {B} \boldsymbol {S} = \boldsymbol {A} ^ {+} \boldsymbol {B} ^ {+} \left(\boldsymbol {A} ^ {-} \bar {\boldsymbol {R}} + \boldsymbol {B} ^ {-} \bar {\boldsymbol {S}}\right) = \boldsymbol {A} ^ {+} \boldsymbol {B} ^ {+} \bar {\boldsymbol {A}} _ {c l} \tag {5.22}$$

The polynomials $A^{+}$ and $B^{+}$ , which are canceled, are thus factors of the closed-loop characteristic polynomial $A_{cl}$ . It is natural to factor the characteristic polynomial as $A_{cl} = A_{c}A_{o}$ , where

$$A _ {c} = B ^ {+} \bar {A} _ {c}\boldsymbol {A} _ {o} = \boldsymbol {A} ^ {+} \bar {\boldsymbol {A}} _ {o} \tag {5.23}$$

Cancelling the common factors in Eq. (5.22) we find that polynomials $\bar{R}$ and $\bar{S}$ satisfy

$$A ^ {-} \bar {R} + B ^ {-} \bar {S} = \bar {A} _ {c l} = \bar {A} _ {c} \bar {A} _ {o} \tag {5.24}$$

The minimum-degree causal controller is obtained by choosing the unique solution with $\deg\bar{S}<\deg A^{-}$ . The control (5.2) law can be written as

$$B ^ {+} \bar {R} u = A ^ {+} \bar {T} u _ {c} - A ^ {+} \bar {S} y$$

Hence
