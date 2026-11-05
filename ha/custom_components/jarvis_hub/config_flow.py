import voluptuous as vol
from homeassistant import config_entries

from . import DOMAIN

DEFAULT_URL = "http://127.0.0.1:8099"


class JarvisHubFlow(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION = 1

    async def async_step_user(self, user_input=None):
        if self._async_current_entries():
            return self.async_abort(reason="single_instance_allowed")
        if user_input is not None:
            return self.async_create_entry(title="Jarvis Hub", data={"url": user_input["url"].rstrip("/")})
        return self.async_show_form(step_id="user", data_schema=vol.Schema({vol.Required("url", default=DEFAULT_URL): str}))
