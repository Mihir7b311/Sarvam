# This file was auto-generated by Fern from our API Definition.

import typing_extensions
from ..types.finish_reason import FinishReason
from .chat_completion_response_message import ChatCompletionResponseMessageParams


class ChoiceParams(typing_extensions.TypedDict):
    finish_reason: FinishReason
    """
    The reason the model stopped generating tokens. This will be `stop` if the model hit a natural stop point or a provided stop sequence,
    `length` if the maximum number of tokens specified in the request was reached,
    `content_filter` if content was omitted due to a flag from our content filters,
    `tool_calls` if the model called a tool, or `function_call` (deprecated) if the model called a function.
    """

    index: int
    """
    The index of the choice in the list of choices.
    """

    message: ChatCompletionResponseMessageParams
