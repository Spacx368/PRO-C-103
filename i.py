class FileEventHandler (FileSystemEventHandler):
    def on_created(self, event):
        print("Hey, {event.src_path} has been created!")

    def on_deleted(self, event):
        print("Oops! Someone deleted {event.src_path}!")

    try:
        while True:
            time.sleep(2)
            print("running...")
        except KeyboardInterrupt:
            print("Stopped!")
            observer.stop