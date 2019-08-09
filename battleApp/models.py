from django.db import models


class post(models.Model):
    TorI = models.CharField(max_length=20)  # 팀전 개인전 여부
    title = models.CharField(max_length=20)
    Writer = models.CharField(max_length=20)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()

    def __str__(self):
        return self.title

class comment(models.Model):
    post = models.ForeignKey(
    post, on_delete=models.CASCADE, null=True, related_name='comments')
    comment_date = models.DateTimeField(auto_now_add=True)
    comment_contents = models.CharField(max_length=200)
    comment_type = models.CharField(max_length=10)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.comment_contents


