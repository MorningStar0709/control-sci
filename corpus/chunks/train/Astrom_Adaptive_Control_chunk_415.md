# Design Calculations

The design calculations are an important part of indirect adaptive systems. Theoretically, the design procedure is represented by the function $\chi$ , which maps process parameters $\hat{\theta}$ to controller parameters $\nu$ . The properties of $\chi$ will, of course, depend on the parameterization of the model and the design procedure chosen. The function can often be quite complicated. It is important that the map gives unique controller parameters and that there are no singularities in the map. We discuss the properties of the map in some simple cases.

Consider the process model

$$A y = B u \tag {6.34}$$

where it is assumed that $A$ has degree $n$ and $B$ has degree $n - 1$ . The model thus has $2n$ parameters. If pole placement design is used, the controller parameters are given by

$$A R + B S = A _ {o} A _ {m} \tag {6.35}$$

where R and S have the same degree m as the observer polynomial $A_{o}$ . The minimum-degree solution corresponds to m = n - 1, but an observer of higher order is often preferable to improve the robustness of the system. Without loss of generality, R can be monic. The controller then has $2m + 1$ parameters. The function $\chi$ is thus a map from $R^{2n}$ to $R^{2m+1}$ , where $m \geq n - 1$ . Since Eq. (6.35) becomes singular when polynomials A and B have a common factor, it follows that the map $\chi$ has singularities. The problem with design singularities is illustrated by an example.
