songs = [ "PROXYCITY", "P.Y.N.G.", "DNSUEY!", "SERVERS", "HOST!", 
         "CRIPTONIZE", "OFFLINE DAY", "SALT", "ANSWER!", "RAR?", "WIFI ANTENNAS"]

N = int(input())

for i in range(N):

    X, Y = map(int, input().split())
    Z = X+Y
    print(songs[Z])