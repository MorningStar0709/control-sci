$$
\inf _ {K \text {   stabilizing }} \left\| \left[ \begin{array}{c} K \\ I \end{array} \right] (I + P K) ^ {- 1} \left[ \begin{array}{c c} I & P \end{array} \right] \right\| _ {\infty}

= \inf _ {K \text {   stabilizing }} \left\| \left[ \begin{array}{c} K \\ I \end{array} \right] (I + P K) ^ {- 1} \tilde {M} ^ {- 1} \right\| _ {\infty} = \left(\sqrt {1 - \left\| \left[ \begin{array}{c c} \tilde {N} & \tilde {M} \end{array} \right] \right\| _ {H} ^ {2}}\right) ^ {- 1}.
$$

This implies that there is a robustly stabilizing controller for

$$P _ {\Delta} = (\tilde {M} + \tilde {\Delta} _ {M}) ^ {- 1} (\tilde {N} + \tilde {\Delta} _ {N})$$

with

$$
\left\| \left[ \begin{array}{c c} \tilde {\Delta} _ {N} & \tilde {\Delta} _ {M} \end{array} \right] \right\| _ {\infty} <   \epsilon
$$

if and only if

$$
\epsilon \leq \sqrt {1 - \left\| \left[ \begin{array}{c c} \tilde {N} & \tilde {M} \end{array} \right] \right\| _ {H} ^ {2}}.
$$

Using this stabilization result, a loop-shaping design technique is proposed. The proposed technique uses only the basic concept of loop-shaping methods, and then a robust stabilization controller for the normalized coprime factor perturbed system is used to construct the final controller.

Chapter 17 introduces the gap metric and the ν-gap metric. The frequency domain interpretation and applications of the ν-gap metric are discussed. The controller order reduction in the gap or ν-gap metric framework is also considered.

Chapter 18 considers briefly the problems of model validation and the mixed real and complex $\mu$ analysis and synthesis.

Most computations and examples in this book are done using Matlab. Since we shall use Matlab as a major computational tool, it is assumed that readers have some basic working knowledge of the Matlab operations (for example, how to input vectors and matrices). We have also included in this book some brief explanations of Matlab, Simulink R , Control System Toolbox, and $\mu$ Analysis and Synthesis Toolbox1 commands. In particular, this book is written consistently with the $\mu$ Analysis and Synthesis Toolbox. (Robust Control Toolbox, LMI Control Toolbox, and other software packages may equally be used with this book.) Thus it is helpful for readers to have access to this toolbox. It is suggested at this point to try the following demo programs from this toolbox.

msdemo1   
msdemo2

We shall introduce many more Matlab commands in the subsequent chapters.
