gridSize = 50
gridNumSize = 100
selectRow = -1
selectCol = -1
selectNum = 0
grid = [[0 for _ in range(9)] for _ in range(9)]
locked = [[False for _ in range(9)] for _ in range(9)]


def setup():
    size(1000,500)
    newGame()


def draw():
    background(255)
    drawGameUI()
    drawGrid()
    drawNumpadGrid()
    drawNum()
    drawNumpadNum()


def drawGrid():
    stroke(0)
    i=0
    while i<=9:
        if i%3==0:
            strokeWeight(3)
        else:
            strokeWeight(1)
        line(i*gridSize, 0, i*gridSize, 9*gridSize)
        line(0, i*gridSize, 9*gridSize, i*gridSize)
        i+=1
        

def drawNum():
    textAlign(CENTER,CENTER)
    textSize(24)
    fill(0)
    row=0
    while row<9:
        col=0
        while col<9:
            if grid[row][col] != 0:
                text(grid[row][col], col*gridSize + gridSize/2, row*gridSize + gridSize/2)
            col+=1
        row+=1
            

def drawNumpadGrid():
    stroke(0)
    strokeWeight(3)
    i=0
    while i<4:
        line(i*gridNumSize+600,0,i*gridNumSize+600,4*gridNumSize)
        i+=1
    i=0
    while i<5:
        line(600,i*gridNumSize,3*gridNumSize+600,i*gridNumSize)
        i+=1
    
    
def drawNumpadNum():
    textAlign(CENTER,CENTER)
    textSize(30)
    fill(0)
    numpadNum = 1
    i=0
    while i<3:
        j=0
        while j<3:
            text(numpadNum, (j*gridNumSize)+600+(gridNumSize/2), (i*gridNumSize)+(gridNumSize/2))
            numpadNum+=1
            j+=1
        i+=1
    text("-",600+gridNumSize+gridNumSize/2,3*gridNumSize+gridNumSize/2)
                         
                                                   
def checkValid(arr, num, row, col):
    i=floor(row/3)*3
    while i<floor(row/3)*3+3:
        j=floor(col/3)*3
        while j<floor(col/3)*3+3:
            if not (j == col and i == row) and arr[i][j] == num:
                return False
            j+=1
        i+=1
    i=0
    while i<9:
        if(i != col and arr[row][i] == num):
            return False
        i+=1
    i=0
    while i<9:
        if i != row and arr[i][col] == num:
            return False
        i+=1
    return True


def mousePressed():
    global selectRow, selectCol, selectNum
    if mouseY < 9*gridSize and mouseX < 9*gridSize:
        if not locked[floor(mouseY/gridSize)][floor(mouseX/gridSize)]:
            selectCol = floor(mouseX/gridSize)
            selectRow = floor(mouseY/gridSize)
        else:
            print("Can't change this number")
            
    if mouseY < 400 and mouseX > 600 and mouseX < 900:
        if mouseY < 100:
            if mouseX < 700:
                selectNum = 1
            elif mouseX < 800:
                selectNum = 2
            else:
                selectNum = 3
        elif mouseY < 200:
            if mouseX < 700:
                selectNum = 4
            elif mouseX < 800:
                selectNum = 5
            else:
                selectNum = 6
        elif mouseY < 300:
            if mouseX < 700:
                selectNum = 7
            elif mouseX < 800:
                selectNum = 8
            else:
                selectNum = 9
        else:
            if mouseX > 700 and mouseX < 800:
                selectNum = 0
                
    if selectRow != -1 and selectCol != -1:
        if selectNum == 0 or checkValid(grid, selectNum, selectRow, selectCol):
            grid[selectRow][selectCol] = selectNum
            selectNum = 0
        else:
            if selectRow != -1 and selectCol != -1:
                print("Invalid number")
                
                
def drawGameUI():
    if selectRow != -1 and selectCol != -1:
        fill(200, 200, 255, 100)
        noStroke()
        rect(selectCol*gridSize, selectRow*gridSize, gridSize, gridSize)
    row=0
    while row<9:
        col=0
        while col<9:
            if locked[row][col]:
                fill(225)
                noStroke()
                rect(col*gridSize, row*gridSize, gridSize, gridSize)
            col+=1
        row+=1
        
                
def shuffleArray(arr):
    i=1
    while i<len(arr) -2:
        j = int(random(i+1))
        tmp = arr[i]
        arr[i] = arr[j]
        arr[j] = tmp
        i+=1
        
    
def generateFullBoard(board):
    row=0
    while row<9:
        col=0
        while col<9:
            if board[row][col] == 0:
                numbers = [1,2,3,4,5,6,7,8,9]
                shuffleArray(numbers)
                
                n=1
                while n<10:
                    if checkValid(board, n, row, col):
                        board[row][col] = n
                        if generateFullBoard(board):
                            return True
                        board[row][col] = 0
                    n+=1
                return False
            col+=1
        row+=1
    return True


    
def newGame():
    full = [[0 for _ in range(9)] for _ in range(9)]
    generateFullBoard(full)
    
    r=0
    while r<9:
        c=0
        while c<9:
            grid[r][c] = full[r][c]
            locked[r][c] = True
            c+=1
        r+=1
    holes = 50
    k=0
    while k<holes:
        r = int(random(9))
        c = int(random(9))
        grid[r][c] = 0
        locked[r][c] = False
        k+=1
