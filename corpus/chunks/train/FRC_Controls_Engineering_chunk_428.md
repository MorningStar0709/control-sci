# 15.3.1 Model-free

Model-free path planning methods use geometric relationships to enforce convergence to a desired pose. They’re ideal for those who want to avoid system modeling and don’t care about the exact path the robot takes between two points. Methods in this category include pure pursuit[1] and guiding vector fields[2].

Model-free methods satisfy the needs of most teams and save them tuning time, but they do impose a performance ceiling; higher performance necessarily requires reasoning about the robot’s dynamics and physical constraints.
