N, S, P = map(int, input().split())
type_S = list(map(int, input().split()))
#print(type_S)
P_list = list(map(int, input().split()))
#print(P_list)

album = list(range(1, N+1))
#print(album)

excluded = set(album) - set(P_list)
#print(excluded)

remaining = set(excluded) - set(type_S)
#print(remaining)

answer = len(excluded) - len(remaining)
print(answer)
