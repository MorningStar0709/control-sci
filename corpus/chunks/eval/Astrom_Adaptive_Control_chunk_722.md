# Adaptive Standard Process Controllers

The tuners discussed above do not tune the controllers continuously but only on demand from the operator. However, there are also standard controllers with adaptation, which can follow changes in the parameters of the process. The adaptive standard controllers can be divided into

• A parametric model approach,   
• A nonparametric model approach, and   
• A pattern recognition approach.

The model-based adaptive controller usually estimates a first- or second-order model with time delay using a recursive least-squares algorithm. A pole placement controller with PID structure can then be determined. Examples are the Bailey Controls CLC04 and Yokogawa SLPC-181, -281.

One example of a nonparametric adaptive controller is SattControl ECA 400. (See Fig. 1.23.) It is a development of the relay-based auto-tuner. One point of the Nyquist curve is estimated continuously by using band-pass filtering. The parameters of the controller are then determined by using a modified version of the Ziegler-Nichols tuning rules.

Expert systems or pattern recognition have also been used for adaptive tuning of standard controllers. The first was the Foxboro EXACT, which was announced in October 1984. This controller is described in more detail in the text that follows. In 1987, Yokogawa announced adaptive PID controllers, SLPC-171 and SLPC-271, which have features similar to those of Foxboro's

EXACT. Another controller in this category is Fenwal 570. The Honeywell. UDC 6000 controller uses step response analysis for automatic tuning and a rule base for adaptation. These controllers are designed to capture the skill of an experienced control engineer in rules. About 100–200 rules are typically implemented. The controllers are waiting for changes in the reference value or large upsets of the process. On the basis of the response and the tuning rules, the parameters of the controller are modified to increase the performance of the closed-loop system.

Several of the adaptive standard controllers, for example, Fisher DPR 910 and SattControl ECA400, have adaptive feedforward and the possibility to build up gain scheduling tables automatically. These features are very useful and can improve the performance considerably.

Standard controllers with more sophisticated control algorithms are now appearing on the market. One example is U.A.C. (Universal Adaptive Controller) from Process Automation Systems in British Columbia, which is based on predictive control. The controller can also handle multivariable systems.
