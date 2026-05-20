$$
\begin{array}{l} \mathcal {E} ((x - \hat {x} ^ {-}) \tilde {y} ^ {\prime}) \approx \sum_ {i} w ^ {i} (z ^ {i} - \hat {x} ^ {-}) (\eta^ {i} - \hat {y} ^ {-}) ^ {\prime} \\ \mathcal {E} (\tilde {y} \tilde {y} ^ {\prime}) \approx \sum_ {i} w ^ {i} (\eta^ {i} - \hat {y} ^ {-}) (\eta^ {i} - \hat {y} ^ {-}) ^ {\prime} \\ \end{array}
$$

See Julier, Uhlmann, and Durrant-Whyte (2000); Julier and Uhlmann (2004a); van der Merwe, Doucet, de Freitas, and Wan (2000) for more details on the algorithm. An added benefit of the UKF approach is that the partial derivatives $\partial f ( x , w ) / \partial x , \partial h ( x ) / \partial x$ are not required. See also (Nørgaard, Poulsen, and Ravn, 2000) for other derivative-free nonlinear filters of comparable accuracy to the UKF. See (Lefebvre, Bruyninckx, and De Schutter, 2002; Julier and Uhlmann, 2002) for an interpretation of the UKF as a use of statistical linear regression.

The UKF has been tested in a variety of simulation examples taken from different application fields including aircraft attitude estimation, tracking and ballistics, and communication systems. In the chemical process control field, Romanenko and coworkers have compared the EKF and UKF on a strongly nonlinear exothermic chemical reactor (Romanenko and Castro, 2004), and a pH system (Romanenko, Santos, and Afonso, 2004). The reactor has nonlinear dynamics and a linear measurement model, i.e., a subset of states is measured. In this case, the

UKF performs significantly better than the EKF when the process noise is large. The pH system has linear dynamics but a strongly nonlinear measurement, i.e., the pH measurement. In this case, the authors show a modest improvement in the UKF over the EKF.
