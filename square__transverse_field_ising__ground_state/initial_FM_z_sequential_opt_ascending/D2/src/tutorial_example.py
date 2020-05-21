#!/usr/bin/env python3

import subprocess

import numpy as np

import toml

import os
os.environ["OMP_NUM_THREADS"] = "1"


num_g = 31
min_g = 0.0
max_g = 3.0

total = 0
for idx, g in enumerate(np.linspace(min_g, max_g, num=num_g)):
    print("Caclulation Process: {}/{}".format(idx+1, num_g))
    with open("simple.toml") as f:
        dict_toml = toml.load(f)
    dict_toml["parameter"]["general"]["output"] = "output_{}".format(idx)
    dict_toml["parameter"]["general"]["tensor_save"] = "output_wf_{}".format(idx)
    if idx>0:
        dict_toml["parameter"]["general"]["tensor_load"] = "output_wf_{}".format(idx-1)
    dict_toml["model"]["G"] = float(g)
    with open("simple_{}.toml".format(idx), 'w') as f:
        toml.dump(dict_toml, f)
    cmd = "python tenes_simple simple_{}.toml -o std_{}.toml".format(idx, idx)
    subprocess.call(cmd.split())
#    if idx==0:
#        with open("std_{}.toml".format(idx)) as f:
#            dict_toml = toml.load(f)
#        dict_toml["tensor"]["unitcell"][0]["initial_state"] = [1.0, 1.0] # FM (x direction)
#        with open("std_{}.toml".format(idx), 'w') as f:
#            toml.dump(dict_toml, f)
    cmd = "python tenes_std std_{}.toml -o input_{}.toml".format(idx, idx)
    subprocess.call(cmd.split())
    cmd = "./tenes input_{}.toml".format(idx)
    subprocess.call(cmd.split())
