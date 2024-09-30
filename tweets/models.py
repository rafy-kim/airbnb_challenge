from django.db import models
from common.models import CommonModel

# Create your models here.

class Tweet(CommonModel):
    payload = models.TextField(max_length=180, blank=True, null=True)
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username}: {self.payload}"
    
    def like_count(self):
        return self.likes.count()


class Like(CommonModel):
    user = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="likes",)
    tweet = models.ForeignKey("Tweet", on_delete=models.CASCADE, related_name="likes",)

    def __str__(self):
        return f"{self.user.username} likes {self.tweet.payload}"
