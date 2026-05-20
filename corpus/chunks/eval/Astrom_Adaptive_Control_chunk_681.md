where $n$ is the dimension of $x$ . But

$$
\begin{array}{l} \det R = \det \left( \begin{array}{l l} R _ {y} & R _ {y x} \\ R _ {x y} & R _ {x} \end{array} \right) = \det \left( \begin{array}{c c} R _ {y} & R _ {y x} \\ 0 & R _ {x} - R _ {x y} R _ {y} ^ {1} R _ {y x} \end{array} \right) \\ = \det R _ {y} \cdot \det \left(R _ {x} - R _ {x y} R _ {y} ^ {- 1} R _ {y x}\right) = \det R _ {y} \cdot \det R _ {z} \\ \end{array}
$$

Hence

$$f (x | y) = (2 \pi) ^ {n / 2} (\det R _ {z}) ^ {- 1 / 2} e ^ {- (1 / 2) z ^ {T} R _ {z} ^ {- 1} z}$$

where $z$ is given by Eq. (11.30) and $R_{z}$ by Eq. (11.31).

The first part of the theorem is thus proved. To show the second part, notice that Eq. (11.27) is

$$
R = \rho \left( \begin{array}{l l} D _ {y} & D _ {y} K ^ {T} \\ K D _ {y} & L _ {x} D _ {x} L _ {x} ^ {T} + K D _ {y} K ^ {T} \end{array} \right)
$$

Identification of the different terms gives

$$
\begin{array}{l} R _ {y} = \rho D _ {y} \\ R _ {x y} = \rho K D _ {y} \\ R _ {x} = \rho \left(L _ {x} D _ {x} L _ {x} ^ {T} + K D _ {y} K ^ {T}\right) \\ \end{array}
$$

Hence

$$R _ {x y} R _ {y} ^ {- 1} = K$$

and

$$R _ {x \mid y} = R _ {x} - R _ {x y} R _ {y} ^ {- 1} R _ {y x} = \rho L _ {x} D _ {x} L _ {x} ^ {T}$$

Remark. It follows from the theorem that the calculation of the conditional mean of a Gaussian random variable is equivalent to transforming the joint covariance matrix of the variables to the form of Eq. (11.27). Notice that this form may be viewed as a square root representation of R. □
