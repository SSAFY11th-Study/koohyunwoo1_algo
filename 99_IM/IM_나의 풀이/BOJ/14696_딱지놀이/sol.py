import sys
sys.stdin = open('input.txt')
'''
별의 개수가 다르다면 별이 많은 쪽의 딱지가 이긴다.
별의 개수가 같고 동그라미의 개수가 다르다면, 동그라미가 많은 쪽의 딱지가이김
네모가 많은쪽
세모가 많은 쪽
모두 같으면 무승부임
별 4 동그라미 3 네모 2 세모 1
'''
N = int(input())
for i in range(N) :
    A = list(map(int,input().split()))[1:]
    B = list(map(int,input().split()))[1:]

    lstA = [A.count(4),A.count(3),A.count(2),A.count(1)]
    lstB = [B.count(4),B.count(3),B.count(2),B.count(1)]

    if lstA[0] > lstB[0] :
        print('A')
    elif lstA[0] <lstB[0] :
        print('B')
    elif lstA[1] > lstB[1] :
        print('A')
    elif lstB[1] > lstA[1] :
        print('B')
    elif lstA[2] > lstB[2] :
        print('A')
    elif lstB[2] > lstA[2] :
        print('B')
    elif lstA[3] > lstB[3] :
        print('A')
    elif lstB[3] > lstA[3] :
        print('B')
    else :
        print('D')
