from typing import List
 
def csMakeItJazzy(chords: List[str]) -> List[str]:
    chords_7 = []
    for i in chords:
        if '7' in i:
            chords_7.append(i)
        else:
            chords_7.append(i + f"7")
    return chords_7