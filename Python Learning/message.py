
def outbox(messages,sent):
    """
    append and pop
    """
    while messages:
        sending = messages.pop()
        sent.append(sending)
        print(f"Sending message {sending}")
def transfer(sent):
    """
    display
    """
    
    for sms in sent:
        print(f"\n Messages sent are : {sms}")
messages = [ 'Hi','whats Up', 'wanna come']
sent = []
outbox(messages[:],sent)
transfer(sent)
print(messages)