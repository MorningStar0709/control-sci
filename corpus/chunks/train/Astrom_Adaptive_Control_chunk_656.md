# 11.5 ESTIMATOR IMPLEMENTATION

There are many issues that have to be considered in the implementation of an estimator. This section can be summarized by the following motto:

"Use only good relevant data, treat it carefully, and don't throw away useful information."

The key issue is that we want to obtain a model that is relevant for the task of control system design and that we want to track changes in the model. The tasks are influenced by many factors. In this section we discuss selection of model structure, filtering and excitation, parameter tracking, estimator windup, and robustness modifications.
