blank = ' '
board = [[blank] * 20 for i in range(20)]
def printboard(board):
    #Prints out board layout
    board2 = board
    string = ''
    [i.insert(0,'|') for i in board2]
    [i.append('|') for i in board2]
    [board[i].append(str(i)) for i in range(len(board2))]
    board2.insert(0,(['_'] * 20))
    board2[0].insert(0,' ')
    board2.append(['_'] * 20)
    board2[-1].insert(0, ' ')
    board2.insert(0,([i for i in range(10)]) * 2)
    board2.append(([i for i in range(10)]) * 2)
    board2[len(board2)-1].insert(0, ' ')
    board2[0].insert(0, ' ')

    for i in range(len(board2)):
        for j in range(len(board2[i])):
            string = string + str(board2[i][j])
        string = string + '\n'
    return string

def addFirstWord(board,word):
    #Adds first word to the middle of the board

    #Boundary check
    if len(word) == 0:
       return False
    elif len(word) > len(board):
        return False

    middleboardx = round(len(board)/2) - 1
    middleboardy = round(len(board)/2) - 1
    middleword = round(len(word)/2)-1
    x = 0

    for i in range((len(word)//2)+1):
        if middleword-x != -1:
            board[middleboardx][middleboardy - x] = word[middleword-x]
            x += 1
    x = 0

    for p in range((len(word)//2)+1):
        board[middleboardx][middleboardy + x] = word[middleword+x]
        x += 1
    return True

def checkvertical(board,word,row,col):
    #Boundary check
    if len(word) > len(board):
        return False

    #Vertical checking for invalid positioning
    else:
        for i in range(len(word)):
            if word[i] == str(board[row][col]):
                if row < len(board) - 1 and col < len(board) - 1:
                    if board[row+1][col] == ' ' and board[row-1][col] == ' ' and board[row+1][col+1] == ' ' and board[row+1][col-1] == ' ' and board[row-1][col+1] == ' ' and board[row-1][col-1] == ' ' :
                        return True
    return False

def checkverticalchar(board,char,row,col):
    #Rigorous vertical checking for invalid positioning
    if str(board[row][col]) == char:
        if board[row + 1][col + 1] == ' ' and board[row + 1][col - 1] == ' ' and board[row - 1][col + 1] == ' ' and board[row - 1][col - 1] == ' ':
            return True
    else:
        if board[row][col+1] == ' ' and board[row][col-1] == ' ' and (board[row-1][col] == ' ' or board[row+1][col] == ' '):
            return True

    return False

def addvertical(board,word):
    #Boundary checking
    if len(word) > len(board):
        return False

    for i in range(len(board)):
        for j in range(1,len(board[i])):
            for k in range(1,len(word)):
                if checkvertical(board,word[k],i,j) == True:
                    up,down = i,i
                    tracker = []
                    error = False

                    #Boundary checking once in position
                    if i - len(word[:k]) <0 or i + len(word[k:]) >= len(board):
                        return False

                    #Adding word letters to board (downwards)
                    for d in range(k+1,len(word)):
                        down += 1

                        #Rigourous check
                        if checkverticalchar(board, word[d], down, j) == True:
                            tracker.append(down)
                            board[down][j] = word[d]
                        else:
                            error = True

                    #Adding word letters to board (upwards)
                    for u in range(k-1,-1,-1):
                        up -= 1

                        #Rigourous check
                        if checkverticalchar(board,word[u],up,j) == True:
                            tracker.append(up)
                            board[up][j] = word[u]
                        else:
                            error = True

                    #Deleting letters from board if error detected
                    if error == True:
                        for t in tracker:
                            board[t][j] = ' '
                    else:
                        return True
    else:
        return False

def checkhorizontal(board,word,row,col):
    #Boundary check
    if len(word) > len(board):
        return False

    #Horizontal checking for invalid positioning
    else:
        for i in range(len(word)):
            if word[i] == str(board[row][col]):
                if row < len(board) - 1 and col < len(board) - 1:
                    if board[row][col+1] == ' ' and board[row][col-1] == ' ' and board[row+1][col+1] == ' ' and board[row+1][col-1] == ' 'and board[row-1][col+1] == ' ' and board[row-1][col-1] == ' ':
                        return True
    return False

def checkhorizontalchar(board,char,row,col):
    #Rigorous horizontal checking for invalid positioning
    if str(board[row][col]) == char:
        if board[row + 1][col + 1] == ' ' and board[row + 1][col - 1] == ' ' and board[row - 1][col + 1] == ' ' and board[row - 1][col - 1] == ' ':
            return True
    else:
        if board[row+1][col] == ' ' and board[row-1][col] == ' ' and (board[row][col+1] == ' ' or board[row][col-1] == ' '):
            return True

    return False

def addhorizontal(board,word):
    #Boundary checking
    if len(word) > len(board):
        return False

    for i in range(len(board)):
        for j in range(len(board[i])):
            for k in range(len(word)):
                if checkhorizontal(board, word[k], i,j) == True:
                    left, right = j, j
                    tracker = []
                    error = False

                    #Boundary checking once in position
                    if j - len(word[:k]) < 0 or j + len(word[k:]) >= len(board[i]):
                        return False

                    #Adding word letters to board (rightwards)
                    for r in range(k+1,len(word)):
                        right += 1

                        #Rigourous check
                        if checkhorizontalchar(board, word[r], i, right) == True:
                            tracker.append(right)
                            board[i][right] = word[r]
                        else:
                            error = True

                    #Adding word letters to board (leftwards)
                    for l in range(k-1,-1,-1):
                        left -= 1

                        #Rigourous check
                        if checkhorizontalchar(board, word[l], i, left) == True:
                            tracker.append(left)
                            board[i][left] = word[l]
                        else:
                            error = True

                    #Deleting letters from board if error detected
                    if error == True:
                        for t in tracker:
                            board[i][t] = ' '
                    else:
                        return True

    else:
        return False

def crossword(L):
    #Boundary check on first word
    if len(L[0]) > len(board):
        L.pop(0)

    #Adding word list to board
    for i in range(len(L)):
        if i == 0:
            addFirstWord(board,L[i])
        elif i%2 != 0:
            addvertical(board,L[i])

        else:
            addhorizontal(board,L[i])

    return printboard(board)

L = ['hippopotamus', 'horse', 'loon', 'snake', 'cat', 'rattlesnake','dinosaur','gorilla','mouse']

print(crossword(L))
print('\n')

