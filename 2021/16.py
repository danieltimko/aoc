from numpy import prod


def gt(arr):
    return arr[0] > arr[1]


def lt(arr):
    return arr[0] < arr[1]


def eq(arr):
    return arr[0] == arr[1]


def hex_to_bin(hex_s):
    bin_s = ""
    for c in hex_s:
        bin_s += bin(int(c, 16))[2:].zfill(4)
    return bin_s


def eval_literals(id, arr):
    assert id != 4
    return [sum, prod, min, max, None, gt, lt, eq][id](arr)


def decode_packet(packet, task):
    version = int(packet[:3], 2)
    id = int(packet[3:6], 2)
    if id == 4:
        i = 0
        s = ""
        while True:
            group = packet[6+i*5:11+i*5]
            s += group[1:]
            if group[0] == '0':
                literal = int(s, 2)
                return packet[11+i*5:], version if task == 1 else literal
            i += 1
    else:
        literals = []
        if packet[6] == '1':
            count = int(packet[7:18], 2)
            rest = packet[18:]
            while count:
                rest, x = decode_packet(rest, task)
                literals.append(x)
                count -= 1
        else:
            length = int(packet[7:22], 2)
            subpackets = packet[22:22+length]
            while subpackets:
                subpackets, x = decode_packet(subpackets, task)
                literals.append(x)
            rest = packet[22+length:]
        return rest, version+sum(literals) if task == 1 else eval_literals(id, literals)


def run():
    with open('input') as file:
        hex_s = file.readline()
        packet = hex_to_bin(hex_s)

        print(decode_packet(packet, 1)[1])
        print(decode_packet(packet, 2)[1])


run()
