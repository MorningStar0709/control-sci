# Summary of State-Space Design Method

1. The state-space design method based on the pole-placement-combined-withobserver approach is very powerful. It is a time-domain method.The desired closedloop poles can be arbitrarily placed, provided the plant is completely state controllable.   
2. If not all state variables can be measured, an observer must be incorporated to estimate the unmeasurable state variables.   
3. In designing a system using the pole-placement approach, several different sets of desired closed-loop poles need be considered, the response characteristics compared, and the best one chosen.   
4. The bandwidth of the observer controller is generally large, because we choose observer poles far to the left in the s plane. A large bandwidth passes highfrequency noises and causes the noise problem.   
5. Adding an observer to the system generally reduces the stability margin. In some cases, an observer controller may have zero(s) in the right-half s plane, which means that the controller may be stable but of nonminimum phase. In other cases, the controller may have pole(s) in the right-half s plane—that is, the controller is unstable. Then the designed system may become conditionally stable.   
6. When the system is designed by the pole-placement-with-observer approach, it is advisable to check the stability margins (phase margin and gain margin), using a

frequency-response method. If the system designed has poor stability margins, it is possible that the designed system may become unstable if the mathematical model involves uncertainties.

7. Note that for nth-order systems, classical design methods (root-locus and frequency-response methods) yield low-order compensators (first or second order). Since the observer-based controllers are nth-order Cor (N-m)th-order if the minimum-order observer is usedD for an nth-order system, the designed system will become 2nth order Cor (2n-m)th orderD. Since lower-order compensators are cheaper than higher-order ones, the designer should first apply classical methods and, if no suitable compensators can be determined, then try the pole-placementwith-observer design approach presented in this chapter.
