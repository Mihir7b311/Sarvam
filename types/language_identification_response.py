# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class LanguageIdentificationResponse(UniversalBaseModel):
    request_id: typing.Optional[str] = None
    language_code: typing.Optional[str] = pydantic.Field(default=None)
    """
    The detected language code of the input text.
    
    Available languages:
    - **`en-IN`**: English
    - **`hi-IN`**: Hindi
    - **`bn-IN`**: Bengali
    - **`gu-IN`**: Gujarati
    - **`kn-IN`**: Kannada
    - **`ml-IN`**: Malayalam
    - **`mr-IN`**: Marathi
    - **`od-IN`**: Odia
    - **`pa-IN`**: Punjabi
    - **`ta-IN`**: Tamil
    - **`te-IN`**: Telugu
    """

    script_code: typing.Optional[str] = pydantic.Field(default=None)
    """
    The detected script code of the input text.
    
    Available scripts:
    - **`Latn`**: Latin (Romanized script)
    - **`Deva`**: Devanagari (Hindi, Marathi)
    - **`Beng`**: Bengali
    - **`Gujr`**: Gujarati
    - **`Knda`**: Kannada
    - **`Mlym`**: Malayalam
    - **`Orya`**: Odia
    - **`Guru`**: Gurmukhi
    - **`Taml`**: Tamil
    - **`Telu`**: Telugu
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
