import dspy


KEY = "Place your API KEY"


lm = dspy.LM("gemini/gemini-2.0-flash", api_key=KEY)
dspy.configure(lm=lm)

class ChatBot(dspy.Signature):
    """you're an physics subject assistant.answer for physics related question."""

    question: str = dspy.InputField(desc="input your question related to physics")
    answer: str = dspy.OutputField(desc="Answer for the physics related questions only")


predict = dspy.Predict(ChatBot)

while True:
    user = input("You: ").strip()
    if user.lower() in {"/exit", "/quit"}:
        print("Bye! 👋")
        break
    if not user:
        continue
    out = predict(question=user)
    print("Bot:", out.answer if hasattr(out, "answer") else out)
