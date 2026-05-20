# 10.2.2 Weights

We need a way to combine the dierent performance measures into a single cost. We can dene cost as the absolute dierence between the performance and our specs. We will adjust the system to minimize cost, but dierent performance criteria may conict with each other1. For example, what if we get really good settling time, but horrible overshoot? We need a score which potentially combines all four of our measures in to a single number. We will use a combined score as follows:

$$S = w _ {1} \times | T _ {s} - T _ {s d} | + w _ {2} \times | \% O S - \% O S _ {d} | + w _ {3} \times | S S E - S S E _ {d} | + w _ {4} \times (\max (u (t))) + w _ {5} \times | g m - g m _ {d} |$$

where $w _ { i }$ are weights which add up to 1. We dene the weight vector to be

$$
w = \left[ \begin{array}{c} w _ {1} \\ w _ {2} \\ w _ {3} \\ w _ {4} \\ w _ {5} \end{array} \right]
$$

There is one remaining problem with this scheme which is that the dierent performance measures have dierent numerical values and units which can mess up the weights. For example, since $T s$ might be only 0.2, if all weights are equal, it would not count much in the nal score if max $( u ( t ) ) = 2 0 0 0$ . To equalize the inuence of each performance criterion, we will normalize the dierence as follows:

$$S = w _ {1} \times | T _ {s} - T _ {s d} | / T _ {s d} + w _ {2} \times | \% O S - \% O S _ {d} | / \% O S _ {d} + w _ {3} \times | S S E - S S E _ {d} | / S S E _ {d} + w _ {4} \times \max (u (t)) / u _ {m a x} + w _ {5} \times | g m - g m _ {d} | / g m _ {d}$$

or more compactly

$$S = \Sigma_ {i} w _ {i} \frac {C _ {i}}{C _ {i D}}$$

where $C _ { i D }$ is the desired value for cost component $C _ { i } .$

Generally all the specications will be given as inputs to the design problem. $u _ { m a x }$ must be set by the actuator (motors, hydraulics, etc) specication. Alternatively, if the actuator is not specied yet, we can experiment to see what kind of actuator is necessary for a give set of specs.

The result, S, can be viewed as a Cost of a given design, which is zero when all the specications are met.

Now the question is which weights to choose? This is another dicult question. However, since we are searching the entire design space, we do not necessarily have to choose a single weight scheme. We could dene several and nd the best design for each weight vector in a single pass through the space. In our approach, we keep track of several weighting schemes simultaneously. For example, we can track the best gains we nd for each of these dierent weight vectors as we search.

<table><tr><td>Scheme Name</td><td> $w_1$ </td><td> $w_2$ </td><td> $w_3$ </td><td> $w_4$ </td></tr><tr><td>Settling Time</td><td>1</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Overshoot</td><td>0</td><td>1</td><td>0</td><td>0</td></tr><tr><td>Steady State Error</td><td>0</td><td>0</td><td>1</td><td>0</td></tr><tr><td>Control Effort</td><td>0</td><td>0</td><td>0</td><td>1</td></tr><tr><td>Balanced</td><td>0.25</td><td>0.25</td><td>0.25</td><td>0.25</td></tr></table>
