#Iam trying to build a Python project on a small version of Chatbot/ChatGPT.

#First, let's define what we mean by a "small version" of Chatbot/ChatGPT. 
# Chatbot/ChatGPT is a very large language model that has been trained on massive amounts of text data. 
# A smaller version of ChatGPT would be a model that has been trained on less data and has fewer parameters.

#One such model is the GPT-2 "117M" model, which has 117 million parameters compared to the full-sized GPT-2 model which has 1.5 billion parameters. 
# We can use this smaller model to build a simple chatbot.

#Here are the steps we can follow to build the project:

#1) Install the necessary libraries: We will need to install the transformers and torch libraries. These can be installed using pip.
#2) Load the model: We can load the pre-trained GPT-2 "117M" model using the AutoModelForCausalLM class from the transformers library.
#3) Initialize the tokenizer: We will need to initialize the tokenizer using the GPT2Tokenizer class from the transformers library.
#4) Define the chatbot function: We can define a function that takes in user input, tokenizes it, and generates a response using the pre-trained GPT-2 model. 
# The function can use a loop to continue the conversation until the user ends it.

# projectcode is:


from transformers import AutoModelForCausalLM, GPT2Tokenizer

# Load the pre-trained model
model = AutoModelForCausalLM.from_pretrained("gpt2")

# Initialize the tokenizer
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")

# Define the chatbot function
def chatbot():
    print("Welcome to the ChatGPT demo! Let's chat.")
    while True:
        # Get user input
        user_input = input("You: ")
        
        # Tokenize the input
        input_ids = tokenizer.encode(user_input, return_tensors='pt')
        
        # Generate a response
        output = model.generate(input_ids, max_length=50, do_sample=True)
        
        # Decode the response
        response = tokenizer.decode(output[0], skip_special_tokens=True)
        
        print("ChatGPT: " + response)
        
        # Check if the user wants to end the conversation
        if input("Do you want to end the conversation? (y/n): ").lower() == 'y':
            print("Goodbye!")
            break
        
#To run the chatbot, simply call the chatbot function:
chatbot()

#This will start the chatbot and allow the user to have a conversation with the GPT-2 "117M" model. 
#Keep in mind that this is a very simple implementation and there are many ways to improve upon it, but it should give you a good starting point.

