import autogen


class AutoGenInteraction:
    def __init__(self, api_key, transcription):
        # gpt-4o is removed from the API on 2027-01-14; gpt-6-luna is OpenAI's
        # replacement (https://developers.openai.com/api/docs/deprecations).
        # Luna rejects temperature unless reasoning_effort is "none", so it is
        # no longer set here.
        self.llm_config = {
            "config_list": [{
                "model": "gpt-6-luna",
                "api_key": api_key
            }],
            "cache_seed": None
        }
        self.transcription = transcription

    def initiate_chat(self):
        user = autogen.UserProxyAgent(
            "user",
            system_message="You are an administrator.",
            human_input_mode="NEVER",
            is_termination_msg=lambda msg: "TERMINATE" in msg["content"],
            code_execution_config=False,
        )

        agent_summarizer = autogen.AssistantAgent(
            "agent_summarizer",
            system_message="You are an assistant agent. When you are done, reply with TERMINATE",
            llm_config=self.llm_config
        )

        agent_translator = autogen.AssistantAgent(
            "ai_agent_translator",
            system_message="You are an assistant agent. When you are done, reply with TERMINATE",
            llm_config=self.llm_config
        )

        user.initiate_chats(
            [
                {
                    "recipient": agent_summarizer,
                    "message": f"Can you summarize: {self.transcription} this nicely with the title and then bullet "
                               f"points?",
                    "clear_history": True,
                    "silent": False,
                    "summary_method": "last_msg",
                    "max_turns": 1
                },
                {
                    "recipient": agent_translator,
                    "message": "Can you translate this into Dutch?",
                    "summary_method": "last_msg",
                },
            ]
        )
