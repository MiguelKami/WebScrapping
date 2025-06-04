# coding: utf-8
"""Generate simple short videos about 'Enigmas ancestrais'.
   The script fetches short facts, converts them to audio using gTTS,
   creates a simple slideshow video with text overlays and audio using
   moviepy, and saves the final MP4 file. This can be used as a basis
   to post on YouTube, TikTok or Instagram.
"""

import os
import tempfile
from gtts import gTTS
from moviepy.editor import (
    ColorClip,
    TextClip,
    CompositeVideoClip,
    concatenate_videoclips,
    AudioFileClip,
)


def fetch_enigma_facts():
    """Return a list of dictionaries with short enigma facts."""
    return [
        {
            "title": "As Linhas de Nazca",
            "description": (
                "Até hoje cientistas debatem o propósito das misteriosas linhas "
                "no deserto do Peru."
            ),
        },
        {
            "title": "O Manuscrito de Voynich",
            "description": (
                "Um livro medieval cheio de ilustrações e uma linguagem "
                "indecifrável que intriga pesquisadores."
            ),
        },
        {
            "title": "Stonehenge",
            "description": (
                "A finalidade exata do monumento megalítico inglês permanece "
                "um enigma." 
            ),
        },
    ]


def create_audio(text, lang="pt"):
    """Convert text to speech and return the audio file path."""
    tts = gTTS(text, lang=lang)
    audio_path = tempfile.mktemp(suffix=".mp3")
    tts.save(audio_path)
    return audio_path


def create_clip(title, description):
    """Create a short video clip for a single enigma."""
    # Background color clip avoids the need for external images
    img_clip = ColorClip(size=(1280, 720), color=(30, 30, 30)).set_duration(5)

    audio_path = create_audio(f"{title}. {description}")
    audio = AudioFileClip(audio_path)

    text_clip = (
        TextClip(
            title,
            fontsize=60,
            color="white",
            font="DejaVu-Sans",
            stroke_color="black",
            method="label",
        )
        .set_position("center")
        .set_duration(audio.duration)
    )

    image_clip = img_clip.set_duration(audio.duration)
    clip = CompositeVideoClip([image_clip, text_clip]).set_audio(audio)
    return clip


def create_video(facts, output="enigma_short.mp4"):
    clips = [create_clip(f["title"], f["description"]) for f in facts]
    final_clip = concatenate_videoclips(clips, method="compose")
    final_clip.write_videofile(output, fps=24)
    print(f"Video salvo em {output}")


if __name__ == "__main__":
    facts = fetch_enigma_facts()
    create_video(facts)
