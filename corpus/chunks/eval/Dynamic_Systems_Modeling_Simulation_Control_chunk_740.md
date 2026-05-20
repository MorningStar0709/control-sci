# B.7 COMMANDS FOR CONTROL SYSTEM ANALYSIS

MATLAB has three very powerful built-in commands for analyzing closed-loop control systems. The first command is feedback, which computes the closed-loop transfer function object sysT given the forward transfer function G(s) (as sysG) and feedback transfer function H(s) (as sysH). That is, feedback computes the closed-loop transfer function T(s) using

Table B.3 MATLAB Commands for Laplace Transform Analysis

<table><tr><td>MATLAB Command</td><td>Description</td></tr><tr><td>[r,p,k] = residue(numF,denF)</td><td>Computes the residues r, associated poles p, and direct term k (if any) for the partial-fraction expansion of  $F(s)$ =numF/denF</td></tr><tr><td>F = laplace(f)</td><td>Computes the Laplace transform of time-function f (expressed as a symbolic object using sym)</td></tr><tr><td>f = ilaplace(F)</td><td>Computes the inverse Laplace transform of F (expressed as a symbolic object using sym)</td></tr></table>

$$T (s) = \frac {G (s)}{1 + G (s) H (s)} = \frac {Y (s)}{R (s)}$$

where r(t) is the overall reference input and y(t) is the plant output. Negative feedback is assumed at the summing junction. The reader should note that once the closed-loop transfer function is obtained, the LTI commands in Table B.2 (step, impulse, etc.) can be used to obtain the closed-loop system response.

The second powerful MATLAB command is rlocus, which plots the root locus to the screen. The user must provide the open-loop transfer function G(s)H(s) as the input (as either sysGH or sysG\*sysH). The closed-loop poles can be computed for a specific forward-path gain K using rlocus, or by using the command rlocfind. The interactive command rlocfind allows the user to place a cross-hair target on any desired root-locus branch, click, and obtain the corresponding gain K and n closed-loop poles.
