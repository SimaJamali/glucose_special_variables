# glucose_special_variables
Using Bridge, HighCentrality and HighDegree variables in SAT solvers
Directory overview:
==================

glpb_a_b/                 Glucose Simp solver modified to bump bridge variables more.
glpb_i_hc/                Glucose Simp solver modified to initially bump HighCenterality variables more.
glbd/                     Glucose Simp solver modified to favor bridge variables in clause deletion.
gl_altered                Glucose Simp with some additional blocks to read community files and find special variables.
louvain.py                Community Detection
networkx_centrality       Computing Centrality Scores
README



======================================================================
Like minisat....

cd { $solver/simp }
make rs
