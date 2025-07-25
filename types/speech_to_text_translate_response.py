# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .diarized_transcript import DiarizedTranscript
from .speech_to_text_translate_language import SpeechToTextTranslateLanguage


class SpeechToTextTranslateResponse(UniversalBaseModel):
    request_id: typing.Optional[str] = None
    transcript: str = pydantic.Field()
    """
    Transcript of the provided speech
    """

    language_code: typing.Optional[SpeechToTextTranslateLanguage] = pydantic.Field(default=None)
    """
    This will return the BCP-47 code of language spoken in the input. If multiple languages are detected, this will return language code of most predominant spoken language. If no language is detected, this will be null
    """

    diarized_transcript: typing.Optional[DiarizedTranscript] = pydantic.Field(default=None)
    """
    Diarized transcript of the provided speech
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
