# Docker Hub Refresh
Pulls all images for a user and removes them afterwards. Doing this at least once
every six months will mark the images as active to Docker Hub and stops them from
being deleted, due to being inactive for too long.

Run the script with Python3:
```python
python3 main.py
```

Output will be something like:
```
Pulling image screencom/php...
Removing image screencom/php...
Pulling image screencom/qsr-cron...
Removing image screencom/qsr-cron...
Pulling image screencom/qsr-php...
...
```
