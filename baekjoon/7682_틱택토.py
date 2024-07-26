class TicTacTo:
    status: str

    vertical_check = [[0,1,2], [3,4,5], [6,7,8]]
    horizontal_check = [[0,3,6], [1,4,7], [2,5,8]]
    diagonal_check = [[0,4,8], [2,4,6]]

    def check_winner(self, check_values):
        result = True
        for i, j, k in check_values:
            if self.status[i] == self.status[j] == self.status[k]:
                result = False
        return result

    def check_duce(self):
        if "." not in self.status:
            return False
        return True


    def check_game_continue(self):
        print(self.check_winner(self.vertical_check) , self.check_winner(self.horizontal_check) , self.check_winner(self.diagonal_check) , self.check_duce())
        return self.check_winner(self.vertical_check) and self.check_winner(self.horizontal_check) and self.check_winner(self.diagonal_check) and self.check_duce()

    def start(self):
        while True:
            self.status = input()

            if self.status == "end":
                break

            if not self.check_game_continue():
                print("invalid")
            else:
                print("valid")

game = TicTacTo()
game.start()

