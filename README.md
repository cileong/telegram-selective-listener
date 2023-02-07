# Telegram Selective Listening App

An app mounted on your Telegram account, listening only for messages from a list of users across all dialogs.

## Setup

1. Install the dependencies. Within the virtual environment of your choice:

    ```sh
    pip install -r requirements.txt
    ```

2. Sign in and create a new Telegram application [here](https://my.telegram.org/apps). Give the app a meaningful title and name. Record the API ID and hash.

3. Create a configuration file named `config.yaml` in the project root, and configure it as follows:

    ```yaml
    # Telegram login credentials.
    api_id: ********
    api_hash: ********************************

    # Usernames of users to be tracked.
    targets: ["@username1", "@username2",]
    ```

## Usage

Start the application:

```sh
python main.py
```

If this is your first time launching the application, you will be prompted to log in to Telegram.

Once you have logged in, the application will start listening for messages.

The messages of the target users will be logged on `stdout`.
