N = int(input())

S_i_t = 0
B_i_t = 0
A_i_t = 0

S_s_t = 0
B_s_t = 0
A_s_t = 0

for i in range(N):

    name = input()
    S_i, B_i, A_i = map(int,input().split() ) #Service individual
    S_i_s, B_i_s, A_i_s = map(int, input().split() ) #Service individual successful
    
    S_i_t += S_i  #Service individual total
    S_s_t += S_i_s  #Service individual successful total
    B_i_t += B_i
    B_s_t += B_i_s
    A_i_t += A_i
    A_s_t += A_i_s


S_p = (S_s_t/S_i_t) * 100
B_p = (B_s_t/B_i_t) * 100
A_p = (A_s_t/A_i_t) * 100
print(f"Pontos de Saque: {S_p:.2f} %.")
print(f"Pontos de Bloqueio: {B_p:.2f} %.")
print(f"Pontos de Ataque: {A_p:.2f} %.")

