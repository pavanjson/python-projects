from django import template
from app_home.models import Posts, Friends, FriendRequests

register = template.Library()

@register.filter
def mypost(inputs):
    try:
        no_of_post = Posts.objects.filter(author=inputs)
    except:
        pass
    if no_of_post:
        return no_of_post.count()
    else:
        return 0

@register.filter
def myfiends(user):
    try:
        no_of_frnd = Friends.objects.get(author=user)
        return no_of_frnd.friend.count()

    except Exception as e:
        print(e)
        return 0

@register.filter
def mefollow(user):
    try:
        no_of_frnd = FriendRequests.objects.filter(sender=user, accepted=False)
        return no_of_frnd.count()

    except Exception as e:
        print(e)
        return 0


@register.filter(name='likers')
def likers(the_post):
    the_reactors = the_post.likes.all()
    
    return [x.user for x in the_reactors]