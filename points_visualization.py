import os
import tomllib
import statistics

CHALLENGES_DIRECTORY = "."


def read_toml_file(file_path):
    if not os.path.exists(file_path):
        filename = os.path.basename(file_path)
        raise FileNotFoundError(
                f"Could not find toml file: '{filename}'"
        )

    with open(file_path, "rb") as file:
        return tomllib.load(file)

def get_challenge_data():
    challenge_data = []

    

    challenge_folders = [
        folder
        for folder in os.listdir(CHALLENGES_DIRECTORY)
        if not folder.startswith(".")
        and os.path.isdir(os.path.join(CHALLENGES_DIRECTORY, folder))
        # Skips directories starting with "." and only scans folders
    ]


    for challenge_id in challenge_folders:
        
        challenge_directory = challenge_id
        challenge_toml = os.path.join(challenge_directory, "challenge.toml")


        data = read_toml_file(challenge_toml)

        points = data["points"]
        difficulty = data["difficulty"]
        name = challenge_id

        challenge_data.append({
            "name": name,
            "points": points,
            "difficulty": difficulty,
        })
    return challenge_data




def main():
    challenges = get_challenge_data()
    challenges = sorted(challenges, key=lambda chall: chall["points"])

    points = []

    for challenge in challenges:
        print(f"diff: {challenge['difficulty']}, pts: {challenge['points']}, name: {challenge['name']}")


    
    # Get averages for each difficulty
    difficulties = {}
    for challenge in challenges:
        diff = challenge["difficulty"]
        if diff not in difficulties:
            difficulties[diff] = [challenge["points"]]
        
        else:
            difficulties[diff].append(challenge["points"])

    for difficulty, points_list in difficulties.items():
        mean = statistics.mean(points_list)
        count = len(points_list)
        print(f"Difficulty: {difficulty}, Mean score: {mean}, Count: {count}")




if __name__ == "__main__":
    main()

