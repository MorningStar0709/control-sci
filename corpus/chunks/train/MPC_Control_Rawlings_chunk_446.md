# 4.2 Full Information Estimation

Of all the estimators considered in this chapter, full information estimation will prove to have the best theoretical properties in terms of stability and optimality. Unfortunately, it will also prove to be computationally intractable except for the simplest cases, such as a linear system model. Its value therefore lies in clearly defining what is desirable in a state estimator. One method for practical estimator design therefore is to come as close as possible to the properties of full information estimation while maintaining a tractable online computation. This design philosophy leads directly to moving horizon estimation (MHE).

<table><tr><td></td><td>System variable</td><td>Decision variable</td><td>Optimal decision</td></tr><tr><td>state</td><td>x</td><td> $\chi$ </td><td> $\hat{x}$ </td></tr><tr><td>process disturbance</td><td>w</td><td> $\omega$ </td><td> $\hat{w}$ </td></tr><tr><td>measured output</td><td>y</td><td> $\eta$ </td><td> $\hat{y}$ </td></tr><tr><td>measurement disturbance</td><td>v</td><td>v</td><td> $\hat{v}$ </td></tr></table>

Table 4.1: System and state estimator variables.

First we define some notation necessary to distinguish the system variables from the estimator variables. We have already introduced the system variables $( x , w , y , \nu )$ . In the estimator optimization problem, these have corresponding decision variables, which we denote $( \chi , \omega , \eta , \nu )$ . The optimal decision variables are denoted $( \hat { x } , \hat { w } , \hat { y } , \hat { \upsilon } )$ and these optimal decisions are the estimates provided by the state estimator. This notation is summarized in Table 4.1. Next we summarize the relationships between these variables

$$
\begin{array}{l} x ^ {+} = f (x, w) \quad y = h (x) + v \\ \chi^ {+} = f (\chi , \omega) \quad y = h (\chi) + \nu \\ \hat {x} ^ {+} = f (\hat {x}, \hat {w}) \quad y = h (\hat {x}) + \hat {v} \\ \end{array}
$$

Notice that it is always the system measurement y that appears in the second column of equations. We can also define the decision variable output, $\eta \ : = \ : h ( \chi )$ , but notice that ν measures the fitting error, $\nu =$ $y - h ( \chi )$ , and we must use the system measurement y and not η in this relationship. Therefore, we do not satisfy a relationship like $\eta =$ $h ( \chi ) + \nu _ { ; }$ , but rather
