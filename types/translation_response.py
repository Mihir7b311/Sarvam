# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class TranslationResponse(UniversalBaseModel):
    request_id: typing.Optional[str] = None
    translated_text: str = pydantic.Field()
    """
    Translated text result in the requested target language.
    """

    source_language_code: str = pydantic.Field()
    """
    Detected or provided source language of the input text.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
