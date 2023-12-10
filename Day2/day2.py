import re

def p1(lines):
    games = []
    for line in lines:
        id, cubes = line.rstrip().split(':')
        game_id = int(id.split()[-1])
        
        plays = cubes.split(';')
        flag = True
        
        for play in plays:
            play_counts = [x.lstrip() for x in play.split(',')]
            for pc in play_counts:
                cnt, color = pc.split(' ')
                match(color):
                    case 'red':
                        if int(cnt) > 12:
                            flag = False
                            break
                    case 'green':
                        if int(cnt) > 13:
                            flag = False
                            break
                    case 'blue':
                        if int(cnt) > 14:
                            flag = False
                            break
        if flag:
            games.append(game_id)
    print(sum(games))

def p2(lines):
    game_power = []
    for line in lines:
        id, cubes = line.rstrip().split(':')
        game_id = int(id.split()[-1])
        
        plays = cubes.split(';')
        red = 0
        green = 0
        blue = 0
        
        for play in plays:
            play_counts = [x.lstrip() for x in play.split(',')]
            for pc in play_counts:
                cnt, color = pc.split(' ')
                cnt = int(cnt)
                match(color):
                    case 'red':
                        if cnt > red:
                            red = cnt
                    case 'green':
                        if cnt > green:
                            green = cnt
                    case 'blue':
                        if cnt > blue:
                            blue = cnt
        game_power.append(red*green*blue)
    print(sum(game_power))

if __name__ == "__main__":
    with open("Day2/input.txt") as file:
        lines = file.readlines()
        p1(lines)
        p2(lines)