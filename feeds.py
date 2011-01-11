from django.contrib.syndication.views import Feed
from blog.models import Entry
from video.models import Video

class LatestBlogFeed(Feed):
    title = "POP Galaxy blog feed"
    link = "/blog/"
    description = "The latest blog entries from POP Galaxy."

    def items(self):
        return Entry.objects.filter(status=1).order_by('-pub_date')[:10]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.body_markdown


class LatestVideoFeed(Feed):
    title = "POP Galaxy video feed"
    link = "/video/"
    description = "The latest videos from POP Galaxy."

    def items(self):
        return Video.objects.filter(isactive=True, syndicate=True).order_by('-pub_date')[:10]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.details
