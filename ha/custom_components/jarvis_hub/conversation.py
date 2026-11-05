"""Conversation agent: sends what the speaker heard to the phone-voice server on the Pi (/ask) and speaks back its answer."""
import logging

import aiohttp
from homeassistant.components import conversation
from homeassistant.const import MATCH_ALL
from homeassistant.helpers import intent
from homeassistant.helpers.aiohttp_client import async_get_clientsession

_LOGGER = logging.getLogger(__name__)


async def async_setup_entry(hass, entry, async_add_entities):
    async_add_entities([JarvisHubAgent(entry)])


class JarvisHubAgent(conversation.ConversationEntity):
    _attr_has_entity_name = True
    _attr_name = None

    def __init__(self, entry):
        self._entry = entry
        self._attr_unique_id = entry.entry_id

    @property
    def supported_languages(self):
        return MATCH_ALL

    async def async_added_to_hass(self):
        await super().async_added_to_hass()
        try:  # older Home Assistant versions need the agent registered by hand
            conversation.async_set_agent(self.hass, self._entry, self)
        except Exception:  # newer versions register the entity themselves
            pass

    async def _reply(self, user_input):
        resp = intent.IntentResponse(language=user_input.language)
        url = self._entry.data.get("url", "http://127.0.0.1:8099") + "/ask"
        try:
            session = async_get_clientsession(self.hass)
            async with session.post(url, json={"format": "json", "text": user_input.text, "audio": False, "source": "home"}, timeout=aiohttp.ClientTimeout(total=40)) as r:
                data = await r.json()
            text = (data.get("reply") or "").strip() or "Sorry, I did not catch that."
            resp.async_set_speech(text)
        except Exception as err:  # keep the speaker usable even if the Pi voice server is down
            _LOGGER.warning("Jarvis Hub could not reach %s: %s", url, err)
            resp.async_set_error(intent.IntentResponseErrorCode.UNKNOWN, "I could not reach my brain on the Pi.")
        return conversation.ConversationResult(response=resp, conversation_id=user_input.conversation_id)

    async def _async_handle_message(self, user_input, chat_log):
        return await self._reply(user_input)

    async def async_process(self, user_input):
        return await self._reply(user_input)
