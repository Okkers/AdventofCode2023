import os
os.environ["PATH"] += os.pathsep + 'D:/Program Files (x86)/Graphviz2.38/bin/'
from math import lcm
from queue import Queue
from collections import defaultdict
from itertools import count
import graphviz

module_table = {}
q = Queue()
dot = graphviz.Digraph(format='png')
shape_table = {'broadcaster': 'star', 'flipflop': 'box', 'conjunction': 'ellipse'}


class Module:
    def __init__(self, name, m_type):
        self.name = name
        self.type = m_type
        self.inputs = []
        self.outputs = []
        self.flip_state = False
        self.conjunction_memory = defaultdict(bool)
        dot.node(name, shape=shape_table[m_type])

    def __repr__(self):
        return self.name
    
    def reset(self):
        self.flip_state = False
        self.conjunction_memory = defaultdict(bool)

    def pulse(self, value, sender):
        if self.type == 'broadcaster':
            for output in self.outputs:
                q.put((output, value, self.name))
        elif self.type == 'flipflop':
            if not value:
                self.flip_state = not self.flip_state
                for output in self.outputs:
                    q.put((output, self.flip_state, self.name))
        elif self.type == 'conjunction':
            self.conjunction_memory[sender] = value
            output_value = not all(self.conjunction_memory[input_module.name] for input_module in self.inputs)
            for output in self.outputs:
                q.put((output, output_value, self.name))

with open('input.txt', 'r') as f:
    for line in f.readlines():
        left, _ = line.strip().split(' -> ')
        if left.startswith('%'):
            module_table[left[1:]] = Module(left[1:], 'flipflop')
        elif left.startswith('&'):
            module_table[left[1:]] = Module(left[1:], 'conjunction')
        else:
            module_table[left] = Module('broadcaster', 'broadcaster')
with open('input.txt', 'r') as f:
    for line in f.readlines():
        left, right = line.strip().split(' -> ')
        m = module_table['broadcaster'] if left == 'broadcaster' else module_table[left[1:]]
        for output in right.split(', '):
            if output not in module_table:
                module_table[output] = Module(output, 'broadcaster')
            dot.edge(m.name, output)
            output_module = module_table[output]
            m.outputs.append(output_module)
            output_module.inputs.append(m)

# part 1
broadcaster = module_table['broadcaster']
pulses = [0,0]
nodes = {}
def press_button(count, part):
    global nodes
    global q
    q.put((broadcaster, False, None))

    if part == 1:
        while not q.empty():
            module, pulse_value, sender = q.get()
            pulses[pulse_value] += 1
            if module.name in ['qk', 'kf', 'kr', 'zs'] and not pulse_value:
                print(module.name, count, int(not module.flip_state))
            module.pulse(pulse_value, sender)
        return False
    else:
        while not q.empty():
            module, pulse_value, sender = q.get()
            if module.name in ['qk', 'kf', 'kr', 'zs'] and not pulse_value:
                if module.name not in nodes.keys():
                    nodes[module.name] = count
            if len(nodes.keys()) == 4:
                return nodes
            module.pulse(pulse_value, sender)
        return False

# part 1
for i in range(1000):
    press_button(i, 1)

print("Solution to Day 20 - part 1:", pulses[0]*pulses[1])

# part 2
for node in module_table.values():
    node.reset()

for presses in count(1):
    ans = press_button(presses, 2)
    if type(ans) == dict:
        break

print("Solution to Day 20 - part 2:", lcm(*list(ans.values())))