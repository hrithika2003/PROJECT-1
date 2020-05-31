from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

 # Puzzle 0
 # A says "I am both a knight and a knave."
knowledge0 = And(
    Or(AKnight, AKnave),
    Implication(AKnight, Not(AKnave)),
    Implication(AKnave, Not(AKnight)),

    Implication(AKnight, And(AKnave, AKnight)),
)

 # Puzzle 1
 # A says "We are both knaves."
 # B says nothing.
knowledge1 = And(
    Or(AKnight, AKnave),
    Implication(AKnight, Not(AKnave)),
    Implication(AKnave, Not(AKnight)),

    Or(BKnight, BKnave),
    Implication(BKnight, Not(BKnave)),
    Implication(BKnave, Not(BKnight)),

   # A says "We are both knaves."
   # If A tells truth:
   Implication(AKnight, And(AKnave, BKnave)),
   # If A tells lie:
   Implication(AKnave, Not(And(AKnave, BKnave))), 
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
   Or(AKnight, AKnave),
   Implication(AKnight, Not(AKnave)),
   Implication(AKnave, Not(AKnight)),
  
   # A says "We are the same kind."
   # If A is telling truth:
   Implication(AKnight, Or(
       And(AKnight, BKnight),
       And(AKnave, BKnave),
   )),
   # If A is telling a lie:
   Implication(AKnave, Not(
       Or(And(AKnight, BKnight),
          And(AKnave, BKnave)
       )
   )),

   # B says "We are of different kinds."
   # If B is telling truth:
   Implication(BKnight, Or(
       And(AKnight, BKnave),
       And(AKnave, BKnight)
   )),

   # If B is telling a lie:
   Implication(BKnave, Not(Or(
       And(AKnight, BKnave),
       And(AKnave, BKnight)
   ))
  )
)
 
# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
   Or(AKnight, AKnave),
   Implication(AKnight, Not(AKnave)),
   Implication(AKnave, Not(AKnight)),
   Not(And(AKnight, AKnave)),

   Or(BKnight, BKnave),
   Implication(BKnight, Not(BKnave)),
   Implication(BKnave, Not(BKnight)),
   Not(And(BKnight, BKnave)),

   Or(CKnight, CKnave),
   Implication(CKnight, Not(CKnave)),
   Implication(CKnave, Not(CKnight)),
   Not(And(CKnight, CKnave)),

  # A says either "I am a knight." or "I am a knave.", but you don't know which.
  # If A is telling the truth:
  Implication(AKnight, Or(AKnight, AKnave)),
  # If A is telling a lie:
  Implication(AKnave, Not(Or(AKnight, AKnave))),

  # B says "A said 'I am a knave'."
  # B says "C is a knave."
  # If B is telling truth:
  Implication(BKnight, CKnave),
  Implication(BKnight, Or(
      # If A is telling the truth:
      Implication(AKnight, AKnave)))

  # If B is telling a lie:
  Implication(BKnave, Not(CKnave))
  Implication(BKnave, Or(
  Not(Implication(AKnight,AKnave)),
  Not(Implication(AKnave, Not(AKnight)))
  )
 ),

 # C says "A is a knight."
 # If C is telling the truth:
 Implication(CKnight, AKnight),
 Implication(CKnave, Not(AKnight))
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
