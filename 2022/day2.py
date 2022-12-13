import lib

player = {
    # rock
    'X': 1,
    # paper
    'Y': 2,
    # scissors
    'Z': 3
}
# win,tie,loss
opponent = {
    # rock
    'A': [2, 1, 3],
    # paper
    'B': [3, 2, 1],
    # scissors
    'C': [1, 3, 2]
}


def pi2outcome(puzzle_input):
    total_score = 0
    for game in puzzle_input:
        opponent_move = game[0]
        outcome = game[-1]

        match outcome:
            case 'X':
                total_score += opponent[opponent_move][2]
            case 'Y':
                total_score += 3 + opponent[opponent_move][1]
            case 'Z':
                total_score += 6 + opponent[opponent_move][0]

    return total_score



def pi2game(puzzle_input):
    games = []
    total_score = 0
    for game in puzzle_input:
        score = 0
        opponent_move = game[0]
        player_move = game[-1]

        score += player[player_move]
        # player throws rock
        if player_move == 'X':
            # opponent throws rock
            if opponent_move == 'A':
                score += 3
            # opponent throws paper
            elif opponent_move == 'B':
                pass
            # opponent throws scissors
            elif opponent_move == 'C':
                score += 6
        # player throws paper
        elif player_move == 'Y':
            if opponent_move == 'A':
                score += 6
            elif opponent_move == 'B':
                score += 3
            elif opponent_move == 'C':
                pass
        # player throws scissors
        elif player_move == 'Z':
            if opponent_move == 'A':
                pass
            elif opponent_move == 'B':
                score += 6
            elif opponent_move == 'C':
                score += 3
        games.append([opponent_move, player_move, score])
    return games

if __name__ == '__main__':
    pi = lib.read_input('./day2_input.txt')
    games = pi2game(pi)
    total_score = 0

    for game in games:
        total_score += game[2]
    print(total_score)

    print(pi2outcome(pi))