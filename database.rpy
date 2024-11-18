init python:
    import json
    import os

    # Path to the JSON file (stored in the game directory)
    DB_PATH = os.path.join(config.basedir, "game_database.json")

    # Save a player name to the JSON file
    def save_player_to_database(player_name):
        try:
            # If the JSON file does not exist, create it with an empty list
            if not os.path.exists(DB_PATH):
                with open(DB_PATH, "w") as db_file:
                    json.dump([], db_file)

            # Read the current data from the JSON file
            with open(DB_PATH, "r+") as db_file:
                data = json.load(db_file)

                # Add the player name if it doesn't already exist
                if player_name not in data:
                    data.append(player_name)
                    db_file.seek(0)
                    json.dump(data, db_file, indent=4)
                    print(f"Saved player: {player_name}")
                else:
                    print(f"Player {player_name} already exists.")
        except Exception as e:
            print(f"Error saving player: {e}")

    # Fetch all saved nicknames from the JSON file
    def fetch_saved_nicknames():
        try:
            # If the file exists, read and return its contents
            if os.path.exists(DB_PATH):
                with open(DB_PATH, "r") as db_file:
                    return json.load(db_file)
            else:
                return []  # Return an empty list if the file does not exist
        except Exception as e:
            print(f"Error fetching nicknames: {e}")
            return []
