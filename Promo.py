def main():
    prezzi = []
    animale = []
    InputUtente = ''
    while InputUtente != '-1':
        InputUtente = input('Digitare il prezzo dell''articolo e l''indicazione se si tratta di un animale (Y/N): ')
        Valore = InputUtente.split(' ' )
        if len(Valore) > 1:
            prezzi.append(float(Valore[0]))
            animale.append(Valore[1] == 'Y')
            ##animale.append(Valore[1].upper == 'Y')
    print(prezzi)
    print(animale)
    sconto = discount(prezzi, animale, len(prezzi))
    print(sconto)
    
def discount(prices, isPet, nItems):
    if (len(prices) < 6): 
        return {0, 'Il n° di articoli acquistati è inferiore al minimo previsto'}
    if (True not in isPet):
        return {0, 'Non sono stati acquistati animali'}
    if (isPet.count(False) < 5):                 
        return {0, 'Il n° di articoli non animali è inferiore a 5'} 
    for indice in range(len(isPet)):
        if isPet[indice]:
            prices.pop(indice)
    
    if len(prices) <= 5:
        divisore = 10
    else:    
        if len(prices) <= 10:
            divisore = 5    
        else:
            divisore = 3
    return {sum(prices)/divisore, 'Sconto calcolato'}   
        
## prezzi  = [2.79, 2.79, 2.79, 2.79, 70]
## animale = [False, False, False, False, True]
## discount(prezzi, animale, 5) ## Restituisce 0.00

## prezzi  = [2.79, 2.79, 2.79, 2.79, 2.79, 70]
## animale = [False, False, False, False, False, True]
## discount(prezzi, animale, 6) ## Restituisce 2.79

main()