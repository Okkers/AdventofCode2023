class Solve_Day_5(object):
    def __init__(self, arg):
        self.arg = arg
        self.data = self._get_data()

    def _get_data(self):
        names =["seed-to-soil map", "soil-to-fertilizer map", "fertilizer-to-water map", 
                "water-to-light map", "light-to-temperature map", "temperature-to-humidity map", 
                "humidity-to-location map"]
        with open("input.txt") as f:
            data = f.read().split(":")

        seeds = [int(y) for y in [x for x in "".join(data[1].split("\n")[:-2]).split(" ") if len(x) != 0]]
        data = data[1:]

        maps = {}
        for ind,map in enumerate(names):
            if map in data[ind]:
                lst_maps = [x for x in data[ind+1].split("\n")[:-2] if len(x) != 0]
                lst_maps = [[int(y) for y in x.split(" ")] for x in lst_maps]
                maps[map] = lst_maps
        return seeds, maps

    def solve1(self):
        seeds, maps = self.data
        locations = []
        for seed in seeds:
            cur_seed = seed
            for map_name in maps.keys():
                mapping = maps[map_name]
                check = False
                for rang in mapping:
                    if not(check):
                        if cur_seed >= rang[1] and cur_seed <= rang[1]+rang[2]-1:
                            cur_seed = cur_seed - rang[1] + rang[0]
                            check = True
            locations.append(cur_seed)

        return min(locations)
    
    def solve2(self):
        seeds, maps = self.data
        locations = []
        for indx in range(0, len(seeds), 2):
            seed_range = [[seeds[indx], seeds[indx]+seeds[indx+1]]]
            conversion = []
            for key in maps.keys():
                queue = seed_range
                while len(queue) != 0:
                    seed_start, seed_end = queue.pop(0)
                    check = False
                    for rang in maps[key]:
                        if not(check):
                            if seed_start < rang[1] and seed_end >= rang[1] and seed_end <= rang[1]+rang[2]-1:
                                queue.append([seed_start, rang[1]-1])
                                conversion.append([rang[0], seed_end - rang[1] + rang[0]])
                                check = True
                            elif seed_start >= rang[1] and seed_start <= rang[1]+rang[2]-1 and seed_end > rang[1]+rang[2]-1:
                                queue.append([rang[1]+rang[2], seed_end])
                                conversion.append([seed_start - rang[1] + rang[0], rang[0]+rang[2]-1])
                                check = True
                            elif seed_start < rang[1] and seed_end > rang[1]+rang[2]-1:
                                queue.append([seed_start, rang[1]+1])
                                queue.append([rang[1]+rang[2]-2, seed_end])
                                conversion.append([rang[0], rang[0]+rang[2]-1])
                                check = True
                            elif seed_start >= rang[1] and seed_start <= rang[1]+rang[2]-1 and seed_end >= rang[1] and seed_end <= rang[1]+rang[2]-1:
                                conversion.append([seed_start - rang[1] + rang[0], seed_end - rang[1]+rang[0]])
                                check = True

                seed_range = conversion
                conversion = []
            locations.append(seed_range)

        unfold_locations = [y for sublist in [x for subsublist in locations for x in subsublist] for y in sublist]

        return min(unfold_locations)
        
solution = Solve_Day_5(1)
ans = solution.solve1()
print("Solution to Day 5 - part 1:", ans)

ans = solution.solve2()
print("Solution to Day 5 - part 2:", ans)