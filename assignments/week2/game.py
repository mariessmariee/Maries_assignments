import time, random, sys

def type_print(text, speed=0.03):
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(speed)
    print()

def pause(t=0.7):
    time.sleep(t)

def ask_choice(prompt, opts):
    opts_l = [o.lower() for o in opts]
    while True:
        ans = input(prompt).strip().lower()
        if ans in opts_l:
            return ans
        type_print("Please choose: " + " / ".join(opts_l))

def ask_int_in_range(prompt, lo, hi):
    while True:
        s = input(prompt).strip()
        try:
            v = int(s)
            if lo <= v <= hi:
                return v
            type_print(f"Enter a number between {lo} and {hi}.")
        except ValueError:
            type_print("Please enter a valid number.")

type_print("🏀 Welcome to Night Court: Lights Out Edition")
pause()
name = input("Player name: ").strip() or "Rookie"
jersey = input("Jersey color: ").strip() or "black"
type_print(f"Spotlights hit the {jersey} jersey. {name} steps onto the hardwood...")
pause(0.9)

type_print("Choose your pregame vibe: music / meditate / hype")
vibe = ask_choice("> ", ["music","meditate","hype"])
if vibe == "music":
    vibe_boost = 4
elif vibe == "meditate":
    vibe_boost = 3
else:
    vibe_boost = 6

diff = ask_int_in_range("Difficulty (1=rookie … 5=legend): ", 1, 5)
diff_mod = {1:+15,2:+7,3:0,4:-8,5:-15}[diff]

stamina = ask_int_in_range("Stamina today (1-10): ", 1, 10)
if stamina >= 9:
    stam_boost = 6
elif stamina >= 6:
    stam_boost = 3
else:
    stam_boost = 0

crowd = ask_choice("Crowd mood (loud/quiet): ", ["loud","quiet"])
if crowd == "loud":
    crowd_boost = 4
else:
    crowd_boost = 0

lucky = jersey.lower() in {"gold","crimson","royal","royal blue","scarlet"}
if lucky:
    type_print("✨ The crowd whispers: lucky colors tonight… (+3)")
pause(0.6)

type_print("Tip-off. The ball finds your hands.")
action = ask_choice("Do you shoot or pass? ", ["shoot","pass"])
pause(0.5)

score = 0

if action == "shoot":
    dist = ask_int_in_range("Range 1=close, 2=mid, 3=deep: ", 1, 3)
    if dist == 1:
        chance = 72
    elif dist == 2:
        chance = 52
    else:
        chance = 35

    shot = ask_choice("Shot type (layup/jumper/three): ", ["layup","jumper","three"])
    if shot == "layup":
        chance += 8
    elif shot == "jumper":
        chance += 0
    else:
        chance -= 6

    if dist == 3 and shot == "three":
        type_print("🎯 Heat-check from downtown…")
        chance += 6

    chance += vibe_boost + stam_boost + crowd_boost + diff_mod + (3 if lucky else 0)
    chance = max(5, min(95, chance))

    type_print(f"Releasing… (chance {chance}%)", 0.02)
    pause(1.0)
    roll = random.randint(1,100)
    if roll <= chance:
        type_print("✅ SWISH! Net barely moves.")
        score += 2 if dist < 3 else 3
        if dist == 3 and crowd == "loud":
            type_print("💥 The arena detonates. Momentum surges!")
    else:
        type_print("❌ Clanks off the iron.")
        if diff == 5 and stamina <= 3:
            type_print("🧢 Coach: \"We'll get an easier look next time.\"")

elif action == "pass":
    mate = ask_choice("Pass to A (shooter) or B (slasher)? ", ["a","b"])
    if mate == "a":
        base = 58 + vibe_boost + crowd_boost - (6 if diff >= 4 else 0)
        type_print("🎯 Catch-and-shoot…", 0.02); pause(0.6)
        if random.randint(1,100) <= base:
            type_print("✅ SPLASH! You notch the assist.")
            score += 3
        else:
            type_print("❌ Rims out. Good look though.")
    else:
        base = 62 + (3 if stamina >= 7 else 0) + (2 if lucky else 0)
        type_print("⚡ Baseline cut — attacking strong…", 0.02); pause(0.6)
        if random.randint(1,100) <= base:
            type_print("✅ AND-ONE! Crowd on its feet.")
            score += 2
        else:
            type_print("❌ Blocked at the summit!")

else:
    type_print("Hesitation. Turnover. The bench winces.")

pause(0.7)
chant = ask_choice("Start a chant? (yes/no): ", ["yes","no"])
if chant == "yes":
    type_print("📣 LET’S GO! The wave rolls around the arena.")
    score += 1
else:
    type_print("🤝 Calm nod. Business face on.")

pause(0.6)
risk = ask_choice("Final play: risk or safe? ", ["risk","safe"])
if risk == "risk":
    type_print("You call an iso at the logo…")
    final = 45 + (5 if vibe == "hype" else 0) + (4 if crowd == "loud" else 0) + (3 if lucky else 0) + diff_mod
    final = max(5, min(90, final))
    if random.randint(1,100) <= final:
        type_print("💫 STEPBACK DAGGER! Buzzer-beater glory.")
        score += 3
    else:
        type_print("🕐 Buzzer sounds… just off. Gasps everywhere.")
else:
    type_print("You run a safe set, milk the clock, get a steady look.")
    final = 60 + (2 if vibe == "meditate" else 0) + (2 if stamina >= 8 else 0) + diff_mod
    final = max(5, min(90, final))
    if random.randint(1,100) <= final:
        type_print("✅ Solid bucket. Job done.")
        score += 2
    else:
        type_print("❌ Short. It happens.")

pause(0.7)
type_print(f"📊 Final tally: {score} points")
if score >= 6:
    type_print("🏆 Player of the Night!")
elif score >= 3:
    type_print("👍 Strong contribution.")
else:
    type_print("🔁 Back to the gym tomorrow.")

again = ask_choice("Play again? (yes/no): ", ["yes","no"])
if again == "yes":
    type_print("Restarting… (demo build ends here)")
else:
    type_print("GGs. Thanks for playing!")