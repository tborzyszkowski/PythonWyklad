from django.db import models
from django.db.models import Sum, Count
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.SlugField('Name')

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    
    def __unicode__(self):
        return self.name
    
    def countReferences(obj):
        return Question.objects.filter(categories__in=[obj]).count()
    countReferences.short_description = 'References'

class Vote(models.Model):
    user = models.ForeignKey(User, blank = True)
    date = models.DateTimeField('Date', auto_now_add=True)
    useragent = models.TextField('User agent', blank = True, null = True)
    ip = models.TextField("IP address", blank = True, null = True)
    vote = models.IntegerField("Vote")

    class Meta:
        verbose_name = 'Vote'
        verbose_name_plural = 'Votes'
    
    def __unicode__(self):
        return self.date.strftime("%Y-%m-%d %H:%M:%S") + " | " + self.ip + " | " + ("{0}").format(self.vote)

class Answer(models.Model):
    author = models.ForeignKey(User)
    answerDate = models.DateTimeField('Answer Date', auto_now_add=True)
    content = models.TextField('Content')
    votes = models.ManyToManyField(Vote, verbose_name = 'Votes', blank = True)

    def isAuthorVote(self, vote):
        if vote.user == self.author:
            return True
        else:
            return False
    
    def saveOrUpdateVote(self, vote):
        if self.votes.filter(user = vote.user).count() == 0:
            vote.save()
            self.votes.add(vote)
        else:
            obj = self.votes.get(user = vote.user)

            if obj.vote != vote.vote:
                obj.useragent = vote.useragent
                obj.ip = vote.ip
                obj.vote = vote.vote
                obj.save()

    def getRating(self):
        if self.votes.all().aggregate(Sum('vote')).get('vote__sum', 0) is None:
            return 0
        else:
            return self.votes.all().aggregate(Sum('vote')).get('vote__sum', 0)

    getRating.short_description = 'Votes'

    class Meta:
        verbose_name = 'Answer'
        verbose_name_plural = 'Answers'

    def __unicode__(self):
        return self.answerDate.strftime("%Y-%m-%d %H:%M:%S") + " | " + self.content

class View(models.Model):
    user = models.ForeignKey(User, blank = True, null = True)
    date = models.DateTimeField('Date', auto_now_add=True)
    useragent = models.TextField('User agent', blank = True, null = True)
    ip = models.TextField("IP address", blank = True, null = True)

    class Meta:
        verbose_name = 'View'
        verbose_name_plural = 'Views'
    
    def __unicode__(self):
        return self.date.strftime("%Y-%m-%d %H:%M:%S") + " | " + self.ip

class Question(models.Model):
    author = models.ForeignKey(User)
    title = models.CharField('Title', max_length = 255)
    askDate = models.DateTimeField('Ask Date', auto_now_add=True)
    content = models.TextField('Content')
    categories = models.ManyToManyField(Category, verbose_name = 'Categories', blank = True)
    answers = models.ManyToManyField(Answer, verbose_name = 'Answers', blank = True)
    views = models.ManyToManyField(View, verbose_name = 'Views', blank = True)
    votes  = models.ManyToManyField(Vote, verbose_name = 'Votes', blank = True)

    def isAuthorVote(self, vote):
        if vote.user == self.author:
            return True
        else:
            return False
    
    def saveOrUpdateVote(self, vote):
        if self.votes.filter(user = vote.user).count() == 0:
            vote.save()
            self.votes.add(vote)
        else:
            obj = self.votes.get(user = vote.user)

            if obj.vote != vote.vote:
                obj.useragent = vote.useragent
                obj.ip = vote.ip
                obj.vote = vote.vote
                obj.save()

    def getAnswerCount(self):
        return self.answers.all().count()

    def getRating(self):
        if self.votes.all().aggregate(Sum('vote')).get('vote__sum', 0) is None:
            return 0
        else:
            return self.votes.all().aggregate(Sum('vote')).get('vote__sum', 0)
    
    def getViews(self):
        return self.views.all().count()

    getRating.short_description = 'Votes'
    getViews.short_description = 'Views'

    class Meta:
        verbose_name = 'Question'
        verbose_name_plural = 'Questions'

    def __unicode__(self):
        return self.title


