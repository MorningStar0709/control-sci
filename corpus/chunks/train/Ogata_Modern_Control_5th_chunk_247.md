# 5–8 STEADY-STATE ERRORS IN UNITY-FEEDBACK CONTROL SYSTEMS

Errors in a control system can be attributed to many factors. Changes in the reference input will cause unavoidable errors during transient periods and may also cause steadystate errors. Imperfections in the system components, such as static friction, backlash, and amplifier drift, as well as aging or deterioration, will cause errors at steady state. In this section, however, we shall not discuss errors due to imperfections in the system components. Rather, we shall investigate a type of steady-state error that is caused by the incapability of a system to follow particular types of inputs.

Any physical control system inherently suffers steady-state error in response to certain types of inputs. A system may have no steady-state error to a step input, but the same system may exhibit nonzero steady-state error to a ramp input. (The only way we may be able to eliminate this error is to modify the system structure.) Whether a given system will exhibit steady-state error for a given type of input depends on the type of open-loop transfer function of the system, to be discussed in what follows.

Classification of Control Systems. Control systems may be classified according to their ability to follow step inputs, ramp inputs, parabolic inputs, and so on. This is a reasonable classification scheme, because actual inputs may frequently be considered combinations of such inputs. The magnitudes of the steady-state errors due to these individual inputs are indicative of the goodness of the system.

Consider the unity-feedback control system with the following open-loop transfer function $G ( s )$ :

$$G (s) = \frac {K (T _ {a} s + 1) (T _ {b} s + 1) \cdots (T _ {m} s + 1)}{s ^ {N} (T _ {1} s + 1) (T _ {2} s + 1) \cdots (T _ {p} s + 1)}$$

It involves the term $s ^ { N }$ in the denominator, representing a pole of multiplicity N at the origin.The present classification scheme is based on the number of integrations indicated by the open-loop transfer function. A system is called type 0, type 1, type 2, p , if N=0, $N = 1 , N = 2 , \ldots$ , respectively. Note that this classification is different from that of the order of a system. As the type number is increased, accuracy is improved; however, increasing the type number aggravates the stability problem. A compromise between steady-state accuracy and relative stability is always necessary.
