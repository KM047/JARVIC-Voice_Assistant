# import socket

# def test_net():
#     try:
#         socket.create_connection(('Google.com', 80))
#         return True
#     except OSError:
#         print(1)
#         return False

# print(test_net())




'''

Remember ----
News
Calculator
Shutdownsystem -----
Scedule your day
focus mode
translator

'''



from pocketsphinx import LiveSpeech
for phrase in LiveSpeech():
    print(phrase)