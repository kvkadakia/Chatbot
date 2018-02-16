# Example 1: sets up service wrapper, sends initial message, and
# receives response.

import watson_developer_cloud
import re
# Set up Conversation service.
conversation = watson_developer_cloud.ConversationV1(
  username = '6286e2d7-08a6-4538-bc8f-c51446ef0190', # replace with username from service key
  password = 'dGyHwqZpcp7H', # replace with password from service key
  version = '2017-05-26'
)
workspace_id = 'c2861c71-c396-477f-a244-739d8783f2dd' # replace with workspace ID

# Initialize with empty value to start the conversation.
user_input = ''
context = {}

item = ''
itemnos = 0    	
order = {}
sum = 0

# Main input/output loop
while True:

  # Send message to Conversation service.
  response = conversation.message(
    workspace_id = workspace_id,
    input = {
      'text': user_input
    },
    context = context
  )
  
  # If an intent was detected, print it to the console.
  if response['intents']:
    print('Detected intent: #' + response['intents'][0]['intent'])

  # Print the output from dialog, if any.
  if response['output']['text']:
    print(response['output']['text'][0])
        
    match = re.match('([0-9]) (.*) has been added to your order', response['output']['text'][0])
    
    '''Add price for item'''
    if (match):
        item = match.group(2)
        itemnos = match.group(1)
        
    if (match):
        quantity = int(itemnos)*5
        sum = sum + quantity
        order[match.group(2)+ ': $' + str(quantity)] = match.group(1)
    
    if(response['output']['text'][0] == 'Hey your final order is:'):
        print('\n')
        for key in order:   
            print order[key] + " " + key
        print('\n')            
        print('Your order total is:' + " " + str(sum))    
            
  # Update the stored context with the latest received from the dialog.
  context = response['context']

  # Prompt for next round of input.
  user_input = input('>> ')
