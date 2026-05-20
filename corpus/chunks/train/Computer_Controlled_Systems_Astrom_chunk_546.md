# Example 9.2 Importance of operational aspects

To illustrate that the operational aspects and security are important we take two examples from practical implementations.

The first example is a control system for a steel rolling mill. In this application the control, signal conditioning and logic took about 30% of the code and the rest was related to operator interface and security measures.

The second example is the implementation of an autotuner based on relay feedback. A straightforward implementation of the tuning algorithm could be done in 1.5 pages of C code. The commercial algorithm with all bells and whistles needed for operator communication and security required 15 pages of code.
