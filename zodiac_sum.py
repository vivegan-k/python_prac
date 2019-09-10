def zodiac_sum(n):
    if n == 0:
        return 0
    else:
        return (n %10) + zodiac_sum(n /10)

print zodiac_sum(4321)
    
        
