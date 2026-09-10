import random
def leibniz(n):
    sum_l = 0
    for i in range(1,n):
        sum_l += ((-1)**(i+1))/(2*i-1)
    
    pi_l = 4*sum_l
    
    return pi_l
    
def sharp(n):
    pi_s = 0
    for i in range(n):
        pi_s += (2*((-1)**i)*3**(1/2 - i))/(2*i + 1)
    return pi_s
def monte_carlo(n):
    inside = 0
    for i in range(n):
        x = random.random()
        y = random.random()
    
        if ((x**2 + y**2) <= 1):
            inside += 1
    
    pi_m = 4 * inside / n
        
    return pi_m
    
    
    # now to actually calculate
    
n = 200 # amount of steps to get close to pi
print("Hi")
print(leibniz(n), " Leibniz")
print(sharp(n), " Sharp")
print(monte_carlo(n), " Monte Carlo")
print("Done")