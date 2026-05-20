# The Minimum-Phase Assumption

In Theorem 6.7 and for the MRAS the process is required to be minimum-phase. This assumption is used to conclude that the input signal is bounded when the output is bounded. The minimum-variance controller, which cancels the open-loop process zeros, cannot be used when the process is nonminimum-phase.

Instead, the LQG self-tuner or the moving-average controller with increased prediction horizon can be used.

It should be remarked that sampled data systems often can be non-minimum-phase because of "sampling zeros" even if the continuous-time system that is sampled is minimum-phase. These zeros are given by the following theorem.
