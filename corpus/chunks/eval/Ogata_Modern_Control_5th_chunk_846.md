$$
\begin{array}{l} \mathbf {W} \left[ \begin{array}{c c c} 0 & 1 & 0 \\ 0 & 0 & 1 \\ - a _ {3} & - a _ {2} & - a _ {1} \end{array} \right] = \left[ \begin{array}{c c c} a _ {2} & a _ {1} & 1 \\ a _ {1} & 1 & 0 \\ 1 & 0 & 0 \end{array} \right] \left[ \begin{array}{c c c} 0 & 1 & 0 \\ 0 & 0 & 1 \\ - a _ {3} & - a _ {2} & - a _ {1} \end{array} \right] \\ = \left[ \begin{array}{c c c} - a _ {3} & 0 & 0 \\ 0 & a _ {1} & 1 \\ 0 & 1 & 0 \end{array} \right] \\ \end{array}
$$

The right-hand side of Equation (10–154) is

$$
\begin{array}{l} \left[ \begin{array}{c c c} 0 & 0 & - a _ {3} \\ 1 & 0 & - a _ {2} \\ 0 & 1 & - a _ {1} \end{array} \right] \mathbf {W} = \left[ \begin{array}{c c c} 0 & 0 & - a _ {3} \\ 1 & 0 & - a _ {2} \\ 0 & 1 & - a _ {1} \end{array} \right] \left[ \begin{array}{c c c} a _ {2} & a _ {1} & 1 \\ a _ {1} & 1 & 0 \\ 1 & 0 & 0 \end{array} \right] \\ = \left[ \begin{array}{c c c} - a _ {3} & 0 & 0 \\ 0 & a _ {1} & 1 \\ 0 & 1 & 0 \end{array} \right] \\ \end{array}
$$

Thus, we see that Equation (10–154) holds true. Hence, we have proved Equation (10–153).

Next we shall show that

$$
\mathbf {C Q} = \left[ \begin{array}{c c c} 0 & 0 & 1 \end{array} \right]
$$

or

$$
\mathbf {C} (\mathbf {W N} ^ {*}) ^ {- 1} = \left[ \begin{array}{c c c} 0 & 0 & 1 \end{array} \right]
$$

Notice that

$$
\begin{array}{l} [ 0 \quad 0 \quad 1 ] (\mathbf {W N} ^ {*}) = [ 0 \quad 0 \quad 1 ] \left[ \begin{array}{c c c} a _ {2} & a _ {1} & 1 \\ a _ {1} & 1 & 0 \\ 1 & 0 & 0 \end{array} \right] \left[ \begin{array}{c} \mathbf {C} \\ \mathbf {C A} \\ \mathbf {C A} ^ {2} \end{array} \right] \\ = \left[ \begin{array}{l l l} 1 & 0 & 0 \end{array} \right] \left[ \begin{array}{c} \mathbf {C} \\ \mathbf {C A} \\ \mathbf {C A ^ {2}} \end{array} \right] = \mathbf {C} \\ \end{array}
$$

Hence, we have shown that

$$[ 0 \quad 0 \quad 1 ] = \mathbf {C} (\mathbf {W N} ^ {*}) ^ {- 1} = \mathbf {C Q}$$

Next define

$$\mathbf {x} = \mathbf {Q} \hat {\mathbf {x}}$$

Then Equation (10–151) becomes

$$\dot {\hat {\mathbf {x}}} = \mathbf {Q} ^ {- 1} \mathbf {A} \mathbf {Q} \hat {\mathbf {x}} + \mathbf {Q} ^ {- 1} \mathbf {B} u \tag {10-155}$$

and Equation (10–152) becomes

$$y = \mathbf {C Q} \hat {\mathbf {x}} + D u \tag {10-156}$$

Referring to Equation (10–153), Equation (10–155) becomes
