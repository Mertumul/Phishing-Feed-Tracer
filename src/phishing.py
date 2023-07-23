import aiohttp
from typing import List
from database import bulk_insert_phishing_url
import logging


async def get_phishing_url_from_txt(url: str) -> List[str]:
    """
    Asynchronously fetches phishing URLs from a text file.

    Args:
        url (str): The URL of the text file containing phishing URLs.

    Returns:
        List[str]: A list of unique phishing URLs fetched from the text file.
    """

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                lines = await response.text()
                unique_urls = set(
                    line.strip() for line in lines.split("\n") if line.strip()
                )
                return list(unique_urls)
            else:
                return []


async def get_alienvault_phishing_feed(url: str) -> List[str]:
    """
    Asynchronously fetches AlienVault phishing feed data.

    Args:
        url (str): The URL of the AlienVault phishing feed API.

    Returns:
        List[str]: A list of unique phishing URLs fetched from the AlienVault feed.
    """

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status == 200:
                    data = await response.json()
                    indicators = [item["indicator"] for item in data["results"]]
                    unique_indicators = list(set(indicators))
                    return unique_indicators
                else:
                    return []
    except aiohttp.ClientError as e:
        print("Hata oluştu:", e)
        return []


async def get_tweet_phishing_feed(url: str) -> List[str]:
    """
    Asynchronously fetches Tweet phishing feed data.

    Args:
        url (str): The URL of the Tweet phishing feed CSV file.

    Returns:
        List[str]: A list of unique phishing URLs fetched from the Tweet phishing feed.
    """

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status == 200:
                    lines = (await response.text()).split("\n")
                    urls = [
                        line.split(",")[3].strip()
                        for line in lines
                        if len(line.split(",")) >= 4
                    ]
                    unique_urls = list(set(urls))
                    return unique_urls
                else:
                    print("Dosya indirilemedi. Hata kodu:", response.status)
                    return []
    except aiohttp.ClientError as e:
        print("Hata oluştu:", e)
        return []


async def get_phishtank_feed(url: str) -> None:
    """
    Asynchronously fetches Phishtank phishing feed data and bulk inserts into the database.

    Args:
        url (str): The URL of the Phishtank phishing feed CSV file.

    Returns:
        Returns None.
    """

    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
        }
        async with aiohttp.ClientSession(headers=headers) as session:
            async with session.get(url) as response:
                if response.status == 200:
                    csv_data = await response.text()
                    rows = [row.split(",") for row in csv_data.split("\n")[1:] if row]
                    urls = [row[1][:1000] for row in rows]

                    chunk_size = 1000
                    for i in range(0, len(urls), chunk_size):
                        chunk = urls[i : i + chunk_size]
                        await bulk_insert_phishing_url(chunk)

                    logging.info("Phishtank Phishing Feeds saved successfully")
                else:
                    logging.error(
                        f"Error: {response.status}, message='{response.reason}', url={response.url}"
                    )
    except Exception as e:
        logging.error(f"Error: {str(e)}")
