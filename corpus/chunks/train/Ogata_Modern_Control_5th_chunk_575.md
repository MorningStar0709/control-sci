# 8–1 INTRODUCTION

In previous chapters, we occasionally discussed the basic PID controllers. For example, we presented electronic, hydraulic, and pneumatic PID controllers. We also designed control systems where PID controllers were involved.

It is interesting to note that more than half of the industrial controllers in use today are PID controllers or modified PID controllers.

Because most PID controllers are adjusted on-site, many different types of tuning rules have been proposed in the literature. Using these tuning rules, delicate and fine tuning of PID controllers can be made on-site. Also, automatic tuning methods have been developed and some of the PID controllers may possess on-line automatic tuning capabilities. Modified forms of PID control, such as I-PD control and multi-degrees-offreedom PID control, are currently in use in industry. Many practical methods for bumpless switching (from manual operation to automatic operation) and gain scheduling are commercially available.

The usefulness of PID controls lies in their general applicability to most control systems. In particular, when the mathematical model of the plant is not known and therefore analytical design methods cannot be used, PID controls prove to be most useful. In the field of process control systems, it is well known that the basic and modified PID control schemes have proved their usefulness in providing satisfactory control, although in many given situations they may not provide optimal control.

In this chapter we first present the design of a PID controlled system using Ziegler and Nichols tuning rules.We next discuss a design of PID controller with the conventional frequency-response approach, followed by the computational optimization approach to design PID controllers. Then we introduce modified PID controls such as PI-D control and I-PD control.Then we introduce multi-degrees-of-freedom control systems, which can satisfy conflicting requirements that single-degree-of-freedom control systems cannot. (For the definition of multi-degrees-of-freedom control systems, see Section 8–6.)
