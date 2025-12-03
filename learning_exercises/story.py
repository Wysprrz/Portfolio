import sys
import time

def typewriter(text, speed=0.03):
    """Print text like a typewriter safely, even in .exe builds."""
    for char in text:
        try:
            sys.stdout.write(char)
            sys.stdout.flush()
        except Exception:
            # fallback in case stdout is unavailable
            print(char, end='', flush=True)
        time.sleep(speed)
    print()


while True:

    # ---------------- Shared Beginning ----------------
    inventory = []

    typewriter("\n=== INTO THE DARK ===\n")

    typewriter("You’d known her for years—late-night messages, inside jokes, voice calls that stretched until sunrise.")
    typewriter("Online friendships always lived in that strange half-real place, where someone could feel closer than people you saw every day.\n")
    input("Press Enter to continue...")

    typewriter("\nTonight was supposed to be normal.")
    typewriter("Smoke.")
    typewriter("Music.")
    typewriter("Your dog asleep at your feet.\n")
    input("Press Enter to continue...")

    typewriter("\nThen your phone buzzed.")
    typewriter("bzzz.\n")
    input("Press Enter to pick up your phone...")

    typewriter("\nYou pick up your phone. It’s a text from Nena:\n")
    typewriter("Nena: Hey, come outside, I came to visit you silly! Surprise :P\n")
    input("Press Enter to continue...")

    typewriter("Your stomach flips.")
    typewriter("She’d never shown up before. Not like this.")
    typewriter("Still… curiosity wins.")
    typewriter("It always does.\n")

    typewriter("You change your clothes.")
    typewriter("Grab your keys.")
    typewriter("Step out into the quiet night where the city hums low and distant.\n")

    typewriter("Neon lights blink.")
    typewriter("Somewhere, someone laughs.")
    typewriter("Somewhere, a train groans along steel.\n")

    typewriter("When you reach the rooftop, she’s already there—")
    typewriter("Leaning against the railing.")
    typewriter("Hair catching the glow of the streetlights.")
    typewriter("Smiling like she’s been waiting all her life for this moment.\n")

    typewriter("You both look up.")
    typewriter("The sky is clear.")
    typewriter("Stars everywhere.\n")

    typewriter("And now…")
    typewriter("The choice you made decides everything.\n")

    typewriter("Did you bring:")
    typewriter("A: Knife")
    typewriter("B: Condoms")
    typewriter("C: Stuffed Bunny\n")

    choice = input("Type A, B, or C: ").upper()

    if choice == "A":
        inventory.append("Knife")
        typewriter("\nYou slipped the knife into your pocket.")

    elif choice == "B":
        inventory.append("Condoms")
        typewriter("\nYou stuffed the condoms into your bag.")

    else:
        inventory.append("Stuffed Bunny")
        typewriter("\nYou hugged the stuffed bunny and brought it with you.")

    typewriter(f"\nYour inventory: {inventory}")
    input("\nPress Enter to continue...")


    # ---------------- ENDINGS ----------------

    if "Stuffed Bunny" in inventory:
        typewriter("\n--- NEUTRAL ENDING: FALLING STARS ---\n")

        typewriter("You pull out the stuffed bunny and hand it to her.")
        typewriter("She blinks at it, then laughs softly like she’s trying not to cry.\n")

        typewriter("She holds it to her chest.")
        typewriter("You light up together.")
        typewriter("The smoke drifts upward into the cold air.\n")

        typewriter("A shooting star streaks the sky.")
        typewriter("Then another.")
        typewriter("Then another.\n")

        typewriter("They stop streaking.")
        typewriter("They start falling.\n")

        typewriter("The first hits miles away.")
        typewriter("The second hits closer.")
        typewriter("The third screams straight toward you.\n")

        typewriter("You grab her hand.")
        typewriter("She squeezes back.\n")

        typewriter('"One last star," she whispers.\n')

        typewriter("The sky shatters in white fire.")
        typewriter("You kiss as the light consumes everything.\n")

        typewriter("You die together.")
        typewriter("Holding hands.")
        typewriter("Under the falling stars.\n")

        typewriter("THE END.")


    elif "Condoms" in inventory:
        typewriter("\n--- GOOD ENDING: THE MORNING ---\n")

        typewriter("You both laugh awkwardly when you pull them out.")
        typewriter("“Always prepared, huh?” she teases.\n")

        typewriter("You shrug.")
        typewriter("She smirks.\n")

        typewriter("The stars come out slow tonight.")
        typewriter("Soft streaks of silver across the dark.\n")

        typewriter("You smoke together on the rooftop.")
        typewriter("Shoulder to shoulder.")
        typewriter("The city fades away.\n")

        typewriter("One kiss becomes two.")
        typewriter("Two becomes many.\n")

        typewriter("Later, the world dissolves into heat and tangled sheets.")
        typewriter("Somewhere you don’t even remember walking to.\n")

        input("Press Enter to wake up...")

        typewriter("\nMorning light through cheap blinds.")
        typewriter("An empty room.")
        typewriter("Your phone still charging.\n")

        typewriter("Your wallet is gone.")
        typewriter("So is she.\n")

        typewriter("On the pillow, a folded note reads:\n")
        typewriter('"tee hee. thanks for the moni stranger <3"\n')

        typewriter("Your card is maxed.")
        typewriter("Your savings are wiped.")
        typewriter("Your heart is confused.\n")

        typewriter("When you check your phone later…")
        typewriter("She’s blocked.")
        typewriter("Vanished.\n")

        typewriter("Like a shooting star that burned out.\n")

        typewriter("You survived.")
        typewriter("You just paid the price.\n")

        typewriter("THE END.")


    elif "Knife" in inventory:
        typewriter("\n--- BAD ENDING: FOREVER YOURS ---\n")

        typewriter("You keep the knife hidden in your pocket.\n")

        typewriter("She brings a drink from the stairwell.")
        typewriter("Hands it to you with that same sweet smile.\n")

        typewriter("You talk.")
        typewriter("You laugh.")
        typewriter("The stars look wrong tonight.\n")

        typewriter("You take a sip.")
        typewriter("Then another.\n")

        typewriter("The world tilts.\n")

        typewriter("Your limbs feel heavy.")
        typewriter("Wrong.")
        typewriter("Distant.\n")

        typewriter("You try to stand.")
        typewriter("Your body refuses.\n")

        typewriter("The knife slips from your pocket.")
        typewriter("It clatters uselessly across the concrete.\n")

        typewriter("She kneels beside you as the darkness pulls in.")
        typewriter("Her face fills your vision.")
        typewriter("Gentle.")
        typewriter("Loving.")
        typewriter("Terrible.\n")

        typewriter("She strokes your hair as the last light fades.\n")

        typewriter("The final words you ever hear are whispered like a lullaby:\n")
        typewriter('"You\'ll be mine forever, pee <3"\n')

        typewriter("And then there is nothing.\n")

        typewriter("THE END.")


    # ---------------- REPLAY ----------------
    again = input("\nPlay again? (Y/N): ").upper()

    if again != "Y":
        typewriter("\nThanks for playing.")
        break
