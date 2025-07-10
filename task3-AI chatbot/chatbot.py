import spacy
import wikipedia

nlp = spacy.load("en_core_web_sm")
wikipedia.set_lang("en")

def search_wikipedia(query):
    try:
        summary = wikipedia.summary(query, sentences=2)
        return summary
    except wikipedia.exceptions.DisambiguationError as e:
        return f"Your query is ambiguous. Did you mean: {', '.join(e.options[:3])}?"
    except wikipedia.exceptions.PageError:
        return None
    except Exception as e:
        return None



def get_response(query):

    wiki_answer = search_wikipedia(query)
    if wiki_answer:
        return wiki_answer
    return "Sorry, I couldn't find a good answer to your question."

def chat():
    print("🤖 InfoBot (Wikipedia) — type 'quit' to exit")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['quit', 'exit']:
            print("InfoBot: Bye! Stay curious 👋")
            break
        response = get_response(user_input)
        print("InfoBot:", response)

if __name__ == "__main__":
    chat()
