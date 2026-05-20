# Tuners for Standard Process Controllers

There are many products for tuning of standard controllers of PID type. Leeds and Northrup announced a PID controller with a self-tuning option in 1981. SattControl in Sweden announced auto-tuning for PID controllers in a small DDC system in 1984 and a single-loop controller with auto-tuning in 1986. Practically all PID controllers that come on the market today have some kind of built-in automatic tuning or adaptation. There are four main solutions for the tuners for standard controllers:

• A parametric model approach,   
• A nonparametric model approach,   
- External tuning devices, and   
- Tuning tools in distributed control systems.

The main idea in the parametric model controllers is to make an experiment, usually in open loop, and estimate a first- or second-order model with time delay. The input signals are usually steps, but pulses or pseudo-random binary sequence (PRBS) signals are also used. The parameters of a PI or PID controller are then determined by using empirical tuning rules or a pole placement technique. Typical products in this category are Protonic from Hartman & Braun and UDC 6000 from Honeywell.

In the nonparametric model approach, a point on the Nyquist curve is generally estimated by using relay feedback. Compare the auto-tuning discussed in Chapter 8. On the basis of this information a modified set of Ziegler-Nichols tuning rules are used to determine the parameters of the controller. SattControl ECA40 and Fisher-Rosemount DPR900 are typical of this category.

The tuning aids discussed above are built-in features in the standard controllers. The operator initiates tuning by pushing a button or giving a command. The external tuning tools are special types of equipment that are connected to the process for the tuning or commissioning and then removed. The experiments are usually done with the process in open loop. The external tuner then determines suitable controller parameters. The new parameters are often entered manually by the operator. Since the external tuner can be used for different types of standard controllers, it must have detailed knowledge about the parameterization and implementation of algorithms from different manufacturers. Examples of external tuning tools are Supertuner from Toyo Systems in Japan, Protuner from Techmation in Arizona, PIDWIZ from BST Control in Illinois, and SIEPID from Siemens in Germany.

Tuning tools have also been introduced in distributed control systems. Because of the available computing power, it is possible to have very good human-machine interfaces and several options for tuning. Honeywell has a system called Looptune; Fisher-Rosemount Systems has a product called Intelligent Tuner.
