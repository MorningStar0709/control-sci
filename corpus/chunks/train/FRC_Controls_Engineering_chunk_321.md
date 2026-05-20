# 9.7.1 Predict and update equations

One first does a forward pass with the typical Kalman filter equations and stores the results. Then one can use the Rauch-Tung-Striebel (RTS) algorithm to do the backward pass. Theorem 9.7.1 shows the predict and and update steps for the forward and backward passes for a Kalman smoother at the kth timestep.

See section 3 of https://users.aalto.fi/\~ssarkka/course\_k2011/pdf/handout7.pdf for a derivation of the Rauch-Tung-Striebel smoother.
