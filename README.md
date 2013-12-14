hnscrape
--------

Pretty straightforward, this one. It scrapes the stories off of the first and
second pages of [Hacker News](https://news.ycombinator.com). It has one useful
function, `get_stories()`. This will return a list of dictionaries that represent
the stories parsed from Hacker News' notoriously old-school html. Values are

* *comments*: The number of comments on the article, 0 for a job posting
* *id*: The hacker news id on an article, 0 for a job posting
* *points*: The number of points for the article, None for a job posting
* *rank*: Story rank
* *time*: Plain-text human-readable time story was posted; None for a job
  posting
* *title*: Posting title
* *url*: Posting URL
* *user*: User who posted the article; None for a job posting

Installation
------------

    pip install git+https://github.com/njl/hnscrape.git#egg=hnscrape

This should install the requirements: lxml, requests, and cssselect.

Don't Be A Jerk
---------------
You don't need to run this very often; cache results, and don't hit the servers
more than once every couple of minutes.

LICENSE
-------
Look in the `LICENSE` file. MIT license.

