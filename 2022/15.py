from input_utils import *


def find_beacon(ranges):
    ranges = sorted(ranges, key=lambda r: r[0])
    end = 0
    for i in range(len(ranges)-1):
        if end == 0 and 0 in ranges[i]:
            end = ranges[i][-1]
        if end == 0:
            continue
        if ranges[i+1][-1] <= end:
            continue
        if ranges[i+1][0] > end+1:
            return ranges[i][-1]+1
        end = ranges[i+1][-1]
    return -1


def task1(sensors, target_row=10):
    vision = set()
    i = 0
    for sensor, beacon in sensors:
        maxdiff = abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])
        print(i)
        i += 1
        for y in range(sensor[1]-maxdiff, sensor[1]+maxdiff+1):
            x_reach = maxdiff - abs(sensor[1]-y)
            x_range = range(sensor[0]-x_reach, sensor[0]+x_reach+1)
            vision.add((x_range, y))
    ranges = [r[0] for r in vision if r[1] == target_row]
    min_x = ranges[0][0]
    max_x = ranges[0][1]
    for r in ranges:
        if min(r) < min_x:
            min_x = min(r)
        if max(r) > max_x:
            max_x = max(r)
    count = 0
    for x in range(min_x, max_x+1):
        for r in ranges:
            if x in r:
                count += 1
                break
    return count-1, vision  # TODO why is it off-by-one ???


def task2(sensors, reach=4000000):
    vision = task1(sensors)[1]
    vision_by_row = dict()
    i = 0
    for r in vision:
        if i % 1000000 == 0:
            print(f"{i}/{len(vision)}")
        i += 1
        if r[1] not in vision_by_row:
            vision_by_row[r[1]] = []
        vision_by_row[r[1]].append(r[0])
    for y in range(reach+1):
        ranges = vision_by_row[y]
        if y % 100000 == 0:
            print(y)
        if (x := find_beacon(ranges)) != -1:
            return x*4000000 + y


def run():
    with open(INPUT_FILE_PATH) as f:
        sensors = []
        for line in f.readlines():
            splitted = line.strip().split('=')
            sensorx = int(splitted[1].split(',')[0])
            sensory = int(splitted[2].split(':')[0])
            beaconx = int(splitted[3].split(',')[0])
            beacony = int(splitted[4])
            sensors.append(((sensorx, sensory), (beaconx, beacony)))

    print(task1(sensors)[0])
    print(task2(sensors))


if __name__ == "__main__":
    run()
