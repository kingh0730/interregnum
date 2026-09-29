"""usage: uv run work/pilot/comp_v3/go.py NN [--sheet]  (pre-comps for shots 01-15)"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
import pre_0115
getattr(pre_0115, "s" + sys.argv[1])()
