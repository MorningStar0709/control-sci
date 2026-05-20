# ALGORITHM 3.5 A hybrid self-tuner

Data: Given polynomials $A_{o}$ and $A_{m}$ .

Step 1: Estimate parameters of polynomials A and B in the model

$$A y = B u$$

Step 2: Estimate parameters of polynomials R and S in Eq. (3.35) where B is the estimate obtained in Step 1.

Step 3: Use the control law

$$R u = T u _ {c} - S y$$

where R and S are obtained from Step 2 and $T = t_{0}A_{o}$ where

$$t _ {0} = \frac {A _ {m} (1)}{B (1)}$$

Remark 1. Instead of being computed, polynomial T can also be estimated by replacing Step 2 by the following step:

Step 2': Estimate parameters of polynomials R and S and $t_{0}$ from the model

$$
\begin{array}{l} e (t) = y (t) - y _ {m} (t) = \frac {B}{A _ {o} A _ {m}} \left(R u (t) + S y (t) - t _ {0} A _ {o} u _ {c} (t)\right) \\ = B ^ {*} \left(R ^ {*} u _ {f} (t - d _ {0}) + S ^ {*} y _ {f} (t - d _ {0}) - t _ {0} A _ {v} ^ {*} u _ {c f} (t - d _ {0})\right) \tag {3.36} \\ \end{array}
$$

where $B$ is the polynomial obtained in Step 1. It is then assumed that $\deg A_m = \deg A$ .

Remark 2. Instead of the Diophantine equation being solved at each step, two process models are estimated. This implies that an additional iteration of the least-squares estimator has to be done at each sampling time.
