import math

import yaml
from scipy.spatial.distance import euclidean
import cairo

file_data = r"C:\Users\HH\PycharmProjects\data_generator\Output\hanoi1000n50 (1).yaml"
with open(file_data, 'r') as file:
    net_argc = yaml.full_load(file)

base_station = net_argc["base_station"]
print(base_station)
nodes = net_argc["nodes"]
print(nodes)
targets = net_argc["targets"]
print(targets)
rs = 40.1
rc = 80.1

with cairo.SVGSurface("Test_test.svg", 1000, 1000) as surface:
    context = cairo.Context(surface)
    context.rectangle(0, 0, 1000, 1000)
    context.set_source_rgba(1, 1, 1, 1)
    context.fill()
    context.set_line_width(1)
    context.set_source_rgba(0, 0, 0, 1)
    for node1 in nodes:
        # connect with base
        if euclidean(node1, base_station) <= rc:
            context.move_to(node1[0], node1[1])
            context.line_to(base_station[0], base_station[1])
            context.stroke()
        for node2 in nodes:
            if euclidean(node1, node2) <= rc:
                context.move_to(node1[0], node1[1])
                context.line_to(node2[0], node2[1])
                context.stroke()
    context.set_source_rgba(1, 0, 0, 1)
    for node1 in nodes:
        for target in targets:
            if euclidean(node1, target) < rs:
                print(node1, target)
                context.move_to(node1[0], node1[1])
                context.line_to(target[0], target[1])
                context.stroke()

    context.set_source_rgba(0, 0, 0, 1)
    for node in nodes:
        context.arc(node[0], node[1], 6, 0, 2*math.pi)
        context.fill()

    context.set_source_rgba(0, 1, 0, 1)
    for node in targets:
        context.arc(node[0], node[1], 6, 0, 2*math.pi)
        context.fill()

