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
    for i in range(5 - len(sub)):
        skill = chooseSubskill()
        while skill in sub:
            skill = chooseSubskill()
        sub.append(skill)
    ing = "A"
    ing += random.choice("ABB")
    ing += random.choice("ABC")
    return [sub[:3], sub[3:], sub, ing]

SAMPLE_SIZE = (10**7)
INTERVAL = 5*(10**5)

print("Sleep Subskill Simulator")
print("Mode 1: Simulator, Mode 2: Probability Calculator")
mode = int(input("Mode: "))

if mode == 1:
    friendLevel = int(input("Friendship Level: "))
    times = int(input("Number of Trials: "))
    for i in range(times):
        print(trial(friendLevel)[2:])
    exit()

results = []
for i in range(SAMPLE_SIZE):
    results.append(trial(friendLevel))
    if i % INTERVAL == 0:
        print("Progress:", i/SAMPLE_SIZE)

# print(results[0])

BFS = 0
BFS_HB = 0
BFS_HS = 0
BFS_HS_Seed = 0
Mono_HSM_IFM = 0
Mono_HS_IF_Seed = 0
RSB_SEB_DSB = 0
Mono = 0

for i in results:
    j = i[0]
    k = i[1]
    ing = i[3]
    if "Berry Finding S" in j and "Helping Bonus" in j:
        BFS_HB += 1
    if "Berry Finding S" in j:
        BFS += 1
    if "Berry Finding S" in j and ("Helping Speed M" in j or "Helping Speed S" in j):
        BFS_HS += 1
    if "Berry Finding S" in j and ("Helping Speed M" in j or "Helping Speed S" in j) and not ("Helping Speed M" in k):
        BFS_HS_Seed += 1
    if "Helping Speed M" in j and "Ingredient Finder M" in j and ing == "AAA":
        Mono_HSM_IFM += 1
    if ("Helping Speed S" in j or "Helping Speed M" in j) and ("Ingredient Finder S" in j or "Ingredient Finder M" in j) and not (("Helping Speed M" in k) or ("Ingredient Finder M" in k)) and ing == "AAA":
        Mono_HS_IF_Seed += 1
    if "Research EXP Bonus" in j and "Sleep EXP Bonus" in j and "Dream Shard Bonus" in j:
        RSB_SEB_DSB += 1
    if ing == "AAA":
        Mono += 1

BFS_Prob = BFS/SAMPLE_SIZE
BFS_HB_Prob = BFS_HB/SAMPLE_SIZE
BFS_HS_Prob = BFS_HS/SAMPLE_SIZE
BFS_HS_Seed_Prob = BFS_HS_Seed/SAMPLE_SIZE
Mono_HSM_IFM_Prob = Mono_HSM_IFM/SAMPLE_SIZE
Mono_HS_IF_Seed_Prob = Mono_HS_IF_Seed/SAMPLE_SIZE
RSB_SEB_DSB_Prob = RSB_SEB_DSB/SAMPLE_SIZE
Mono_Prob = Mono/SAMPLE_SIZE
BFS_CONFIDENCE = (BFS_Prob*(1-BFS_Prob)/SAMPLE_SIZE)
BFS_HB_CONFIDENCE = (BFS_HB_Prob*(1-BFS_HB_Prob)/SAMPLE_SIZE)
BFS_HS_CONFIDENCE = (BFS_HS_Prob*(1-BFS_HS_Prob)/SAMPLE_SIZE)
BFS_HS_Seed_CONFIDENCE = (BFS_HS_Seed_Prob*(1-BFS_HS_Seed_Prob)/SAMPLE_SIZE)
Mono_HSM_IFM_CONFIDENCE = (Mono_HSM_IFM_Prob*(1-Mono_HSM_IFM_Prob)/SAMPLE_SIZE)
Mono_HS_IF_Seed_CONFIDENCE = (Mono_HS_IF_Seed_Prob*(1-Mono_HS_IF_Seed_Prob)/SAMPLE_SIZE)
RSB_SEB_DSB_CONFIDENCE = (RSB_SEB_DSB_Prob*(1-RSB_SEB_DSB_Prob)/SAMPLE_SIZE)

print("Sample Size:", SAMPLE_SIZE)
print("Friendship Level", friendLevel)
print("Berry Finding S:", BFS)
print("BFS+HB:", BFS_HB)
print("BFS+Speed:", BFS_HS)
print()
print("Test: Mono Probability (11.11%):", Mono_Prob)
print("-- Berrymon -- ")
print("Est. BFS Probability:", BFS_Prob)
print("95% Confidence Level (Upper):", BFS_Prob + 1.96 * BFS_CONFIDENCE)
print("95% Confidence Level (Lower):", BFS_Prob - 1.96 * BFS_CONFIDENCE)
print("Est. BFS+HB Probability:", BFS_HB_Prob)
print("95% Confidence Level (Upper):", BFS_HB_Prob + 1.96 * BFS_HB_CONFIDENCE)
print("95% Confidence Level (Lower):", BFS_HB_Prob - 1.96 * BFS_HB_CONFIDENCE)
print("Est. BFS+Speed Probability:", BFS_HS_Prob)
print("95% Confidence Level (Upper):", BFS_HS_Prob + 1.96 * BFS_HS_CONFIDENCE)
print("95% Confidence Level (Lower):", BFS_HS_Prob - 1.96 * BFS_HS_CONFIDENCE)
print("Est. BFS+Speed Seed Probability:", BFS_HS_Seed_Prob)
print("95% Confidence Level (Upper):", BFS_HS_Seed_Prob + 1.96 * BFS_HS_Seed_CONFIDENCE)
print("95% Confidence Level (Lower):", BFS_HS_Seed_Prob - 1.96 * BFS_HS_Seed_CONFIDENCE)
print("-- Ingredientmon --")
print("Est. Mono HSM+IFM Probability:", Mono_HSM_IFM_Prob)
print("95% Confidence Level (Upper):", Mono_HSM_IFM_Prob + 1.96 * Mono_HSM_IFM_CONFIDENCE)
print("95% Confidence Level (Lower):", Mono_HSM_IFM_Prob - 1.96 * Mono_HSM_IFM_CONFIDENCE)
print("Est. Mono HS+IF Seed Probability:", Mono_HS_IF_Seed_Prob)
print("95% Confidence Level (Upper):", Mono_HS_IF_Seed_Prob + 1.96 * Mono_HS_IF_Seed_CONFIDENCE)
print("95% Confidence Level (Lower):", Mono_HS_IF_Seed_Prob - 1.96 * Mono_HS_IF_Seed_CONFIDENCE)
print("-- Misc --")
print("Est. RSB+SEB+DSB Probability:", RSB_SEB_DSB_Prob)
print("95% Confidence Level (Upper):", RSB_SEB_DSB_Prob + 1.96 * RSB_SEB_DSB_CONFIDENCE)
print("95% Confidence Level (Lower):", RSB_SEB_DSB_Prob - 1.96 * RSB_SEB_DSB_CONFIDENCE)