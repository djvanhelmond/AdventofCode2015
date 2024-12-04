from itertools import permutations, product
import math

ingredientsList = list()
class ingredient:
    def __init__(self, ingredientLine):
        self.name = ingredientLine.split(': ')[0]
        self.ingredients = dict()
        for prop in ingredientLine.split(': ')[1].strip('\n').split(', '):
            self.ingredients[prop.split(" ")[0]] = int(prop.split(" ")[1])


with open('input.txt', 'r') as file:
    for line in file:
        ingredientsList.append(ingredient(line))
    file.close()

totalTeaspoons = 100
numList = [i for i in range(totalTeaspoons + 1)]
perms = [numList for _ in range(len(ingredientsList))]
receipts = [r for r in product(*perms) if sum(r) == totalTeaspoons]

def cookReceipt(rcpt):
    val = dict()
    for j in ingredientsList[0].ingredients.keys():
        val[j] = 0
        for i in range(len(rcpt)):
            val[j] = val[j] + (int(rcpt[i]) * int(ingredientsList[i].ingredients[j]))
        val[j] = max(val[j], 0)
    return math.prod(list(val.values())[:-1]), math.prod(list(val.values())[-1:])


sum1 = 0
sum2 = 0
for receipt in receipts:
    totalScore, calorieCount = cookReceipt(receipt)
    if totalScore > sum1:
        sum1 = totalScore
    if calorieCount == 500:
        if totalScore > sum2:
            sum2 = totalScore

print("star 1: " + str(sum1))
print("star 2: " + str(sum2))
