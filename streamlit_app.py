import streamlit as st
import feedparser

# You can update more Feeds as you like
rss_feeds = {
  "Select" : "",
  "ielts" : "https://morss.it/:items=||*[class=news1]||li/https://www.chinaielts.org/whats_new/ielts_news.shtml",
  "Times of India Top Stories" : "http://timesofindia.indiatimes.com/rssfeedstopstories.cms",
  "BBC" : "https://www.bbc.com/news/rss.xml",
  "The Guardian" : "https://www.theguardian.com/international/rss"
}

#Parses an RSS feed and returns a list of articles.
def parse_rss_feed(url):
  feed = feedparser.parse(url)
  articles = []
  for entry in feed.entries:
    article = {
      "title": entry.title,
      "link": entry.link,
      "description": entry.summary,
      "published_at": entry.published
    }
    articles.append(article)
  return articles

# Title
st.title("RSS Feed Reader")

# Choose a Feed
choose_news_feed = "**Select a News Feed:**"
rss_feed_selected = st.selectbox(choose_news_feed, rss_feeds.keys())
st.write(rss_feed_selected)
selected_rss_feed_url = rss_feeds[rss_feed_selected]

# Collect all Feeds
all_articles = []
articles = parse_rss_feed(selected_rss_feed_url)
all_articles += articles

# Sort articles by datetime
all_articles.sort(key=lambda article: article["published_at"], reverse=True)

#Display Articles
for article in all_articles:
  st.markdown(f"**{article['title']}**")
  st.markdown(f"{article['description']}", unsafe_allow_html=True)
  st.markdown(f"Published on: {article['published_at']}")
  st.markdown(f"Link: [More Info]({article['link']})")