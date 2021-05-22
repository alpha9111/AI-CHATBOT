pip install chatterbot
pip install chatterbot_corpus
pip install functions


def create_bot(name):

    from chatterbot import ChatBot

    Bot = ChatBot(name = name,

                  read_only = False,                  

                  logic_adapters = ["chatterbot.logic.BestMatch"],                 

                  storage_adapter = "chatterbot.storage.SQLStorageAdapter")

    return Bot

def train_all_data(Bot):

    from chatterbot.trainers import ChatterBotCorpusTrainer

    corpus_trainer = ChatterBotCorpusTrainer(Bot)

    corpus_trainer.train("chatterbot.corpus.english")

def custom_train(Bot, conversation):

    from chatterbot.trainers import ListTrainer

    trainer = ListTrainer(Bot)

    trainer.train(conversation)

def start_chatbot(Bot):

    print('\033c')

    print("Hello, I am Jordan. How can I help you")

    bye_list = ["bye jordan", "bye", "good bye"] 

    

    while (True):

        user_input = input("me: ")   

        if user_input.lower() in bye_list:

            print("Jordan: Good bye and have a Good day")

            break

        

        response = Bot.get_response(user_input)

        print("Jordan:", response)

home_bot = create_bot('Jordan')

train_all_data(home_bot)

identity = input("State your identity please: ")

if identity == "Mark":

    print("Welcome, Mark. Happy to have you at home.")

elif identity == "Jane":

    print("Mark is out right now, but you are welcome to the house.")

else:

    print("Your access is denied here.")

    exit()

# custom data

house_owner = [

    "Who is the owner of this house?",

    "Mark Nicholas is the owner of this house."

]

custom_train(home_bot, house_owner)

print("Training Data")

if identity == 'Mark':   

    city_born = [

        "Where was I born?",

        "Mark, you were born in India."

    ]

    fav_book = [

        "What is my favourite book?",

        "That is easy. Your favourite book is English Grammar."

    ]

    fav_movie = [

        "What is my favourite movie?",

        "You have watch end game so many time."

    ]

    fav_sports = [

        "What is my favourite sport?",

        "You have always loved raceing."

    ]

   

    custom_train(home_bot, city_born)

    custom_train(home_bot, fav_book)

    custom_train(home_bot, fav_movie)

    custom_train(home_bot, fav_sports)

start_chatbot(home_bot)
