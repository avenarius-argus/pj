import logging
import feedparser
from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.dispatch_components import AbstractExceptionHandler
from ask_sdk_core.utils import is_request_type, is_intent_name
from ask_sdk_model.ui import SimpleCard
from ask_sdk_model import Response

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)



class GetRSSFeedIntentHandler(AbstractRequestHandler):
    """Handler for getting the RSS feed"""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_intent_name("GetRSSFeedIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Union[None, Response]
        rss_feed_url = "https://www.example.com/rss"
        feed = feedparser.parse(rss_feed_url)
        speech_text = "Here is the latest episode from the podcast: " + feed.entries[0].title

        handler_input.response_builder.speak(speech_text).set_card(
            SimpleCard("RSS Feed", speech_text)).set_should_end_session(
            True)
        return handler_input.response_builder.response


class PlayPodcastIntentHandler(AbstractRequestHandler):
    """Handler for playing a podcast episode"""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_intent_name("PlayPodcastIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Union[None, Response]
        rss_feed_url = "https://www.example.com/rss"
        feed = feedparser.parse(rss_feed_url)
        speech_text = "Playing the latest episode from the podcast: " + feed.entries[0].title

        handler_input.response_builder.speak(speech_text).set_card(
            SimpleCard("Podcast", speech_text)).set_should_end_session(
            True)
        return handler_input.response_builder.response


class HelpIntentHandler(AbstractRequestHandler):
    """Handler for providing help information"""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_intent_name("AMAZON.HelpIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Union[None, Response]
        speech_text = "You can ask me to get the latest episode from the podcast, or to play a podcast episode. How can I help you?"

        handler_input.response_builder.speak(speech_text).set_card(
            SimpleCard("Help", speech_text)).set_should_end_session(
            False)
        return handler_input.response_builder.response
