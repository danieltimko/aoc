
class Computer:
    def __init__(self):
        self.accumulator = 0
        self.pointer = 1
        self.visited_instructions = set()


def parse_instruction(instruction):
    splitted = instruction.split(" ")
    return splitted[0], splitted[1]


def execute_instruction(computer, instruction, arg):
    if computer.pointer in computer.visited_instructions:
        return False
    computer.visited_instructions.add(computer.pointer)
    if instruction == "acc":
        computer.accumulator += int(arg)
    if instruction == "jmp":
        computer.pointer += int(arg) - 1
    elif instruction == "nop":
        pass
    computer.pointer += 1
    return True


def start(computer, instructions):
    result = True
    while result and computer.pointer <= len(instructions):
        result = execute_instruction(computer, *parse_instruction(instructions[computer.pointer-1]))
    return result


def run():
    with open('input') as file:
        lines = list(map(lambda line: line.strip(), file.readlines()))

        computer = Computer()
        start(computer, lines)
        print(computer.accumulator)

        for i in range(len(lines)):
            instruction, arg = parse_instruction(lines[i])
            if instruction in ["nop", "jmp"]:
                lines[i] = f"{'jmp' if instruction == 'nop' else 'nop'} {arg}"
                computer = Computer()
                result = start(computer, lines)
                if result:
                    print(computer.accumulator)
                lines[i] = f"{instruction} {arg}"


run()
