#!/usr/bin/python

import sys

ventas_pago = {}

for line in sys.stdin:
    data = line.strip().split("\t")
    date, time, store, item, cost, payment = data

    cost = float(cost)

    if payment in ventas_pago:
        if cost > ventas_pago[payment]:
            ventas_pago[payment] = cost
    else:
        ventas_pago[payment] = cost

for payment, max_pago in ventas_pago.items():
    print(payment + "\t" + str(max_pago))

