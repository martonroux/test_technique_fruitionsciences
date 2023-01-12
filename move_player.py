import re


class MovePlayer:
    def __init__(self, file):
        self.file = self.generate_file(file)

    def generate_file(self, file):
        file_content = open(file).read()
        file_content = file_content.split("\n")

        grid_size_nums = re.findall(r'\d+', file_content[0])
        init_pos_data = file_content[1].split(" ")
        sequence = file_content[2]

        result = {'grid size': [int(grid_size_nums[0]), int(grid_size_nums[1])],
                  'pos': [int(init_pos_data[0]), int(init_pos_data[1])],
                  'direction': [init_pos_data[2]],
                  'sequence': [sequence]}
        return result

    def pilot(self):
        for i in self.file['sequence'][0]:
            if i == 'D' or i == 'G':
                self.rotate_player(i)

            if i == 'A':
                self.move_player()
        print("final position: x={} y={}, direction: {}".format(self.file['pos'][0],
                                                            self.file['pos'][1],
                                                            self.file['direction'][0]))

    def rotate_player(self, rotation):
        act_rotation = self.file['direction'][0]

        if rotation == 'G':
            if act_rotation == 'N':
                self.file['direction'][0] = 'W'
            if act_rotation == 'W':
                self.file['direction'][0] = 'S'
            if act_rotation == 'S':
                self.file['direction'][0] = 'E'
            if act_rotation == 'E':
                self.file['direction'][0] = 'N'
            return

        if rotation == 'D':
            if act_rotation == 'N':
                self.file['direction'][0] = 'E'
            if act_rotation == 'E':
                self.file['direction'][0] = 'S'
            if act_rotation == 'S':
                self.file['direction'][0] = 'W'
            if act_rotation == 'W':
                self.file['direction'][0] = 'N'

    def move_player(self):
        if self.test_out_bounds() == 1:
            return

        rotation = self.file['direction'][0]

        if rotation == 'N':
            self.file['pos'][1] += 1
        if rotation == 'E':
            self.file['pos'][0] -= 1
        if rotation == 'S':
            self.file['pos'][1] -= 1
        if rotation == 'W':
            self.file['pos'][0] += 1

    def test_out_bounds(self):
        rotation = self.file['direction'][0]
        x, y = self.file['pos']
        x_max, y_max = self.file['grid size']

        if rotation == 'N' and y + 1 > y_max:
            return 1
        if rotation == 'E' and x - 1 < 0:
            return 1
        if rotation == 'S' and y - 1 < 0:
            return 1
        if rotation == 'W' and x + 1 > x_max:
            return 1
        return 0
