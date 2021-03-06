#!/usr/bin/env python3

from os.path import join

import numpy as np

import toml

import os
os.environ["OMP_NUM_THREADS"] = "1"


num_g = 31

for idx in range(num_g):
    try:
        with open("simple_{}.toml".format(idx)) as f:
            dict_toml = toml.load(f)
        g = dict_toml["model"]["G"]
        ene = 0.0
        mag_sz = 0.0
        mag_sx = 0.0
        with open(join("output_{}".format(idx), "density.dat")) as f:
            for line in f:
                words = line.split()
                if words[0] == 'hamiltonian':
                    ene = words[2]
                elif words[0] == 'Sz':
                    mag_sz = words[2]
                elif words[0] == 'Sx':
                    mag_sx = words[2]
        print("{} {} {} {}".format(g, ene, mag_sz, mag_sx))
    except:
        continue
