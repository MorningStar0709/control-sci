# 8.2 LAPLACE TRANSFORMATION

The Laplace transform converts the function f (t) from the time domain to the domain of the complex variable s, and is defined by

$$\mathscr {L} \{f (t) \} = F (s) = \int_ {0} ^ {\infty} f (t) e ^ {- s t} d t \tag {8.1}$$

The Laplace transform variable s = ?? + j?? is a complex variable where ?? and ?? are the real and imaginary parts, respectively. The operation defined by Eq. (8.1) can be stated as “the Laplace transform of f (t) is the complex function F(s).” Typically, the uppercase letter is used for the Laplace transform of the corresponding time function (lowercase letter) and the parenthetical s indicates that the complex (Laplace) variable is the independent variable. The Laplace transform converts an ordinary differential equation (ODE) into an algebraic equation in s, which can be easily manipulated. The inverse operation

$$\mathscr {L} ^ {- 1} \{F (s) \} = f (t) \tag {8.2}$$

converts the complex function $F ( s )$ into the time function f (t) and is known as the “inverse Laplace transform of $F ( s )$ .”
