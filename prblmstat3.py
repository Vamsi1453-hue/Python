class Player:
    def __init__(self, player_name):
        self.player_name = player_name

class Tournament:
    def __init__(self):
        self.runs = []

    def add_runs(self, score):
        self.runs.append(score)

    def total_runs(self):
        return sum(self.runs)

    def average_runs(self):
        return self.total_runs() / len(self.runs) if self.runs else 0

    def generate_report(self, player):
        print("=" * 50)
        print("         PLAYER PERFORMANCE REPORT")
        print("=" * 50)
        print(f"\nPlayer Name    : {player.player_name}")
        print(f"\nTotal Runs     : {self.total_runs()}")
        print(f"Matches Played : {len(self.runs)}")
        print(f"Average Runs   : {self.average_runs()}")
        print("\n" + "=" * 50)

player = Player("Arjun")
tournament = Tournament()

tournament.add_runs(50)
tournament.add_runs(75)
tournament.add_runs(100)

tournament.generate_report(player)