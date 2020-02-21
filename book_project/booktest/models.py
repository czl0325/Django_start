from django.db import models


# Create your models here.
# 定义图书模型类BookInfo
class BookInfo(models.Model):
    btitle = models.CharField(max_length=50)
    bpub_date = models.DateField()
    bread = models.PositiveIntegerField(default=0)  # 阅读量
    bcomment = models.PositiveIntegerField(default=0)  # 评论量
    isDelete = models.BooleanField(default=False)  # 逻辑删除

    def __str__(self):
        return "id：{id}，书名：{btitle}，发行日期：{bpub_date}，阅读量：{bread}，评论量：{bcomment}".format(id=self.id, btitle=self.btitle,bpub_date=self.bpub_date,bread=self.bread,bcomment=self.bcomment)

    class Meta:
        db_table = "bookinfo"


# 定义英雄模型类HeroInfo
class HeroInfo(models.Model):
    hname = models.CharField(max_length=20)                 # 英雄姓名
    hgender = models.BooleanField(default=True)             # 英雄性别
    isDelete = models.BooleanField(default=False)           # 逻辑删除
    hcomment = models.CharField(max_length=200, null=True, blank=False)
    hbook = models.ForeignKey('BookInfo', on_delete=models.CASCADE)           # 英雄与图书表的关系为一对多，所以属性定义在英雄模型类中

    class Meta:
        db_table = "heroinfo"
