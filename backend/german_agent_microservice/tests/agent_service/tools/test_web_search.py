import sys, os
testdir = os.path.dirname(__file__)
srcdir = '../../../src/agent_service/tools/'
sys.path.insert(0, os.path.abspath(os.path.join(testdir, srcdir)))
import web_search_tool
import json
import unittest
sys.path.insert(0, os.path.abspath(testdir))
class TestWebSearchTool(unittest.TestCase):
    res_dict = { "organic_results":[
            {
            "position": 1,
            "title": "Coffee",
            "link": "https://en.wikipedia.org/wiki/Coffee",
            "redirect_link": "https://www.google.com/url?sa=t&source=web&rct=j&opi=89978449&url=https://en.wikipedia.org/wiki/Coffee&ved=2ahUKEwiR5vqbm5KDAxUJSzABHetUBPsQFnoECA8QAQ",
            "displayed_link": "https://en.wikipedia.org › wiki › Coffee",
            "thumbnail": "https://serpapi.com/searches/644b696a15afff2c2fdb8474/images/ed8bda76b255c4dc4634911fb134de5319e08af7e374d3ea998b50f738d9f3d2.jpeg",
            "favicon":  "https://serpapi.com/searches/647d7f362c2c2a3962879557/images/eaae281147a6573e1938c032f47c3595217b0dd06301405bb682756bcef85f10.png",
            "snippet": "Coffee is a beverage prepared from roasted coffee beans. Darkly colored, bitter, and slightly acidic, coffee has a stimulating effect on humans, ...",
            "snippet_highlighted_words": [
                "Coffee",
                "coffee",
                "coffee"
            ],
            "sitelinks": {
                "inline": [
                {
                    "title": "Coffee bean",
                    "link": "https://en.wikipedia.org/wiki/Coffee_bean"
                },
                {
                    "title": "History",
                    "link": "https://en.wikipedia.org/wiki/History_of_coffee"
                },
                {
                    "title": "Coffee production",
                    "link": "https://en.wikipedia.org/wiki/Coffee_production"
                },
                {
                    "title": "Coffee preparation",
                    "link": "https://en.wikipedia.org/wiki/Coffee_preparation"
                }
                ]
            },
            "rich_snippet": {
                "bottom": {
                "extensions": [
                    "Region of origin: Kaffa in Horn of Africa",
                    "Introduced: 15th century",
                    "Ingredients: Roasted coffee beans",
                    "Flavor: Distinctive, somewhat bitter"
                ],
                "detected_extensions": {
                    "introduced_th_century": 15
                }
                }
            },
            "about_this_result": {
                "source": {
                "description": "Wikipedia is a multilingual free online encyclopedia written and maintained by a community of volunteers, known as Wikipedians, through open collaboration and using a wiki-based editing system called MediaWiki. Wikipedia is the largest and most-read reference work in history.",
                "source_info_link": "https://en.wikipedia.org/wiki/Coffee",
                "security": "secure",
                "icon": "https://serpapi.com/searches/644b696a15afff2c2fdb8474/images/ed8bda76b255c4dc4634911fb134de53068293b1c92f91967eef45285098b61516f2cf8b6f353fb18774013a1039b1fb.png"
                }
            },
            "about_page_link": "https://www.google.com/search?q=About+https://en.wikipedia.org/wiki/Coffee&tbm=ilp&ilps=ADJL0izANxNmAZazzpMAeGlkd2tXrw-aIQ",
            "about_page_serpapi_link": "https://serpapi.com/search.json?engine=google_about_this_result&google_domain=google.com&ilps=ADJL0izANxNmAZazzpMAeGlkd2tXrw-aIQ&q=About+https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FCoffee",
            "cached_page_link": "https://webcache.googleusercontent.com/search?q=cache:U6oJMnF-eeUJ:https://en.wikipedia.org/wiki/Coffee&cd=19&hl=en&ct=clnk&gl=us",
            "related_pages_link": "https://www.google.com/search?gl=us&hl=en&q=related:https://en.wikipedia.org/wiki/Coffee+Coffee",
            "source": "Wikipedia"
            },
            {
            "position": 2,
            "title": "The Coffee Bean & Tea Leaf | CBTL",
            "link": "https://www.coffeebean.com/",
            "redirect_link": "https://www.google.com/url?sa=t&source=web&rct=j&opi=89978449&url=https://www.coffeebean.com/&ved=2ahUKEwj3gdzSm5KDAxXdIEQIHW5OCPkQFnoECAkQAQ",
            "displayed_link": "https://www.coffeebean.com",
            "favicon":  "https://serpapi.com/searches/647d7f362c2c2a3962879557/images/eaae281147a6573e1938c032f47c3595277a9cb2cabd3d308557d74427b8c62d.png",
            "snippet": "Born and brewed in Southern California since 1963, The Coffee Bean & Tea Leaf® is passionate about connecting loyal customers with carefully handcrafted ...",
            "snippet_highlighted_words": [
                "Coffee"
            ],
            "sitelinks": {
                "inline": [
                {
                    "title": "Store locator",
                    "link": "https://www.coffeebean.com/store-locator"
                },
                {
                    "title": "Coffee",
                    "link": "https://www.coffeebean.com/cafe-menu/coffee"
                },
                {
                    "title": "Cafe Menu",
                    "link": "https://www.coffeebean.com/cafe-menu"
                },
                {
                    "title": "Coffee Sourcing",
                    "link": "https://www.coffeebean.com/our-story/coffee-sourcing"
                }
                ]
            },
            "about_this_result": {
                "source": {
                "description": "The Coffee Bean & Tea Leaf is an American coffee shop chain founded in 1963. Since 2019, it is a trade name of Ireland-based Super Magnificent Coffee Company Ireland Limited. Its 80% stake is by multinational company Jollibee Foods Corporation.",
                "source_info_link": "https://www.coffeebean.com/",
                "security": "secure",
                "icon": "https://serpapi.com/searches/644b696a15afff2c2fdb8474/images/ed8bda76b255c4dc4634911fb134de536aae041ac4d3ec38c806b5ac043223330ee0f1a11b201598d2e5fe218962b69a.png"
                }
            },
            "about_page_link": "https://www.google.com/search?q=About+https://www.coffeebean.com/&tbm=ilp&ilps=ADJL0iyEMfWcc_F0sQp68evlFpMNONzA7w",
            "about_page_serpapi_link": "https://serpapi.com/search.json?engine=google_about_this_result&google_domain=google.com&ilps=ADJL0iyEMfWcc_F0sQp68evlFpMNONzA7w&q=About+https%3A%2F%2Fwww.coffeebean.com%2F",
            "cached_page_link": "https://webcache.googleusercontent.com/search?q=cache:WpQxSYo2c6AJ:https://www.coffeebean.com/&cd=20&hl=en&ct=clnk&gl=us",
            "related_pages_link": "https://www.google.com/search?gl=us&hl=en&q=related:https://www.coffeebean.com/+Coffee",
            "source": "Coffee Bean"
            }
        ]
    }
    def test_parse_contains(self):
        """
        The function `test_simple_substitute` tests the parsing of search results for specific text patterns
        using regular expressions.
        """
        tool = web_search_tool.WebSearch()
        res = tool.parse_results(self.res_dict)
        self.assertRegexpMatches(res, r"Coffee is a beverage prepared from roasted coffee beans.")
        self.assertRegexpMatches(res, r"Born and brewed in Southern California since 1963, The Coffee Bean & Tea Leaf® is passionate about connecting loyal")

    def test_parse_not_contain(self):
        """
        The function `test_simple_substitute` tests the parsing of search results for specific text patterns
        using regular expressions.
        """
        tool = web_search_tool.WebSearch()
        res = tool.parse_results(self.res_dict)
        self.assertNotRegexpMatches(res, r"https://en.wikipedia.org/wiki/Coffee")
        self.assertNotRegexpMatches(res, r"Wikipedia is a multilingual free online encyclopedia written and maintained by")


if __name__ == '__main__':
    unittest.main()