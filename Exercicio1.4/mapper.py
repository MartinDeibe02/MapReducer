#!/usr/bin/python

import sys

max_venta = 0

for line in sys.stdin:
    data = line.strip().split("\t")
    date, time, store, item, cost, payment = data

    cost = float(cost)

    if cost > max_venta:
        max_venta = cost

print("La venta mas alta fue " + str(max_venta))

