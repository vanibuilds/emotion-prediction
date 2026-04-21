print("=== Complete Human Emotion & Condition Detector ===")

while True:
    text = input("\nEnter your message: ").lower()

    happy_words = ["happy", "joy", "good", "great", "smile"]
    sad_words = ["sad", "cry", "bad", "upset", "depressed"]
    angry_words = ["angry", "mad", "furious"]
    love_words = ["love", "lovely", "care", "affection", "dear"]
    romantic_words = ["romantic", "date", "kiss", "hug"]
    hate_words = ["hate", "dislike"]
    stress_words = ["stress", "stressed", "struggling", "pressure", "tension"]
    excited_words = ["excited", "wow", "amazing", "thrilled"]
    enjoy_words = ["enjoy", "fun", "funny", "enjoyed"]
    addiction_words = ["addicted", "addiction", "craving", "obsessed", "habit", "can't stop"]
    sick_words = ["sick", "fever", "headache", "pain", "ill"]
    sleep_words = ["sleepy", "sleep", "tired", "drowsy"]

    if any(word in text for word in happy_words):
        print("Detected Emotion: Happy 😊")

    elif any(word in text for word in sad_words):
        print("Detected Emotion: Sad 😢")

    elif any(word in text for word in angry_words):
        print("Detected Emotion: Angry 😠")

    elif any(word in text for word in love_words):
        print("Detected Emotion: Loving / Caring 🥰")

    elif any(word in text for word in romantic_words):
        print("Detected Emotion: Romantic ❤️")

    elif any(word in text for word in hate_words):
        print("Detected Emotion: Hate 😡")

    elif any(word in text for word in stress_words):
        print("Detected Emotion: Stressed / Struggling 😣")

    elif any(word in text for word in excited_words):
        print("Detected Emotion: Excited 🤩")

    elif any(word in text for word in enjoy_words):
        print("Detected Emotion: Enjoyment 😄")

    elif any(word in text for word in addiction_words):
        print("Detected Emotion: Addiction / Craving ⚠️")

    elif any(word in text for word in sick_words):
        print("Detected Condition: Sick 🤒")

    elif any(word in text for word in sleep_words):
        print("Detected Condition: Sleepy 😴")

    else:
        print("Detected Emotion: Neutral 😐")

    choice = input("\nDo you want to continue? (yes/no): ")
    if choice.lower() != "yes":
        print("Thank you!")
        break