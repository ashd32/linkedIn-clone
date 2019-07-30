import os.path

def _save_logs(filename, logs):
    with open('app/logs/{filename}.log'.format(filename=filename), 'a') as f:
        f.write(logs)


def _create_file_and_save_logs(filename, logs):
    with open('app/logs/{filename}.log'.format(filename=filename), 'w') as f:
        f.write(logs)


def process_logs(filename, request):
    if os.path.isfile('app/logs/{filename}.log'.format(filename=filename)):
        _save_logs(filename, str(request.body))
    else:
        _create_file_and_save_logs(filename, str(request.body))
    return True

