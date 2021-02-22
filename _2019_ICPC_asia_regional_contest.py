class Q1:
    def problem():
        print("--The government of Neverland has recently announced a new petrol rationing plan with an unexpected pricehike. According to the new plan, each person receives a quota of 60 liters per month in a fuel card. Each literof petrol costs 1500 Oshloobs if it is within quota. Any extra fueling costs 3000 Oshloobs per liter.After recovering from the shock, Mahya is trying to figure out how dark is the future. The current month iscoming to an end, and Mahya has some quota left in her fuel card, remaining available for the next month. Aquota of 60 liters will also be added to her fuel card just at the beginning of the next month. She also has aprediction of the amount of petrol that will be used in the next month. She now wants to know how much sheshould pay for petrol in the next month. However, she is too lazy to do that on her own. So, she needs yourhelp to calculate the cost for her.InputThe input consists of two lines. The first line contains an integer n (0 ⩽ n ⩽ 200), specifying the amount ofpetrol that will be used in the next month. The second line contains an integer k (0 ⩽ k ⩽ 360), showing thequota left in Mahya’s fuel card at the end of current month.OutputPrint the amount of money (in Oshloobs) that Mahya will pay for petrol in the next month.")
        return "--Standard Input Standard Output 41 0 61500 Standard Input Standard Output 125 40 225000"

    def solution():
        standardAmountWeWillTake = 60
        standardPrice = 1500
        needMoreOilPrice = 3000
        output = 0

        howMuchWeNeedForNextMonth = int(input('how Much We Need For Next Month? '))
        howMuchWeHaveInCurrentMonth = int(input('how Much We Have In Current Month? '))
        
        if howMuchWeHaveInCurrentMonth == None or howMuchWeNeedForNextMonth == None: return 'The input is None'
        if howMuchWeNeedForNextMonth > standardAmountWeWillTake:
            allStandardOilYouWillHave = standardAmountWeWillTake + howMuchWeHaveInCurrentMonth
            output = (howMuchWeNeedForNextMonth - (allStandardOilYouWillHave)) * needMoreOilPrice + allStandardOilYouWillHave * standardPrice
            return f'You should pay: {output}'
        else:
            output = howMuchWeHaveInCurrentMonth * standardPrice
            return f'You need to pay: {output}'

class Q2:
    def problem():
        return
        
    def solution():
        return






print('Write The question number with option: problem solution. \n Ex: Q2.problem')

while True:
    try: 
        userInput = input()
        x = (exec(f'print ( {userInput} () )'))
        
    except TypeError:
        print('question or option not available!')
        
    except:
        print('Undefined!')