from textwrap import dedent
from urllib.parse import quote


def on_page_markdown(markdown, **kwargs):
    page = kwargs["page"]
    config = kwargs["config"]
    title = page.title
    percent_title = quote(title)
    url = config.site_url + page.url
    percent_url = quote(url)
    percent_bsky_text = quote(f"{title} {url}")
    return markdown + dedent(
        f"""

                            ---

                            <div markdown class="s-list-none-container">
                            - <a class="md-button s-style s-share-button s-share-bsky" href="javascript:void(0)" onclick="window.open('https://bsky.app/intent/compose?text={percent_bsky_text}', '_blank', 'width=800, height=450')">:fontawesome-brands-bluesky:</a>
                            - <a class="md-button s-style s-share-button s-share-x" href="javascript:void(0)" onclick="window.open('https://x.com/intent/tweet?text={percent_title}&url={percent_url}', '_blank', 'width=800, height=450')">:fontawesome-brands-x-twitter:</a>
                            - <a class="md-button s-style s-share-button s-share-copy" href="javascript:void(0)" data-clipboard-text="{url}">:material-link-variant:</a>
                            - <a class="md-button s-style s-share-button s-share-os" href="javascript:share()">:material-share-variant:</a>
                            </div>
                            <script>
                            async function share()
                            {{
                                if (!window.navigator.share)
                                {{
                                    alert('OS share is not available in your environment...');
                                    return;
                                }}
                                console.log('{page.title}');
                                await window.navigator.share({{
                                    title: '{page.title}',
                                    url: '{url}',
                                }});
                            }}
                            </script>

                            """
    )
