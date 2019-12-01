#samogłoski

text="Nam strzelać nie kazano. Wstąpiłem na działo. I spojrzałem na pole, dwieście armat grzmiało. Artyleryji ruskiej ciągną się szeregi, Prosto, długo, daleko, jako morza brzegi."
n="AaEeIiOoUuYyóÓąĄęĘ"
def count(text,n): 
    result = [each for each in text if each in n] 
    print(len(result)) 
    print(result)    

count(text,n)