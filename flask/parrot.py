def show_message(messages):
    for message  in messages:
        print (message)



def send_message(messages, sent_messages):
  while messages:
    current_message  =messages.pop()
    print(f"Moving {current_message}")
    sent_messages.append(current_message)

messages  = ['Babu', 'Laban', 'Kaimogul', 'Allan', 'Maureen']
sent_messages = []



show_message(messages)

send_message(messages, sent_messages)




