import webbrowser
from win10toast_click import ToastNotifier

# Create a toast notifier object
toaster = ToastNotifier()

def show_toast(title, message, job_link):

    toaster.show_toast(
        title,
        message,
        icon_path="127435039.ico",
        duration=None,
        threaded=False,
        callback_on_click=lambda: webbrowser.open(f"{job_link}")
    )