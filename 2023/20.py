from input_utils import *
from utils import lcm

from collections import defaultdict, deque
from copy import deepcopy


class Module:
    def __init__(self, name, outs):
        self.name = name
        self.outs = outs

    def receive_pulse(self, pulse, received_from, q):
        pass


class FlipFlopModule(Module):
    def __init__(self, name, outs):
        super().__init__(name, outs)
        self.state = False  # off

    def receive_pulse(self, pulse, received_from, q):
        if not pulse:
            self.state = not self.state
            for out in self.outs:
                q.append((self.state, self.name, out))


class ConjunctionModule(Module):
    def __init__(self, name, outs):
        super().__init__(name, outs)
        self.memory = defaultdict(lambda: False)

    def receive_pulse(self, pulse, received_from, q):
        self.memory[received_from] = pulse
        generated_pulse = not all(self.memory.values())
        for out in self.outs:
            q.append((generated_pulse, self.name, out))


class BroadcasterModule(Module):
    def receive_pulse(self, pulse, received_from, q):
        for out in self.outs:
            q.append((pulse, self.name, out))


def solve(modules, task):
    low_pulses = 0
    high_pulses = 0
    i = 0
    cycles = {}
    while task == 2 or i != 1000:
        i += 1
        q = deque([(False, "button", modules["broadcaster"])])
        while q:
            pulse, received_from, module = q.popleft()
            if task == 2:
                # solved kinda by hand, by observing the graph, making assumptions, and calculating LCM
                # assumptions:
                # - there are 4 disjoint components leading to module "dt"
                # - all 4 cycles start with the first press of the button
                if module.name == "dt" and pulse:
                    # print(f"{received_from} ==high==> dt (step {i})")
                    cycles[received_from] = i
                if len(cycles) == 4:
                    return lcm(list(cycles.values()))
            if not pulse:
                low_pulses += 1
            else:
                high_pulses += 1
            module.receive_pulse(pulse, received_from, q)
    return low_pulses * high_pulses


def run():
    lines = read_n_lines_one_string()
    modules = {}
    for line in lines:
        name, outs = line.split(' -> ')
        outs = outs.split(', ')
        if name == "broadcaster":
            modules[name] = BroadcasterModule(name, outs)
        elif name[0] == "%":
            modules[name[1:]] = FlipFlopModule(name[1:], outs)
        elif name[0] == "&":
            modules[name[1:]] = ConjunctionModule(name[1:], outs)
    end_module = Module("", [])
    for module in modules.values():
        outs = []
        for out in module.outs:
            if out not in modules:
                end_module.name = out
                outs.append(end_module)
            else:
                outs.append(modules[out])
                if isinstance(modules[out], ConjunctionModule):
                    modules[out].memory[module.name] = False
        module.outs = outs

    print(solve(deepcopy(modules), task=1))
    print(solve(deepcopy(modules), task=2))


if __name__ == "__main__":
    run()
