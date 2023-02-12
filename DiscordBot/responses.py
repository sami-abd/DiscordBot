import random
from better_profanity import profanity

def handle_response(message) -> str:
    p_message = message.lower()
    
    if p_message == 'hello':
        return 'Salam'

    if p_message == '!dice':
        if random.randint(1,2) == 1:
            return "Heads"
        else:
            return "Tails"

    if p_message == '!help':
        return " Type !dice to flip a coin. \n Type hello for a greeting \n `Message Whatagwan#0001 for more help.`"

    if profanity.contains_profanity(p_message) :
        return "Your mouth needs some soap washing " + str(message.author)
