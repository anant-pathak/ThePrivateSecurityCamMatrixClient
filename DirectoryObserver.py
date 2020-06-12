import watchdog.events
import watchdog.observers
import time
import os


class Handler(watchdog.events.PatternMatchingEventHandler):
    def __init__(self):
        # Set the patterns for PatternMatchingEventHandler
        watchdog.events.PatternMatchingEventHandler.__init__(self, patterns=['*.jpg'],
                                                             ignore_directories=True, case_sensitive=False)

    def on_created(self, event):
        print("Watchdog received created event - % s." % event.src_path)
        os.system('python3 EncryptionTestAdvanced.py {}'.format(event.src_path))
        print("returned from the Fn and uploaded the image and MIGHT delete it.")
        #os.system("rm -f {}".format(event.src_path))

        # Event is created, you can process it now

    # def on_modified(self, event):
    #     print("Watchdog received modified event - % s." % event.src_path)
    #     # Event is modified, you can process it now

    # def on_any_event(self, event):
    #     if event.is_directory:
    #         return None
    #
    #     elif event.event_type == 'created':
    #         # Event is created, you can process it now
    #         print("Watchdog received created event - % s." % event.src_path)
    #     elif event.event_type == 'modified':
    #         # Event is modified, you can process it now
    #         print("Watchdog received modified event - % s." % event.src_path)


if __name__ == "__main__":
    src_path = r"/Users/anantpathak/Learning/ProjectSecretCam/DummyFolder"
    event_handler = Handler()
    observer = watchdog.observers.Observer()
    observer.schedule(event_handler, path=src_path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()