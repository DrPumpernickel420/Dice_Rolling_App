def return_dices(rolls):
    dice = [
        ["┌─────────┐","│         │","│    ●    │","│         │","└─────────┘"],
        ["┌─────────┐","│  ●      │","│         │","│      ●  │","└─────────┘"],
        ["┌─────────┐","│  ●      │","│    ●    │","│      ●  │","└─────────┘"],
        ["┌─────────┐","│  ●   ●  │","│         │","│  ●   ●  │","└─────────┘"],
        ["┌─────────┐","│  ●   ●  │","│    ●    │","│  ●   ●  │","└─────────┘"],
        ["┌─────────┐","│  ●   ●  │","│  ●   ●  │","│  ●   ●  │","└─────────┘"],
    ]
    list_of_dices = [rolls[x:x+5] for x in range(0,len(rolls),5)]
    final_result = []
    for x in list_of_dices:
        result = []
        dices = [dice[i-1] for i in x]
        for x in range(0,5):
            result.append("   ".join([dice[x] for dice in dices]))
        final_result.append("\n".join(result))
    return "\n\n\n".join(final_result)
