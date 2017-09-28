def swapPlayer(iPlayer): #when input is 1 returns 2, when input is 2 returns 1
    return ((~(iPlayer-1))&0x01)+1