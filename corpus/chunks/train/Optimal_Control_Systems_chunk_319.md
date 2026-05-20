# 6.1 Constrained System

2. Thrust of a rocket engine used in a space shuttle launch control system cannot exceed a certain designed value.

3. Speed of an electric motor used in a typical speed control system cannot exceed a certain value without damaging some of the mechanical components such as bearings and shaft.

This optimal control problem for a system with constraints was addressed by Pontryagin et al., and the results were enunciated in the celebrated Pontryagin Minimum Principle [109]. In their original works, the previous optimization problem was addressed to maximize the Hamiltonian

$$\mathcal {H} (\mathbf {x} (t), \mathbf {u} (t), \boldsymbol {\lambda} (t), t) = - V (\mathbf {x} (t), \mathbf {u} (t), t) + \boldsymbol {\lambda} ^ {\prime} (t) \mathbf {f} (\mathbf {x} (t), \mathbf {u} (t), t) \tag {6.1.9}$$

which is equivalent to minimization of the Hamiltonian defined in (6.1.4). However, here and throughout this book, we define the Hamiltonian as in (6.1.4) and use Pontryagin Minimum Principle (PMP) or simply Pontryagin Principle. Before we consider the optimal control system with control constraints, a historical perspective is in order regarding Pontryagin Minimum Principle [52, 53].

Lev Semyonovich Pontryagin (born September 3, 1908, Moscow, Russia and died May 3, 1988, Moscow, Russia) lost his eyesight when he was about 14 years old due to an explosion. His mother, although does not know mathematics herself, became his tutor by just reading and describing the various mathematical symbols as they appeared to her.
