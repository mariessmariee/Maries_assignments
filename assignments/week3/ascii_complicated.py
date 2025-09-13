import time, random, sys

WAIT = 0.6
CLOSE = 78
MID = 54
FAR = 34
VIBE_BOOST = {"music": 4, "meditate": 3, "hype": 6}
DIFF_MOD = {1: +12, 2: +6, 3: 0, 4: -8, 5: -14}

def pause(t=WAIT):
    time.sleep(t)

def type_out(s, sp=0.02):
    for ch in s:
        sys.stdout.write(ch); sys.stdout.flush(); time.sleep(sp)
    print()

def ask_choice(prompt, opts):
    opts_l = [o.lower() for o in opts]
    while True:
        a = input(prompt).strip().lower()
        if a in opts_l: return a
        print("Options:", ", ".join(opts_l))

def ask_int(prompt, lo, hi):
    while True:
        s = input(f"{prompt} ({lo}-{hi}): ").strip()
        try:
            v = int(s)
            if lo <= v <= hi: return v
            print(f"Enter {lo}-{hi}.")
        except ValueError:
            print("Enter a number.")

def base_chance(dist):
    return CLOSE if dist == 1 else MID if dist == 2 else FAR

def shot_outcome(dist, vibe, diff, jersey):
    c = base_chance(dist)
    c += VIBE_BOOST.get(vibe, 0)
    c += DIFF_MOD.get(diff, 0)
    if jersey.lower() in {"gold","crimson","royal","white"}: c += 3
    return max(5, min(92, c))

def scene_pregame():
    name = input("Your name: ").strip() or "Rookie"
    color = input("Jersey color: ").strip() or "black"
    vibe = ask_choice("Pregame (music/meditate/hype): ", ["music","meditate","hype"])
    diff = ask_int("Difficulty", 1, 5)
    return name, color, vibe, diff

def scene_action(name, color, vibe, diff):
    type_out(f"Alright {name}, in your {color} jersey — tip-off!")
    pause()
    act = ask_choice("Action (shoot/pass): ", ["shoot","pass"])
    score = 0
    if act == "shoot":
        dist = ask_int("Distance 1=close 2=mid 3=far", 1, 3)
        chance = shot_outcome(dist, vibe, diff, color)
        type_out(f"Shooting… (chance {chance}%)", 0.015); pause(0.9)
        if random.randint(1,100) <= chance:
            print("Score!")
            score += 3 if dist == 3 else 2
            if dist == 3: print("Deep three!")
        else:
            print("Miss.")
            if diff >= 4: print("Tough defense tonight.")
    else:
        mate = ask_choice("Pass to A (shooter) or B (slasher): ", ["a","b"])
        if mate == "a":
            base = 56 + VIBE_BOOST.get(vibe, 0) + DIFF_MOD.get(diff, 0)
            print("Catch-and-shoot…"); pause()
            if random.randint(1,100) <= max(5, min(90, base)): print("Splash! Assist." ); score += 3
            else: print("Rim out.")
        else:
            base = 60 + (3 if color.lower() in {"gold","white"} else 0)
            print("Baseline cut…"); pause()
            if random.randint(1,100) <= base: print("And-one!"); score += 2
            else: print("Blocked!")
    return score

def scene_final(score, vibe, diff):
    risk = ask_choice("Final play (risk/safe): ", ["risk","safe"])
    if risk == "risk":
        ch = 44 + VIBE_BOOST.get(vibe, 0) + DIFF_MOD.get(diff, 0)
        print("Stepback at the buzzer…"); pause()
        if random.randint(1,100) <= max(5, min(88, ch)): print("Buzzer-beater!"); score += 3
        else: print("Just off…")
    else:
        ch = 62 + (2 if vibe == "meditate" else 0) + DIFF_MOD.get(diff, 0)
        print("Run a safe set…"); pause()
        if random.randint(1,100) <= max(5, min(90, ch)): print("Solid bucket."); score += 2
        else: print("Short.")
    print(f"Total points: {score}")
    if score >= 6: print("MVP vibes.")
    elif score >= 3: print("Strong contribution.")
    else: print("Back to drills.")
    return score

def main():
    type_out("🏀 Welcome to the Mini Basketball Game!")
    while True:
        name, color, vibe, diff = scene_pregame()
        sc = scene_action(name, color, vibe, diff)
        scene_final(sc, vibe, diff)
        again = ask_choice("Play again? (yes/no): ", ["yes","no"])
        if again == "no": print("GGs — thanks for playing!"); break

if __name__ == "__main__":
    main()
