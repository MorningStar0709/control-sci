# 11.6.1 Inverse kinematics

First, we’ll derive the front-left wheel kinematics.

$$\vec {v} _ {f l} = v _ {x} \hat {i} + v _ {y} \hat {j} + \omega \hat {k} \times (r _ {f l _ {x}} \hat {i} + r _ {f l _ {y}} \hat {j})\vec {v} _ {f l} = v _ {x} \hat {i} + v _ {y} \hat {j} + \omega r _ {f l _ {x}} \hat {j} - \omega r _ {f l _ {y}} \hat {i}\vec {v} _ {f l} = (v _ {x} - \omega r _ {f l _ {y}}) \hat {i} + (v _ {y} + \omega r _ {f l _ {x}}) \hat {j}$$

Project the front-left wheel onto its wheel vector.

$$v _ {f l} = ((v _ {x} - \omega r _ {f l _ {y}}) \hat {i} + (v _ {y} + \omega r _ {f l _ {x}}) \hat {j}) \cdot \frac {\hat {i} - \hat {j}}{\sqrt {2}}v _ {f l} = ((v _ {x} - \omega r _ {f l _ {y}}) - (v _ {y} + \omega r _ {f l _ {x}})) \frac {1}{\sqrt {2}}v _ {f l} = (v _ {x} - \omega r _ {f l _ {y}} - v _ {y} - \omega r _ {f l _ {x}}) \frac {1}{\sqrt {2}}v _ {f l} = (v _ {x} - v _ {y} - \omega r _ {f l _ {y}} - \omega r _ {f l _ {x}}) \frac {1}{\sqrt {2}}v _ {f l} = (v _ {x} - v _ {y} - \omega (r _ {f l _ {x}} + r _ {f l _ {y}})) \frac {1}{\sqrt {2}}v _ {f l} = \frac {1}{\sqrt {2}} v _ {x} - \frac {1}{\sqrt {2}} v _ {y} - \frac {1}{\sqrt {2}} \omega (r _ {f l _ {x}} + r _ {f l _ {y}}) \tag {11.8}$$

Next, we’ll derive the front-right wheel kinematics.

$$\vec {v} _ {f r} = v _ {x} \hat {i} + v _ {y} \hat {j} + \omega \hat {k} \times (r _ {f r _ {x}} \hat {i} + r _ {f r _ {y}} \hat {j})\vec {v} _ {f r} = v _ {x} \hat {i} + v _ {y} \hat {j} + \omega r _ {f r _ {x}} \hat {j} - \omega r _ {f r _ {y}} \hat {i}\vec {v} _ {f r} = (v _ {x} - \omega r _ {f r _ {y}}) \hat {i} + (v _ {y} + \omega r _ {f r _ {x}}) \hat {j}$$

Project the front-right wheel onto its wheel vector.

$$v _ {f r} = ((v _ {x} - \omega r _ {f r _ {y}}) \hat {i} + (v _ {y} + \omega r _ {f r _ {x}}) \hat {j}) \cdot (\hat {i} + \hat {j}) \frac {1}{\sqrt {2}}v _ {f r} = ((v _ {x} - \omega r _ {f r _ {y}}) + (v _ {y} + \omega r _ {f r _ {x}})) \frac {1}{\sqrt {2}}v _ {f r} = (v _ {x} - \omega r _ {f r _ {y}} + v _ {y} + \omega r _ {f r _ {x}}) \frac {1}{\sqrt {2}}v _ {f r} = (v _ {x} + v _ {y} - \omega r _ {f r _ {y}} + \omega r _ {f r _ {x}}) \frac {1}{\sqrt {2}}v _ {f r} = (v _ {x} + v _ {y} + \omega (r _ {f r _ {x}} - r _ {f r _ {y}})) \frac {1}{\sqrt {2}}v _ {f r} = \frac {1}{\sqrt {2}} v _ {x} + \frac {1}{\sqrt {2}} v _ {y} + \frac {1}{\sqrt {2}} \omega (r _ {f r _ {x}} - r _ {f r _ {y}}) \tag {11.9}$$

Next, we’ll derive the rear-left wheel kinematics.
