# 2.6 Extrema of Functionals with Conditions

In this section, we extend our ideas to functionals based on those developed in the last section for functions. First, we consider a functional with two variables, use the results of the previous section on the CoV, derive the necessary conditions and then extend the same for a general nth order vector case. Consider the extremization of the performance index in the form of a functional

$$J (x _ {1} (t), x _ {2} (t), t) = J = \int_ {t _ {0}} ^ {t _ {f}} V (x _ {1} (t), x _ {2} (t), \dot {x} _ {1} (t), \dot {x} _ {2} (t), t) d t \tag {2.6.1}$$

subject to the condition (plant or system equation)

$$g (x _ {1} (t), x _ {2} (t), \dot {x} _ {1} (t), \dot {x} _ {2} (t)) = 0 \tag {2.6.2}$$

with fixed-end-point conditions

$$x _ {1} (t _ {0}) = x _ {1 0}; \quad x _ {2} (t _ {0}) = x _ {2 0}x _ {1} (t _ {f}) = x _ {1 f}; \quad x _ {2} (t _ {f}) = x _ {2 f}. \tag {2.6.3}$$

Now we address this problem under the following steps.

- Step 1: Lagrangian   
- Step 2: Variations and Increment   
- Step 3: First Variation   
- Step 4: Fundamental Theorem   
- Step 5: Fundamental Lemma   
- Step 6: Euler-Lagrange Equation

\- Step 1: Lagrangian: We form an augmented functional

$$J _ {a} = \int_ {t _ {0}} ^ {t _ {f}} \mathcal {L} (x _ {1} (t), x _ {2} (t), \dot {x} _ {1} (t), \dot {x} _ {2} (t), \lambda (t), t) d t \tag {2.6.4}$$

where, $\lambda(t)$ is the Lagrange multiplier, and the Lagrangian $\mathcal{L}$ is defined as

$$
\begin{array}{l} \mathcal {L} = \mathcal {L} (x _ {1} (t), x _ {2} (t), \dot {x} _ {1} (t), \dot {x} _ {2} (t), \lambda (t), t) \\ = V \left(x _ {1} (t), x _ {2} (t), \dot {x} _ {1} (t), \dot {x} _ {2} (t), t\right) \\ + \lambda (t) g (x _ {1} (t), x _ {2} (t), \dot {x} _ {1} (t), \dot {x} _ {2} (t)) \tag {2.6.5} \\ \end{array}
$$

Note from the performance index (2.6.1) and the augmented performance index (2.6.4) that $J_{a} = J$ if the condition (2.6.2) is satisfied for any $\lambda(t)$ .

\- Step 2: Variations and Increment: Next, assume optimal values and then consider the variations and increment as

$$
\begin{array}{l} x _ {i} (t) = x _ {i} ^ {*} (t) + \delta x _ {i} (t), \quad \dot {x} _ {i} (t) = \dot {x} _ {i} ^ {*} (t) + \delta \dot {x} _ {i} (t), \quad i = 1, 2 \\ \Delta J _ {a} = J _ {a} \left(x _ {i} ^ {*} (t) + \delta x _ {i} (t), \dot {x} _ {i} ^ {*} (t) + \delta \dot {x} _ {i} (t), t\right) - J _ {a} \left(x _ {i} ^ {*} (t), \dot {x} _ {i} ^ {*} (t), t\right), \tag {2.6.6} \\ \end{array}
$$

for i = 1, 2.
