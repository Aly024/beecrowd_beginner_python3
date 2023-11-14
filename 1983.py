N = int(input())
id_list = []
score_list = []

for i in range(N):

    id, score = map(float, input().split())
    id_list.append(id)
    score_list.append(score)

max_score = max(score_list)
if max_score >= 8:
    max_score_index = score_list.index(max_score) 
    print(int(id_list[max_score_index]))
else:
    print("Minimum note not reached")