$$
P \star K = \left[ \begin{array}{c c c} \bar {A} & \bar {B} _ {1} & \bar {B} _ {2} \\ \hline \bar {C} _ {1} & \bar {D} _ {1 1} & \bar {D} _ {1 2} \\ \bar {C} _ {2} & \bar {D} _ {2 1} & \bar {D} _ {2 2} \end{array} \right] = \left[ \begin{array}{c c} \bar {A} & \bar {B} \\ \hline \bar {C} & \bar {D} \end{array} \right]
$$

where

$$
\begin{array}{l} \bar {A} = \left[ \begin{array}{c c} A + B _ {2} \tilde {R} ^ {- 1} D _ {K 1 1} C _ {2} & B _ {2} \tilde {R} ^ {- 1} C _ {K 1} \\ B _ {K 1} R ^ {- 1} C _ {2} & A _ {K} + B _ {K 1} R ^ {- 1} D _ {2 2} C _ {K 1} \end{array} \right] \\ \bar {B} = \left[ \begin{array}{c c} B _ {1} + B _ {2} \tilde {R} ^ {- 1} D _ {K 1 1} D _ {2 1} & B _ {2} \tilde {R} ^ {- 1} D _ {K 1 2} \\ B _ {K 1} R ^ {- 1} D _ {2 1} & B _ {K 2} + B _ {K 1} R ^ {- 1} D _ {2 2} D _ {K 1 2} \end{array} \right] \\ \bar {C} = \left[ \begin{array}{c c} C _ {1} + D _ {1 2} D _ {K 1 1} R ^ {- 1} C _ {2} & D _ {1 2} \tilde {R} ^ {- 1} C _ {K 1} \\ D _ {K 2 1} R ^ {- 1} C _ {2} & C _ {K 2} + D _ {K 2 1} R ^ {- 1} D _ {2 2} C _ {K 1} \end{array} \right] \\ \bar {D} = \left[ \begin{array}{c c} D _ {1 1} + D _ {1 2} D _ {K 1 1} R ^ {- 1} D _ {2 1} & D _ {1 2} \tilde {R} ^ {- 1} D _ {K 1 2} \\ D _ {K 2 1} R ^ {- 1} D _ {2 1} & D _ {K 2 2} + D _ {K 2 1} R ^ {- 1} D _ {2 2} D _ {K 1 2} \end{array} \right] \\ R = I - D _ {2 2} D _ {K 1 1}, \quad \tilde {R} = I - D _ {K 1 1} D _ {2 2}. \\ \end{array}
$$

In fact, it is easy to show that

$$
\begin{array}{l} \bar {A} = \left[ \begin{array}{c c} A & B _ {2} \\ C _ {2} & D _ {2 2} \end{array} \right] \star \left[ \begin{array}{c c} D _ {K 1 1} & C _ {K 1} \\ B _ {K 1} & A _ {K} \end{array} \right], \\ \bar {B} = \left[ \begin{array}{c c} B _ {1} & B _ {2} \\ D _ {2 1} & D _ {2 2} \end{array} \right] \star \left[ \begin{array}{c c} D _ {K 1 1} & D _ {K 1 2} \\ B _ {K 1} & B _ {K 2} \end{array} \right], \\ \bar {C} = \left[ \begin{array}{c c} C _ {1} & D _ {1 2} \\ C _ {2} & D _ {2 2} \end{array} \right] \star \left[ \begin{array}{c c} D _ {K 1 1} & C _ {K 1} \\ D _ {K 2 1} & C _ {K 2} \end{array} \right], \\ \bar {D} = \left[ \begin{array}{c c} D _ {1 1} & D _ {1 2} \\ D _ {2 1} & D _ {2 2} \end{array} \right] \star \left[ \begin{array}{c c} D _ {K 1 1} & D _ {K 1 2} \\ D _ {K 2 1} & D _ {K 2 2} \end{array} \right]. \\ \end{array}
$$

The Matlab command starp can be used to compute the star product:

$$\gg \mathbf {P} \star \mathbf {K} = \operatorname{starp} (\mathbf {P}, \mathbf {K}, \dim y, \dim u)$$

where dimy and dimu are the dimensions of y and u, respectively. In the particular case when dim(ˆz) = 0 and dim( ˆw) = 0, we have

$$\gg \mathcal {F} _ {\ell} (\mathbf {P}, \mathbf {K}) = \operatorname{starp} (\mathbf {P}, \mathbf {K})$$
