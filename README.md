# Random Fastapi

Creates random data using python, faker and serve it through fastapi

## Setup
This project includes using of split to demo how feature toggle work, you can create your own API key in [split.io](https://app.split.io) or you can just use the localhost as key (make sure you create a file $HOME/.split).

Copy dev.env to .env, and update the `SPLIT_KEY` value to your API Key
```
SPLIT_KEY=localhost
```

Run the application using uvicorn
```
uvicorn main:app --reload
```

Auto reload will update the app when there are code changes (to be removed when deploying to production)

### Site links:
- http://127.0.0.1:8000/docs
- http://127.0.0.1:8000/user/random
