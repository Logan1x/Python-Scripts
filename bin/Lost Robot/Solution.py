# According to question we can only instruct robot up or down or left or right.
# So in his current coordiantes and home coordinates one of the/
# coordinate either X or Y must be same.


for _ in range(int(input())):
    x1, y1, x2, y2 = map(int, input().split())  # This will parse input to x1,y1,x2 and y2
    if x1 != x2 and y1 != y2:
        print('sad')
    elif x1 == x2 and y1 < y2:
        print('up')
    elif x1 == x2 and y1 > y2:
        print('down')
    elif y1 == y2 and x1 < x2:
        print('right')
    elif y1 == y2 and x1 > x2:
        print('left')
