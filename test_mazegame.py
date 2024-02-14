import random

class Player:
    def __init__(self, name):
        self.name = name
        self.position = (0, 0)

class MazeGame:
    def __init__(self):
        self.player = None
        self.maze = [
            [0, 0, 1, 0],
            [0, 1, 0, 1, 0],
            [0, 1, 0, 1, 0],
            [0, 0, 0, 0, 0],
            [1, 1, 1, 1, 0]
        ]
        self.goal = (3, 3)  # Change the goal position to an unreachable location

    def set_player(self, player):
        self.player = player

    def move_player(self, direction):
        x, y = self.player.position
        if direction == "up":
            x -= 1
        elif direction == "down":
            x += 1
        elif direction == "left":
            y -= 1
        elif direction == "right":
            y += 1
        else:
            print("Invalid direction. Please enter up, down, left, or right.")
            return

        if 0 <= x < len(self.maze) and 0 <= y < len(self.maze[0]) and self.maze[x][y] != 1:
            # Introduce randomness for wall appearance
            if random.random() < 0.2:  # 20% chance for a wall to appear
                print("Oops! A wall appeared out of nowhere!")
                self.maze[x][y] = 1
            else:
                self.player.position = (x, y)
                print("Player moved to:", self.player.position)
                if self.player.position == self.goal:
                    print("Congratulations! You reached the goal!")
        else:
            print("Invalid move. You cannot go there.")

# Main program
def main():
    player_name = input("Enter your name: ")
    player = Player(player_name)
    game = MazeGame()
    game.set_player(player)

    while True:
        direction = input("Enter your move (up, down, left, right): ")
        game.move_player(direction)

if __name__ == "__main__":
    main()
