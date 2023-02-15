import openai
from dotenv import load_dotenv

load_dotenv()

music_category_mapping = {
    0: 'gangsta rap',
    1: 'heavy metal',
    2: 'polish disco polo'
}


class OpenAIProxy(object):
    @classmethod
    def create_album_cover(cls, cover_description: str) -> str:
        response = openai.Image.create(
            prompt=cover_description,
            n=1,
            size="256x256",
        )
        return response['data'][0]['url'] if response else ''

    @classmethod
    def create_lyrics(cls, song_theme: str, music_category: str, count: int = 1) -> list[str]:
        prompt = 'Write a short {category} song about {theme}'.format(
            category=music_category_mapping[music_category],
            theme=song_theme,
        )
        return cls._create_multiple_text_completion(prompt=prompt, count=count)

    @classmethod
    def create_titles(cls, lyrics: list[str]) -> str:
        titles = []
        prompt = 'Provide me a title for a song with the following lyric: {lyric}'
        for lyric in lyrics:
            title = cls._create_multiple_text_completion(prompt=prompt.format(lyric=lyric), count=1, max_tokens=100)
            titles.append(title[0])
        return titles

    @classmethod
    def _create_multiple_text_completion(cls, prompt: str, count: int, max_tokens:int = 1024) -> list[str]:
        response = openai.Completion.create(
          model="text-curie-001",
          prompt=prompt,
          n=count,
          max_tokens=max_tokens,
          temperature=0,
        )

        return [choice.text for choice in response['choices']]
