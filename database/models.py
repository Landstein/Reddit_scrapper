import sqlalchemy
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import sessionmaker, relationship



#Databases are collections of tables.  Tables are formatted with the select set of properties called columns
#each row in the table has a property associated with each column
#lines 16 - 21 define the columns and on line 14 will create a table called submission

#Spins up the database
Base = declarative_base()

class Submission(Base):
    __tablename__ = 'submission'

    id = Column(String, primary_key=True)
    author_fullname = Column(String)
    title = Column(String)
    url = Column(String)
    created_utc = Column(Date)
    subreddit_display_name = Column(String)

    subreddit_id = Column(String, ForeignKey("subreddit.id"))
    subreddit = relationship("Subreddit", back_populates="submissions")
    comments = relationship("Comment", back_populates="submission")

    def __repr__(self):
        return f"<Submission(id={self.id}, author_name={self.author_fullname}, {self.title}, {self.subreddit}, {self.url}, {self.created_utc})>"

#Relationship Class Below

class Subreddit(Base):
    __tablename__ = "subreddit"

    id = Column(String, primary_key=True)
    display_name = Column(String)
    subscribers = Column(Integer)
    submissions = relationship("Submission", back_populates="subreddit")

    def __repr__(self):
        return f"<Subreddit(id={self.id}, display_name={self.display_name}, subscribers={self.subscribers})>"

class Comment(Base):
    __tablename__ = "comment"

    id = Column(String, primary_key=True)
    author = Column(String)
    body = Column(String)
    score = Column(Integer)
    link_id = Column(String)
    submission_id = Column(String, ForeignKey("submission.id"))
    submission = relationship("Submission", back_populates="comments")

    def __repr__(self):
        return f"<Comment(id={self.id}, author={self.author}, body={self.body}, score={self.score}, " \
            f"link_id={self.link_id})>"

# class Address(Base):
#     __tablename__ = 'addresses'
#      id = Column(Integer, primary_key=True)
#      email_address = Column(String, nullable=False)
#      user_id = Column(Integer, ForeignKey('users.id'))
#
#      user = relationship("User", back_populates="addresses")



# {'_comments_by_id': {},
#  '_fetched': False,
#  '_reddit': <praw.reddit.Reddit object at 0x103bdbd30>,
#  'all_awardings': [],
#  'approved_at_utc': None,
#  'approved_by': None,
#  'archived': False,
#  'author': Redditor(name='AutoModerator'),
#  'author_flair_background_color': None,
#  'author_flair_css_class': None,
#  'author_flair_richtext': [],
#  'author_flair_template_id': None,
#  'author_flair_text': None,
#  'author_flair_text_color': None,
#  'author_flair_type': 'text',
#  'author_fullname': 't2_6l4z3',
#  'author_patreon_flair': False,
#  'banned_at_utc': None,
#  'banned_by': None,
#  'can_gild': True,
#  'can_mod_post': False,
#  'category': None,
#  'clicked': False,
#  'comment_limit': 2048,
#  'comment_sort': 'best',
#  'content_categories': None,
#  'contest_mode': False,
#  'created': 1561364229.0,
#  'created_utc': 1561335429.0,
#  'distinguished': 'moderator',
#  'domain': 'self.learnpython',
#  'downs': 0,
#  'edited': False,
#  'gilded': 0,
#  'gildings': {},
#  'hidden': False,
#  'hide_score': False,
#  'id': 'c4f68u',
#  'is_crosspostable': True,
#  'is_meta': False,
#  'is_original_content': False,
#  'is_reddit_media_domain': False,
#  'is_robot_indexable': True,
#  'is_self': True,
#  'is_video': False,
#  'likes': None,
#  'link_flair_background_color': '',
#  'link_flair_css_class': None,
#  'link_flair_richtext': [],
#  'link_flair_text': None,
#  'link_flair_text_color': 'dark',
#  'link_flair_type': 'text',
#  'locked': False,
#  'media': None,
#  'media_embed': {},
#  'media_only': False,
#  'mod_note': None,
#  'mod_reason_by': None,
#  'mod_reason_title': None,
#  'mod_reports': [],
#  'name': 't3_c4f68u',
#  'no_follow': True,
#  'num_comments': 104,
#  'num_crossposts': 0,
#  'num_reports': None,
#  'over_18': False,
#  'parent_whitelist_status': 'all_ads',
#  'permalink': '/r/learnpython/comments/c4f68u/ask_anything_monday_weekly_thread/',
#  'pinned': False,
#  'pwls': 6,
#  'quarantine': False,
#  'removal_reason': None,
#  'report_reasons': None,
#  'saved': False,
#  'score': 5,
#  'secure_media': None,
#  'secure_media_embed': {},
#  'selftext': 'Welcome to another /r/learnPython weekly "Ask Anything* Monday" '
#              'thread\n'
#              '\n'
#              'Here you can ask all the questions that you wanted to ask but '
#              "didn't feel like making a new thread.\n"
#              '\n'
#              "\\* It's primarily intended for simple questions but as long as "
#              "it's about python it's allowed.\n"
#              '\n'
#              'If you have any suggestions or questions about this thread use '
#              'the message the moderators button in the sidebar.\n'
#              '\n'
#              '**Rules:**\n'
#              '\n'
#              "* Don't downvote stuff - instead explain what's wrong with the "
#              'comment, if it\'s against the rules "report" it and it will be '
#              'dealt with.\n'
#              '\n'
#              "* Don't post stuff that doesn't have absolutely anything to do "
#              'with python. \n'
#              '\n'
#              "* Don't make fun of someone for not knowing something, insult "
#              'anyone etc - this will result in an immediate ban.\n'
#              '\n'
#              "That's it.",
#  'selftext_html': '<!-- SC_OFF --><div class="md"><p>Welcome to another <a '
#                   'href="/r/learnPython">/r/learnPython</a> weekly &quot;Ask '
#                   'Anything* Monday&quot; thread</p>\n'
#                   '\n'
#                   '<p>Here you can ask all the questions that you wanted to '
#                   'ask but didn&#39;t feel like making a new thread.</p>\n'
#                   '\n'
#                   '<p>* It&#39;s primarily intended for simple questions but '
#                   'as long as it&#39;s about python it&#39;s allowed.</p>\n'
#                   '\n'
#                   '<p>If you have any suggestions or questions about this '
#                   'thread use the message the moderators button in the '
#                   'sidebar.</p>\n'
#                   '\n'
#                   '<p><strong>Rules:</strong></p>\n'
#                   '\n'
#                   '<ul>\n'
#                   '<li><p>Don&#39;t downvote stuff - instead explain '
#                   'what&#39;s wrong with the comment, if it&#39;s against the '
#                   'rules &quot;report&quot; it and it will be dealt '
#                   'with.</p></li>\n'
#                   '<li><p>Don&#39;t post stuff that doesn&#39;t have '
#                   'absolutely anything to do with python. </p></li>\n'
#                   '<li><p>Don&#39;t make fun of someone for not knowing '
#                   'something, insult anyone etc - this will result in an '
#                   'immediate ban.</p></li>\n'
#                   '</ul>\n'
#                   '\n'
#                   '<p>That&#39;s it.</p>\n'
#                   '</div><!-- SC_ON -->',
#  'send_replies': False,
#  'spoiler': False,
#  'stickied': True,
#  'subreddit': Subreddit(display_name='learnpython'),
#  'subreddit_id': 't5_2r8ot',
#  'subreddit_name_prefixed': 'r/learnpython',
#  'subreddit_subscribers': 210240,
#  'subreddit_type': 'public',
#  'suggested_sort': 'new',
#  'thumbnail': '',
#  'title': 'Ask Anything Monday - Weekly Thread',
#  'total_awards_received': 0,
#  'ups': 5,
#  'url': 'https://www.reddit.com/r/learnpython/comments/c4f68u/ask_anything_monday_weekly_thread/',
#  'user_reports': [],
#  'view_count': None,
#  'visited': False,
#  'whitelist_status': 'all_ads',
#  'wls': 6}