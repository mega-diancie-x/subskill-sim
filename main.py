import random

goldProb = 0.14
blueProb = 0.47
whiteProb = 1.00

friendLevel = 0

goldSub = [
    "Berry Finding S",
    "Helping Bonus",
    "Research EXP Bonus",
    "Sleep EXP Bonus",
    "Dream Shard Bonus",
    "Energy Recovery Bonus",
    "Skill Level Up M"
]

blueSub = [
    "Helping Speed M",
    "Ingredient Finder M",
    "Skill Trigger M",
    "Inventory Up L",
    "Inventory Up M",
    "Skill Level Up S"
]

whiteSub = [
    "Helping Speed S",
    "Ingredient Finder S",
    "Skill Trigger S",
    "Inventory Up S"
]

def chooseSubskill():
    global goldProb, blueProb, whiteProb, goldSub, blueSub, whiteSub
    n = random.random()
    if n < goldProb:
        return random.choice(goldSub)
    elif n < blueProb:
        return random.choice(blueSub)
    else:
        return random.choice(whiteSub)

def trial(friendLevel = 0):
    sub = []
    if friendLevel >= 10:
        sub.append(random.choice(goldSub))
    if friendLevel >= 40:
        sub.append(random.choice(goldSub))
    if friendLevel >= 100:
        sub.append(random.choice(goldSub))
        return sub
    for i in range(3 - len(sub)):
        sub.append(chooseSubskill())
    return sub

SAMPLE_SIZE = 5000000

results = []
for i in range(SAMPLE_SIZE):
    results.append(trial(friendLevel))

# print(results[0])

BFS = 0
BFS_HB = 0

for i in results:
    if "Berry Finding S" in i and "Helping Bonus" in i:
        BFS_HB += 1
    if "Berry Finding S" in i:
        BFS += 1

BFS_Prob = BFS/SAMPLE_SIZE
BFS_HB_Prob = BFS_HB/SAMPLE_SIZE
BFS_CONFIDENCE = (BFS_Prob*(1-BFS_Prob)/SAMPLE_SIZE)
BFS_HB_CONFIDENCE = (BFS_HB_Prob*(1-BFS_HB_Prob)/SAMPLE_SIZE)
print("Sample Size:", SAMPLE_SIZE)
print("Friendship Level", friendLevel)
print("Berry Finding S:", BFS)
print("BFS+HB:", BFS_HB)
print()
print("Est. BFS Probability:", BFS_Prob)
print("95% Confidence Level (Upper):", BFS_Prob + 1.96 * BFS_CONFIDENCE)
print("95% Confidence Level (Lower):", BFS_Prob - 1.96 * BFS_CONFIDENCE)
print("Est. BFS+HB Probability:", BFS_HB/SAMPLE_SIZE)
print("95% Confidence Level (Upper):", BFS_HB_Prob + 1.96 * BFS_HB_CONFIDENCE)
print("95% Confidence Level (Lower):", BFS_HB_Prob - 1.96 * BFS_HB_CONFIDENCE)
