# SaintCTF Challenges 2024
This repository stores the challenges for SaintCTF 2024.

## Installation
>[!NOTE]
> These steps assume you already have SaintCTF installed on your system. Please install SaintCTF first!
1. Navigate into the '/challenges/' folder in your SaintCTF installation.
2. Run this command:
```bash
git clone https://github.com/SaintNong/SaintCTF_Challenges_2024.git .
```

3. Now go back to the root directory of SaintCTF and run the server.
4. The challenges should now be deployed on the website!

## Some loose guidelines for new challenges on this repo
- If your challenge is short, (i.e. around 1 or 2 commits), then you do not *need* to create a branch.
  - e.g. Some crypto challenges just need container.toml and that's it.
- Otherwise, please create a branch for your challenge which will be merged onto main.
  - This is especially true for containerized challenges, where for example you may need to build an entire web app for your challenge. Please, we urge you, do all of that on a branch.

## How do I make challenges?
Note, these steps assume you followed the installation instructions at the top of this page.

Making challenges is easy, just follow these few steps:

1. Create a folder (in this repo) named after your challenge. (e.g. 'example_challenge')

2. Create the file 'challenge.toml' and copy and paste the example configuration below, then edit the values to suit your challenge.
```toml
name = "Example"
author = "ning"
description = """
This is a great example.
What a great example challenge!
Lets all just sit back and admire how great of an example this is..."""
category = "misc"
difficulty = "easy"
points = 10
flag = "saint{example}"
```
3. If there are any files required to solve your challenge, create folder named '/downloads/' in your challenge directory and place downloadable files there.

4. Your challenge is now ready for deployment. Just run the site and see your challenge in action!

### Challenge docker container (optional)
5. If your challenge requires a docker container to be run, create a container.toml file in your challenge directory.
An example is provided here:
```toml
tag = "example_container"
port = 3001
```

6. Create a folder named '/container/' in your challenge folder
>[!NOTE]
> If 'container.toml' is defined but '/container/' does not exist, the CTF will not run.

7. Place your Dockerfile and your container files in this folder. Be sure to use the same port in your Dockerfile as defined in your 'container.toml'.

8. If docker is installed on your server, then your container will now be automatically deployed whenever the server starts!
