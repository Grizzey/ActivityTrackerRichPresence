import discord_rpc
import time
import threading

if __name__ == '__main__':
    def readyCallback(current_user):
        print('Our user: {}'.format(current_user))


    def disconnectedCallback(codeno, codemsg):
        print('Disconnected from Discord rich presence RPC. Code {}: {}'.format(
            codeno, codemsg
        ))


    def errorCallback(errno, errmsg):
        print('An error occurred! Error {}: {}'.format(
            errno, errmsg
        ))


    # Note: 'event_name': callback
    callbacks = {
        'ready': readyCallback,
        'disconnected': disconnectedCallback,
        'error': errorCallback,
    }
    discord_rpc.initialize(input("Client ID: "), callbacks=callbacks, log=True)

    i = 0
    start = time.time()
    while i < 10:
        i += 1

        discord_rpc.update_presence(
            **{
                'details': 'Iteration # {}'.format(i),
                'start_timestamp': start,
                'large_image_key': 'default'
            }
        )

        discord_rpc.update_connection()
        time.sleep(2)
        discord_rpc.run_callbacks()

    discord_rpc.shutdown()
