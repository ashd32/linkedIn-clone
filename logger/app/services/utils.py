def save_logs(filename, logs):
    with open('logs/{filename}.log'.format(filename=filename), 'a') as f:
        f.write(logs)


