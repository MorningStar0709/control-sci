# Specifications for the Controller Problem

The purpose of regulation is to keep process variables close to specified values in spite of process disturbances and variations in process dynamics.

Minimum-variance control. For regulation of important quality variables, it is often possible to state objective criteria for regulation performance. A common situation is illustrated in Fig. 6.7, which shows the distribution of the quality variables. It is often specified that a certain percentage of the production should be at a quality level above a given value. By reducing the quality variations, it is then possible to move the set point closer to the target. The improved performance can be expressed in terms of reduced consumption of energy or raw material or increased production. It is thus possible to express reductions in quality variations directly in economic terms.

For processes with a large production, reductions of a fraction of a percent can amount to a large sum of money. For example, a reduction in moisture variation of 1% in paper-machine control can amount to savings of \$100,000 per year.

If the variations in quality can be expressed by Gaussian distributions, the criterion would simply be to minimize the variance of the quality variables. In these problems, the required control actions are irrelevant as long as they do not cause excessive wear or excessively large signals. A control strategy that minimizes the variance of the process output is called minimum-variance control.

Optimal control. Minimum-variance control is a typical example of how a control problem can be specified as an optimization problem. In a more general case, it is not appropriate to minimize the variance of the output. Instead there will be a criterion of the type

$$\mathrm{E} \int_ {t _ {0}} ^ {t _ {1}} g (x (s), u (s)) d s$$

where x is the state variable, u is the control variable, and E denotes the mean value. An example of such a criterion is given next.
