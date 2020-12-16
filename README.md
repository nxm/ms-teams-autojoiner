# Microsoft Teams AutoJoiner

You can join automatically on classes, when the teacher starts a meeting, then you'll join

## Installation

- Clone this repo `git clone https://github.com/nxm/ms-teams-autojoiner.git`
- Install requirements.txt `pip3 install -r requirements.txt`
- Run the program `python3 main.py`

## Configuration

Create file `config.json`

```json
{
    "login": "your email",
    "password": "your password",
    "webhookURL": "your discord webhook",
    "blacklist": ["className", "it's printing in console"]
}
```

## TODO

It's first version of program. Let me know if you have any issues!

- [ ] Add end of lesson detector
- [ ] Cleanup code
- [ ] Add logs to file/db

Written on Python3