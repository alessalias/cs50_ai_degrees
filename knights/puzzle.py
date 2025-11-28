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
    # A is either a Knight or a Knave, but not both
    Or(
        And(AKnight, Not(AKnave)),
        And(AKnave, Not(AKnight))
    ),
    # If A is a Knight, then his statement is true
    Implication(AKnight, And(AKnight, AKnave)),
    # If A is a Knave, then his statement is false
    Implication(AKnave, Not(And(AKnight, AKnave)))
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(

    Or(
        And(AKnight, Not(AKnave)),
        And(AKnave, Not(AKnight))
    ),

    Or(
        And(BKnight, Not(BKnave)),
        And(BKnave, Not(BKnight))
    ),

    Or(
        Biconditional(AKnight, BKnave),
        Biconditional(AKnave, BKnight)
    ),

    Implication(AKnight, And(AKnave, BKnave)),
    Implication(AKnave, Not(And(AKnave, BKnave)))
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(

    Or(
        And(AKnight, Not(AKnave)),
        And(AKnave, Not(AKnight))
    ),

    Or(
        And(BKnight, Not(BKnave)),
        And(BKnave, Not(BKnight))
    ),

    Implication(
        AKnight, Or(
                    And(AKnave, BKnave),
                    And(AKnight, BKnight)
                )
    ),

    Implication(
        AKnave, Not(
                    Or(
                        And(AKnave, BKnave),
                        And(AKnight, BKnight)
                    )
                )
    ),

    Implication(
        BKnight, Or(
                And(AKnave, Not(BKnave)),
                And(AKnight, Not(BKnight))
            )
    ),

    Implication(
        BKnave, Not(
                    Or(
                        And(AKnave, Not(BKnave)),
                        And(AKnight, Not(BKnight))
                    )
                )
    ),
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    Or(
        And(AKnight, Not(AKnave)),
        And(AKnave, Not(AKnight))
    ),

    Or(
        And(BKnight, Not(BKnave)),
        And(BKnave, Not(BKnight))
    ),

    Or(
        And(CKnight, Not(CKnave)),
        And(CKnave, Not(CKnight))
    ),

    # A says either "I am a knight." or "I am a knave.", but you don't know which.
    Implication(AKnight, Or(And(AKnight, Not(AKnave)), And(AKnave, Not(AKnight)))),
    Implication(AKnave, Not(Or(And(AKnight, Not(AKnave)), And(AKnave, Not(AKnight))))),

    # B says "A said 'I am a knave'."
    # A’s statement “I am a knave” is represented as AKnave because that’s literally what A is asserting about himself
    Implication(BKnight, AKnave),
    Implication(BKnave, Not(AKnave)),

    # B says "C is a knave."
    Implication(BKnight, CKnave),
    Implication(BKnave, Not(CKnave)),

    # C says "A is a knight."
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
