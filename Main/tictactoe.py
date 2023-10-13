class TicTacToe:
    
    def __init__(self):
        self.grid = [['1','2','3'],['4','5','6'],['7','8','9']]

    def display(self):
      display = '- - - - -\n'

      for i in self.grid:
        display+=' | '.join(i)+'\n- - - - -\n'
      
      print(display)
    
    def check_rows(self):
      for row in self.grid:
        if ''.join(row) == 'xxx' or ''.join(row) == 'ooo':
            return True
        
    def check_cols(self):
        for i in range(3):
            if (''.join([self.grid[0][i],self.grid[1][i],self.grid[2][i]]) == 'xxx' or ''.join([self.grid[0][i],self.grid[1][i],self.grid[2][i]]) == 'ooo'):
                return True

    def check_cross(self):
        return (''.join([self.grid[0][0],self.grid[1][1],self.grid[2][2]]) == 'xxx' or ''.join([self.grid[0][0],self.grid[1][1],self.grid[2][2]]) == 'ooo' or (''.join([self.grid[0][2],self.grid[1][1],self.grid[2][0]]) == 'xxx' or (''.join([self.grid[0][2],self.grid[1][1],self.grid[2][0]]) == 'ooo')))

    def check_grid(self):
        if self.check_rows():
            return True
        elif self.check_cols():
            return True
        elif self.check_cross():
            return True
        else:
            return False
    
    def input(self,option):
        self.display()
        pos = input(f'Enter position for {option}:\n')
        try:
            pos = int(pos)
            current_pos = 0
            if pos<1 or pos>9:
                print('\nthe position is invalid, try valid position')
                return 0

            for i in range(3):
                for j in range(3):
                    current_pos+=1
                    if current_pos == pos:
                        if self.grid[i][j] == 'x' or self.grid[i][j] == 'o':
                          print('\nthe position is already used, try another one')
                          return 0  
                        else:
                          self.grid[i][j] = option
                          return 1
        except:
            print('\nEnter valid position among the available positions, you entered',pos)
            return 0
    
    def start(self):
        count = 0
        while True:
            count+=1
            if count%2==1:
                option = 'x'
            else:
                option = 'o'
            
            flag = self.input(option)

            print()
            if flag != 1:
                count-=1
            elif self.check_grid():
                print('\ngame over! \n')
                self.display()
                print()
                if option == 'x':
                  print('Player 1[x] won :)')
                  break
                else:
                  print('Player 2[o] won :)')
                  break
            elif count>8:
                print("\nit's a DRAW!!! try again :)")
                break
