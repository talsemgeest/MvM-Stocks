import itertools
import operator

data = list(open('mvm_stocks.txt', 'r'))

stocks = data[1].strip().split(',')
stocks = map(int, stocks)
stocks_titles = ["Money Furnace", "KB-808", "Taunt Processor", "Emotion Detector",
                 "Bomb Stabilizer", "Humor Supression Pump", "Currency Digester",
                 "Brainstorm Bulb"]
kits = []
combos = []
#i is the start line of kits
i = 4

while i < len(data):
    kits.append(data[i].strip().split(','))
    i += 1

def intify_kit(kit):
    for j in range(0, 8):
        kit[j] = int(kit[j])
    #Also numerify price
    kit[9] = float(kit[9])
    return kit
        

kits = map(intify_kit, kits)

for i in range(1, len(kits)+1):
    combolist = list(itertools.combinations(kits, i))
    for combo in combolist:
        #Get total count of ingredients in combo
        itemtotals = [0,0,0,0,0,0,0,0]

        value = 0
        for kit in combo:
            for j in range(0,8):
                itemtotals[j] += kit[j]
            value += kit[9]

        #Determine if there are enough parts to make combo
        validcombo = True
        for l in range(0,8):
            if stocks[l] < itemtotals[l]:
                validcombo = False

        #If so, add to list
        if validcombo:
            combos.append([value, combo])




combos.sort(key=lambda x: x[0])
combos.reverse()

bestcombo_value = combos[0][0]
bestcombo_items = combos[0][1]

print "Best combo is:"
result = bestcombo_items[0][8]
if len(bestcombo_items) > 1:
    for x in range(1, len(bestcombo_items)):
        result += (" + " + bestcombo_items[x][8])

print result
print "\nDetails:\n"

for item in bestcombo_items:
    print "---" + item[8] + "---"
    for x in range(0, 8):
        print str(item[x]).zfill(2) + " " + stocks_titles[x]

    print "\n"
                   




